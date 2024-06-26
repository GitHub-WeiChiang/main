2 - 关系模型: 主键和外键
=====
* ### 关系数据库中表與表之间的逻辑关系
    * ### 一对多
    * ### 多对一
    * ### 一对一
* ### 系所資料表與學生資料表的關係為: 一对多。
* ### 系所資料表與系主任資料表的關係為: 一对一。
* ### 主鍵: 关系表中有个很重要的约束，就是任意两条记录不能重复，这里的不能重复指的是每条记录需要一个能和其他记录区别开来的特定字段，这个字段称为 "主键"。
* ### 關於 "主鍵"
    * ### 记录一旦被插入表中，"主键最好不要修改"，因为主键是用来定位记录的，主键的变动必然会造成一定的影响。
    * ### 选取主键的基本原则: 盡可能不选取任何与业务相关的字段作为主键。
* ### 最好选择与业务完全无关的字段作为主键，一般这个字段命名为 id，常见的可作为 id 字段的类型如下:
    * ### 自增整数类型 (通常自增类型的主键就能满足需求)
    * ### 全局唯一 GUID 类型
* ### 联合主键: 通过多个字段来定位记录，既使用两个或多个字段作为主键，这种主键叫做联合主键。
* ### 外键
    * ### 一对多
        * ### 系所資料表與學生資料表的關係。
        * ### 學生資料表中有一列為系所 id，此時系所 id 就是學生資料表的外鍵，且其必須為系所資料表的主鍵。
    * ### 多对一
        * ### 課程資料表與學生資料表的關係。
        * ### 創建一個 "中間表"，其中有兩個列分別為課程 id 與學生 id，此兩列皆為中間表格的外鍵，且其必須各自為程資料表與學生資料表的主鍵，彼此相互映射。
    * ### 一对一
        * ### 學生資料表與學生進階資訊表的關係。
        * ### 學生進階資訊表有一列為學生 id，此時學生 id 就是學生進階資訊表的外鍵，且其必須為學生資料表的主鍵。
* ### 关系型数据库中的数据需要用表格来存储，表的每一行叫记录 (Record)，表的每一列称为字段 (Column)。
* ### 外键必须是其它表的主键。
* ### 表格之间的关系有三种: "一对一"、"一对多"與"多对多"。
* ### 在多对多的关系中，需要创建一个中间表来连接互相关的两张表。
<br />
