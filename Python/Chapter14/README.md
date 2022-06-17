Chapter14
=====
* ### 一個物件可以被稱為描述器 (Descriptor)，它必須有 \_\_get\_\_() 方法和選擇性的 \_\_set\_\_() 與 \_\_delete\_\_() 方法。
* ### 資料描述器可以攔截對實例的屬性取得、設定與刪除行為；非資料描述器，是用來攔截透過實例取得類別屬性時的行為。
* ### 若想控制可以指定給物件的屬性名稱，可以在定義類別十時指定 \_\_slots\_\_。
* ### 物件本身可以定義 \_\_getattribute\_\_()、\_\_getattr\_\_()、\_\_setattr\_\_()、\_\_delattr\_\_() 等方法決定存取屬性的行為。
* ### 簡單的裝飾器可以使用函式，可接受函式且傳回函式。
* ### 類別的 \_\_class\_\_() 參考至 type 類別，每個類別也是一個物件，是 type 類別的實例。
* ### 物件是類別的實例，類別是 type 的實例，如果有方法能介入 type 建立實例與初始化的過程，就會有辦法改變類別的行為，這就是 meta 類別的基本概念。
* ### meta 類別就是 type 的子類別，藉由 metaclass = MetaClass 的協定，可在類別定義剖析完後，繞送至指定的 meta 類別，可以定義 meta 類別的 \_\_new\_\_() 方法，決定類別如何建立，定義 meta 類別的 \_\_init\_\_()，則可以決定類別如何初始，而定義 meta 類別的 \_\_call\_\_() 方法，決定若使用類別來建構物件時，該如何進行物件的建立與初始。
* ### 兩種匯入方式: 絕對匯入 (Abstract import)、相對匯入 (Relative import)。
* ### 如果 B 是 A 的子類別，而 Node[B] 可視為一種 Node[A]，則稱 Node 是有共變性或有彈性的 (flexible)。
* ### TypeVar 建立的佔位型態預設為不可變 (Non variant)，但可透過 covariant 為 True 來支援共變。
* ### 如果 B 是 A 的子類別，而 Node[A] 可視為一種 Node[B]，則稱 Node 具有逆變性 (Contravariance)。
* ### 可藉由 contravariant 為 True 來支援逆變性。