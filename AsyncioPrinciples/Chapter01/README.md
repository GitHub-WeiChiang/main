Chapter01 簡介 Asyncio
=====
* ### Python 3 的 Asyncio: 可以在程式中執行多個並行 (concurrent) 的 HTTP 要求。
* ### Asyncio 改變了程式在架構時的思考模式。
* ### Asyncio 著重的是，多個作業同時執行時，如何做到最好。
* ### Asyncio 並不是什麼作業都能處理，而是那些涉及到等待的作業。
* ### Asyncio 在等待作業完成的這段時間，可以去執行其它作業。
* ### ThreadBots 餐廳故事的閉幕語
  * ### 電腦程式設計涉及網路設計時，CPU 執行作業並等待網路 I/O，現代電腦的 CPU 在運作時，速度會比網路訊息溝通快上幾十萬倍，因此，CPU 執行網路程式時，會耗費大量的等待時間。
  * ### Asyncio 的解決方案是，撰寫程式在必要時，明確要求 CPU 轉換作業。
  * ### 在經濟效益上，用比較少的 CPU 以相似的效能來做同樣的事 (Asyncio 在定義上是單執行緒)。
  * ### 相較於多執行緒，Asyncio 避免了競速 (Race Condition) 問題。
* ### Asyncio 想解決的問題 ?
  * ### 對於 I/O 密集式的作業，決定不使用執行緒，而採用非同步的並行方案，其實只有兩個理由:
    * ### 相較於先佔式多工 (Preemptive Multitasking)，也就是所謂的執行緒，Asyncio 是更安全的替代方案，可以避免複雜執行緒應用程式上常見的臭蟲、競速以及其它難以確認的風險。
    * ### 針對數以萬計的 Socket 連線，Asyncio 提供一個簡明的支援方式，像是處理多個 WebSocket 之類新技術的長時連線，或者是 IoT (Internet of Things) 應用程式的 MQTT。
  * ### 執行緒適用於運算作業，在多核心 CPU 執行，且共享記憶體，即便這是必要之惡。
  * ### 網路程式設計則非上述適用場景，網路程式設計涉及大量的 "等待某事發生"，不需要作業系統有效率地在多 CPU 上指派作業，進一步的也就不需要承擔先佔式多工帶來的風險，像是共享記憶體所造成的競速問題。
* ### 基於 "事件" 的設計模型不正確的認知
  * ### Asyncio 可以讓程式碼快到飛起來
    * ### 執行緒方案還是稍微快了些。
    * ### Asyncio 在建立大量並行 Socket 連線時確實比較輕量。
    * ### 協程 (Coroutine) 能避免上萬執行緒帶來的環境切換 (Context - Switching) 成本。
    * ### Asyncio 帶來的不是速度上的效益，如果追求速度，請找隔壁棚的 Cython。
    * ### 在 Linux 中，一次執行緒環境切換大約是 50 微秒 (這是一個非常粗略的估算大概值)，意味著一千個執行緒環境切換成本約為 50 毫秒，確實是個負擔，但也不致於毀了程式。
  * ### Asyncio 讓執行緒險得多餘
    * ### 執行緒真正的價值在於設計多 CPU 程式，且不同運算作業間可以共享記憶體。
    * ### 在 CPU 密集式 (CPU - Bound) 的作業上，多執行緒是無敵的。
  * ### Asyncio 避免了 GIL 的問題
    * ### Asyncio 確實不受 GIL 的影響，這是因為 GIL 只影響多執行緒。
    * ### GIL 阻礙了真正的多核平行 (Parallelism)。
    * ### Asyncio 在定義上是單執行緒的，所以不受 GIL 影響，相對的無法從多 CPU 核心上獲得效益。
  * ### Asyncio 可以避免競速
    * ### 任何可並行程式都有競速的問題。
    * ### Asyncio 只避免了多執行緒設計上某些類型的競速問題，像是內部程序的共享記憶體存取。
    * ### Asyncio 未避免其它類型的競速問題，像是分散式微服務架構常見的內部程序的共享資源問題。
    * ### Asyncio 優勢在於，可以看得出協程間轉換了執行權 (因為有 await 關鍵字，Asyncio 遇到它時會進行等待，也就是會跑去做其它事)，因此更易於推導出共享資源的存取方式。
  * ### Asyncio 簡化了並行程式設計
    * ### 並行程式設計必然複雜...
* ### 全局解譯器鎖 (Global Interpreter Lock, GIL) 藉由鎖定每個操作碼 (opcode)，確保 Python 解譯器的程式碼 (非開發者的程式碼) 是執行緒安全，帶來的負面效應是，解譯器會被釘在單一 CPU 上執行，因而阻礙了多核平行化。
<br />
