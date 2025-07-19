Question056 - Docker Container Port 小複習: 如何映射與相互連接 ?
=====
* ### 在 Docker 的 port 映射語法中
    ```
    -p <host_port>:<container_port>
    ```
* ### 所以
    ```
    -p 8888:8888
    ```
    * ### 左邊的 8888 是 主機 (Host) 的 port。
    * ### 右邊的 8888 是 容器 (Container) 的 port。
* ### 容器之間的相互連接 (例如透過 Docker network 時): 它們彼此是直接連到對方的 container port，而不是主機 port。因為在同一個 Docker network 裡，容器會像是同一個內部網路下的主機一樣互通，這時候與主機的 port 就完全沒有關係。
    ```
    # 建立一個新的 Docker 網路: 可以讓多個容器彼此之間通訊，就像它們連在同一個虛擬交換機上。
    docker network create NETWORK_NAME

    # 把已經存在的容器連接到指定的 Docker 網路: 讓某個已經運行中的容器，加入到建立的網路裡。
    docker network connect NETWORK_NAME CONTAINER_NAME
    ```
* ### 在 Docker Compose 中，當兩個容器要互相通信時，它們之間是透過「容器內部的網路」互連的，不會使用到主機的對應 port，在容器之間通信時，會直接使用「容器內部的 port」。
* ### Docker Compose 相關指令
    * ### Attached Mode (前景執行)
        ```
        docker-compose -p app up --build

        -p app: 指定專案名稱為 app。
        up: 啟動服務 (若需要會自動建構 Image 與 Container 並啟動)。
        --build: 啟動前會先重新建構 Image（就算之前已經建構過）。
        ```
    * ### Detached Mode (背景執行)
        ```
        docker-compose -p app up --build -d

        -p app: 指定專案名稱為 app。
        up: 啟動服務 (若需要會自動建構 Image 與 Container 並啟動)。
        --build: 啟動前會先重新建構 Image（就算之前已經建構過）。
        -d: 分離模式。
        ```
<br />
