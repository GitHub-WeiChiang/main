03 - 資料存取
=====
* ### MongoDB 在新增資料時，若資料庫與資料表不存在，會自動建立。
* ### 新增文件時，"_id" 欄位可以自行指定，若未指定或指定為 null 則 MongoDB 會使用 ObjectId() 函數生成。
* ### "_id" 欄位的型態可以是字典，但不能是陣列。
* ### 新增文件時，若 "_id" 欄位型態不正確或是該值已經存在皆會引發錯誤。
* ### 常用數字型態比較運算子
    * ### "$gt": 大於。
    * ### "$gte": 大於等於。
    * ### "$lt": 小於。
    * ### "$lte": 小於等於。
    * ### "$ne": 不等於。
* ### MongoDB 限制一份文件大小不能超過 16M bytes，若要儲存影片、WORD 文件、MP3 音樂、JPEG 與 PDF 等，需使用 GridFS。
* ### GridFS (Grid File System)
    * ### 以檔案為單位。
    * ### 存放在指定的資料表 (Collection) 中，也就是說每一個資料表只會有一個獨立的 GridFS 儲存區。
    * ### 完全獨立，不會與其它文件混在一起。
* ### GridFS 的結構
    * ### 使用兩個資料表儲存資料: fs.files + fs.chunks。
    * ### fs.files: 記錄檔案資訊 (名稱、大小與上傳時間等)。
    * ### fs.chunks: 檔案實際內容。
<br />

範例程式
=====
* ### 3_1_2.py: 使用 Python 新增資料。
* ### 3_1_6.py: 儲存開放資料平台上的資料。
* ### 3_2.py: 查詢所有資料。
* ### 3_3.py: 修改資料。
* ### 3_4.py: 刪除資料。
* ### 3_5.py: 取代資料。
* ### 3_6.py: 用 GridFS 儲存大型檔案。
<br />
