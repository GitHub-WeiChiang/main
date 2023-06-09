Chapter14 基於規則的最佳化 (內含子查詢最佳化二三事)
=====
* ### 條件化簡
    * ### 移除不必要的括號。
    * ### 常數傳遞。
    * ### 移除沒用的條件。
    * ### 運算式計算。
    * ### HAVING 子句和 WHERE 子句的合併。
    * ### 常數表檢測。
        * ### 設計 MySQL 的工程師認為下述兩種類型的查詢速度很快。
        * ### 查詢表中一筆記錄都沒有或是只有一筆記錄。
        * ### 使用主鍵相等匹配或唯一二級索引列相等匹配作為搜索條件來查詢某表。
        * ### 上述兩種查詢方式所查詢的表被稱為 "常數表 (constant table)"。
        * ### 查詢最佳化工具在分析一個查詢敘述時，首先執行常數表查詢，然後會把涉及該表的條件全替換成常數，最後才分析其餘表的查詢成本。
    * ### 註: HAVING 子句與 WHERE 子句的差異為，前者可以搭配 Aggregate Function。
* ### 外連接消除
    * ### "內連接" 的 "驅動表" 和 "被驅動表" 的 "位置可以相互轉換"。
    * ### "外連接" 無論是左連接還是又連接，驅動表和被驅動表是固定的 "不可戶換"。
    * ### 因此，"內連接" 可能 "透過最佳化表連接順序" 降低整體查詢成本。
    * ### 而 "外連接" 無法最佳化表連接順序。
    * ### 複習一下:
        * ### 內連接的兩個表: "驅動表" 中的記錄在 "被驅動表" 中無法匹配時，"不加入" 結果集。
        * ### 外連接的兩個表: "驅動表" 中的記錄在 "被驅動表" 中無法匹配時，"仍加入" 結果集 (使用 NULL 填充欄位)。
    * ### 在 WHERE 子句的搜索條件中指定 "被驅動表的列不為 NULL"，這種情況下，外連接和內連接本質上就沒有區別了。
    * ### 上述方法被稱為 "空值拒絕 (reject - NULL)"。
    * ### 使用 "空值拒絕" 會導致外連接和內連接可以相互轉換，好處就是最佳化器可以透過評估不同連接順序成本，選擇連接順序成本最低的方案執行查詢。
* ### 子查詢最佳化
    * ### 出現在某個查詢 (外層查詢) 敘述的某個位置中的查詢就稱為子查詢 (寶寶查詢)。
    * ### 當子查詢被放置在 FROM 子句後，這個子查詢被稱為 "衍生表"。
* ### 按返回結果集區分子查詢
    * ### 純量子查詢: 只返回一個單一值。
    * ### 行子查詢: 返回一筆記錄的子查詢 (需包含數個列)。
    * ### 列子查詢: 返回一個列的資料 (需包含數個行)。
    * ### 表子查詢: 包還多筆記錄的數個列。
* ### 按與外層查詢的關係來區分子查詢
    * ### 不相關子查詢: 子查詢可以單獨運行出結果，不依賴於外層查詢的值。
    * ### 相關子查詢: 子查詢的執行需要依賴外層查詢的值。
* ### 子查詢在布林運算式中的使用
    * ### 使用 =、>、<、>=、<=、<>、!=、<=> 時，子查詢結果需為單一值。
    * ### 使用 [NOT] IN / ANY / SOME / ALL 時，子查詢結果相當於一個集合。
    * ### [NOT] IN: 判斷某運算元是否 (不) 存在於由子查詢結果集組成的集合中。
    * ### ANY / SOME (兩者同意): 在子查詢結果集組成的集合中存在一個符合比較的值。
    * ### ALL: 在子查詢結果集組成的集合中全部都符合比較的值。
    * ### EXISTS: 是否有記錄。
* ### 子查詢注意事項
    * ### 小括號括起來。
    * ### 在 SELECT 子句中的子查詢必需為純量子查詢。
    * ### 如果渴望得到純量子查詢或行子查詢，但又無法保證結果，加上 LIMIT 1 吧。
    * ### 使用 [NOT] IN / ANY / SOME / ALL 時，子查詢中不允許有 LIMIT 敘述 (這是規定)。
    * ### 如果要進行增刪改就不允許同時執行子查詢操作。
* ### 小白眼中的子查詢執行方式
    * ### 不相關子查詢: 先執行子查詢，後執行外層查詢。
    * ### 相關子查詢: 先取的一筆外層查詢記錄，後套用於子查詢並執行，重複上述之。
* ### 純量子查詢、行子查詢的執行方式
    * ### 不相關子查詢: 如同小白所知。
    * ### 相關子查詢: 如同小白所知。
* ### 物化表的提出 (對於不相關的 IN 子查詢)
    * ### 不直接將不相關子查詢的結果集當作外層查詢的參數，而是將該結果集寫入一個臨時表中 (臨時表的列就是子查詢結果集的列、寫入記錄會被去重)。
    * ### 一般情況，基於 MEMORY 儲存引擎建立臨時表，並會建立雜湊索引。
    * ### MySQL 雜湊索引: 基於雜湊表實現，MEMORY 儲存引擎預設索引型別，支援非唯一雜湊索引。
    * ### 如果子查詢結果真的太多，會改用基於磁碟的儲存引擎進行之，但相對的索引類型也會被轉變為 B+ 樹索引。
    * ### 重點來了，"將子查詢結果集中的記錄保存到臨時表的過程稱為物化 (materialize)"，該臨時表可稱為 "物化表"。
    * ### 如此，可以加速 IN 判斷的性能。
* ### 物化表轉連接
    * ### 如上所述，不相關的 IN 子查詢，其實就是 "某表" 與 "物化表 (臨時表)" 進行 "內連接"，如此查詢最佳化工具就可以評估不同連接順序的成本，選擇較佳執行方案。
* ### 將子查詢轉為半連接 (semi - join)
    * ### 這是一種 MySQL 內部執行方式，不提供外部使用者呼叫。
    * ### 不進行物化，直接轉為連接敘述。
* ### 子查詢轉為半連接執行方法 (詳細內容請參閱書籍 14-23 頁)
    * ### Table pullout (子查詢中的表上拉): 當子查詢的查詢列表只有主鍵或唯一索引列。
    * ### Duplicate Weedout (重複值消除): 使用臨時表消除半連接結果集中重複值。
    * ### LooseScan (鬆散掃描): 只取鍵值相同的第一筆記錄執行匹配操作。
    * ### Semi - join Materialization (半連接物化): 先把外層查詢的 IN 子句中的不相關子查詢進行物化，然後再將外層查詢的表與物化表進行連接。
    * ### FirstMatch (第一次匹配): 就是小白眼中的相關子查詢執行方式。
* ### 半連接適用條件
    * ### 子查詢與 IN 組成布林運算，並出現於外層查詢的 WHERE 或 ON 子句中。
    * ### 使用 AND 與 IN 連接的子查詢。
    * ### 子查詢為一個單一查詢，非由 UNION 連接。
    * ### 子查詢不包含 GROUP BY、HAVING 或聚集函數。
* ### 不適用於半連接
    * ### 在外層的 WHERE 中存在其它搜索條件並使用 OR 與 IN 串接子查詢。
    * ### 使用 NOT IN。
    * ### 位於 SELECT 子句中的 IN 子查詢。
    * ### 子查詢中包含 GROUP BY、HAVING 或聚集函數。
    * ### 子查詢中包含 UNION。
* ### MySQL 面對不能轉為半連接查詢的子查詢 (詳細內容請參閱書籍 14-28 頁)
    * ### 對於不相關子查詢，先物化後再參與查詢。
    * ### 無論為相關亦或是不相關子查詢，嘗試將 IN 轉為 EXISTS (可以增加使用索引機率)。
* ### 若 IN 子查詢可以轉為半連接，查詢最佳化工具會優先進行轉換，並從以下五種策略中選擇成本最低的執行。
    * ### Table pullout
    * ### Duplicate Weedout
    * ### LooseScan
    * ### Semi - join Materialization
    * ### FirstMatch
* ### 若 IN 子查詢不符合轉為半連接的條件
    * ### 將子查詢物化，在執行查詢。
    * ### 執行 IN 到 EXISTS 轉換。
* ### 對於衍生表的最佳化
    * ### 把衍生表物化。
    * ### 將衍生表與外層查詢合併。
<br />
