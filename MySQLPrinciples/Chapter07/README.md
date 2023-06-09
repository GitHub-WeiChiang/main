Chapter07 B+ 樹索引的使用
=====
* ### 一個索引對應一個 B+ 樹，最下面一層為葉子節點 (使用者紀錄)，其餘為內節點 (目錄項記錄)。
* ### 一個 "組" 中 "最大" 的記錄會被 "放置到槽" 以便定位。
* ### 一個 "頁" 中 "最小" 的記錄會被 "放置到目錄項" 以便定位。
* ### B+ 樹是一個矮矮的大胖子臭肥宅。
* ### 聚簇索引葉子節點中的記錄 -> 聚簇索引記錄。
* ### 二級索引葉子節點中的記錄 -> 二級索引記錄。
* ### 索引的代價
    * ### 索引是個好東西，但是不能肆意創建。
    * ### 會拖空間與時間的後腿。
    * ### 一個索引對應一顆 B+ 樹，一個節點就是一個資料頁，一個資料頁要 16 KB。
    * ### 每一次的增刪改操作都需要修改各個 B+ 樹，最可怕的是此操作連帶造成的排序破壞，需要額外進行頁面分裂與頁面回收。
    * ### 過多的 B+ 樹會使執行計畫生成時分析與計算各個索引的使用成本過程耗時太多。
* ### 掃描區間和邊界條件
    * ### 全資料掃描: 掃描表中的所有記錄，從聚簇索引的第一筆一路到最後一筆。
    * ### B+ 樹索引可以用於快速定位，後再執行單向鏈結串列掃描 (此動作將對應一個 "掃描區間")。
    * ### 掃描區間: 單點掃描、範圍掃描。
    * ### 全資料表掃描有也掃描區間 -> (-∞, +∞)。
    * ### 沒有形成掃描區間的搜索條件將被稱為 "普通搜索條件"，會透過 "回表操作" 或是 "索引下推" 進行比對。
    * ### 使用索引查詢的關鍵為: 透過搜索條件找出適合的掃描區間，後至相應的 B+ 樹中搜索記錄 (只需搜索位於 "掃描區間" 的記錄，這樣就快多了)。
    * ### 若以字串作為比對條件，只有完整字串與字串字首匹配才能產生掃描區間。
    * ### 執行查詢敘述時，要先找出所有可用的掃描區間。
    * ### 若需要回表操作，將在每獲取到一筆二級索引記錄時執行。
* ### 索引下推
    * ### 沒有開啟，乖乖回表。
    * ### 若有開啟，需要才回表。
    * ### 在 MySQL 5.6 中引入且預設為開啟。
    * ### 索引條件下推 (index condition pushdown) 發生在聯合索引查詢。
* ### 索引用於排序
    * ### 排序 (ORDER BY): 將記錄載入記憶體，透過排序算法排序，若記憶體不夠用則借助磁碟空間存放中間結果。
    * ### 在記憶體或是磁碟中進行排序統稱為 "檔案排序 (filesort)"。
    * ### ORDER BY 子句中若使用索引列，且按索引列順序要求，有可能省去在記憶體或磁碟中排序的步驟。
    * ### 雖然 Query 中有 ORDER BY 子句並且其使用的列也建立了索引，但若 Select 過多欄位且搜尋太多筆錄，使回表操作造成的成本大於前述所節省的成本，可能導致最佳化查詢選用全資料掃描。
    * ### 無法觸發 ORDER BY 索引 (上述) 情況
        * ### ASC 與 DESC 混用 (MySQL 8.0 引入 Descending Index 支援混用)。
        * ### 包含非同一索引的列。
        * ### 排列順序與聯合索引不同或是不連續。
        * ### 形成掃描區間的索引並非 ORDER BY 中的列。
        * ### 該列非單獨出現 (如被函數操作等)。
    * ### 降冪排序透過索引的查詢步驟 (找尋上一筆記錄的過程)
        * ### 從自己出發 (透過 next_record)
        * ### 找到大哥 (n_owned 不為 0)
        * ### 找到大哥所在槽的前 (上) 一個槽
        * ### 找到該槽的大哥的下一筆記錄 (自己這組的第一筆記錄)
        * ### 遍歷找到自己的前一筆記錄
    * ### 聯合索引對分組可能有顯著的效能提升，因為不用在 GROUP BY 查詢時特別建立臨時表進行分組。
* ### 回表的代價 (InnoDB)
    * ### 所以中的資料頁存放於磁碟，需要時載入記憶體。
    * ### 執行一次的頁 I/O 可以把多筆記錄載入。
    * ### 每在記憶體讀取一筆二級索引記錄就需要執行回表操作。
    * ### 如果對應的聚簇索引所在頁面不在記憶體中，就需要到磁碟載入頁面。
    * ### 如果二級索引的記錄其在聚簇索引並不連續則會造成大量隨機 I/O。
    * ### 最佳化查詢工具會負責判斷該使用何種查詢方式。
    * ### 回表越多傾向全資料掃描，反之使用二級索引。
    * ### 可以透過 LIMIT 使最佳化查詢工具傾向使用二級索引 + 回表操作。
    * ### SELECT 查詢清單欄位太多，可能導致最佳化查詢工具傾向使用全資料掃描 + 檔案排序 (若有需要)。
* ### 更進一步的創建和使用索引
    * ### 只為用於搜索、排序或分組的列創建索引: 沒有用於以上操作的列，沒必要創建，如果不知道原因，回去重讀。
    * ### 考慮索引列中不重複值的個數: 不重複比例太低代表需要進行大量回表操作，所以不重複比例高的列較適合創建索引。
    * ### 索引列的類型儘量小: 類型小，儲存索引的資料頁就可以儲存更多的記錄，除了降低儲存空間的佔用，最重要的是一次的 I/O 可以載入更多記錄到記憶體，使讀寫效率提升 (主鍵更應該是如此)。
    * ### 為列字首建立索引: 可以縮小索引大小。
    * ### 覆蓋索引 (索引下推)
        * ### 查詢清單盡可能只包含索引列 (index + primary key)
        * ### 當索引中包含所有需要讀取列的查詢方式稱為 "覆蓋索引"。
        * ### 不過還是以業務需求為主啦。
    * ### 讓索引列以列名稱的形式在搜索條件中 "單獨" 出現。
    * ### 新插入記錄時主鍵大小對效率的影響
        * ### 如果插入主鍵忽大忽小使頁分裂操作頻繁，將會造成性能影響。
        * ### 最好讓插入的記錄主鍵依次遞增。
    * ### 容錯索引和重複索引
        * ### 應避免容錯索引和重複索引的建立。
        * ### 容錯索引: 針對聯合索引的第一個索引又單獨創建了一個二級索引。
        * ### 重複索引: 針對聚簇索引或唯一二級索引又單獨創建了一個二級索引。
<br />
