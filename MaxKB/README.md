MaxKB
=====
* ### MaxKB，祖國牛 B，單押 x 1。
* ### This is a Quick Start Guide that documents how to deploy a Knowledge Based QA (KBQA, Knowledge Base Question Answering) system based on the LLM (Large Language Model) in an offline environment using Docker.
* ### Architecture: MaxKB -> Ollama -> Meta Llama 3 (8B)。
* ### Basic commands for Ollama
    ```
    # Pull a model.

    ollama pull llama3:8b
    ```
    ```
    # Run a model (interactive mode).

    ollama run llama3:8b
    ```
    ```
    # Remove a model.

    ollama rm llama3:8b
    ```
    ```
    # Copy a model.

    ollama cp llama3:8b my-llama3:8b
    ```
    ```
    # List models currently hosted.

    ollama list
    ```
    ```
    # Start a server.

    ollama serve
    ```
    ```
    # When requesting ollama api from another PC (Windows).

    set OLLAMA_HOST=0.0.0.0
    ollama serve
    ```
    ```
    # Run ollama in cpu-mode.

    $ ollama run MODEL_NAME
    >>> /set parameter num_gpu 0
    Set parameter 'num_gpu' to '0'
    >>> Hi
    ```
* ### Other commands for Ollama
    ```
    # Start the server.

    ./ollama serve
    ```
    ```
    # In a separate shell.

    ./ollama run llama3
    ```
* ### REST API for Ollama
    ```
    # Generate a response.

    curl http://localhost:11434/api/generate -d '{
        "model": "llama3",
        "prompt":"Why is the sky blue?"
    }'
    ```
    ```
    # Chat with a model.

    curl http://localhost:11434/api/chat -d '{
        "model": "llama3",
        "messages": [
            { "role": "user", "content": "why is the sky blue?" }
        ]
    }'
    ```
* ### 如何连接和使用 Ollama API
    * ### 默认地址和端口: Ollama API 的默认地址是 ```http://localhost:11434```，可以在安装 Ollama 的系统中直接调用。
    * ### 修改 API 的侦听地址和端口: 如果要在网络中提供服务，可以修改 API 的侦听地址和端口。
        1. ### 右击点击任务栏图标，选择「Quit Ollama」退出后台运行。
        2. ### 使用 Windows + R 快捷键打开「运行」对话框，输入命令 ```sysdm.cpl```。
        3. ### 系统属性 -> 环境变量 -> 用户变量 -> 新增变量记录。
        4. ### 变量名設置為 ```OLLAMA_HOST```、变量值 (端口) 設置為 ```:11434```。
        5. ### 重新运行 Ollama 后在浏览器中测试访问验证更改是否成功。
* ### Ollama v0.1.33 - Experimental concurrency features
    * ### New concurrency features are coming soon to Ollama. They are available
        * ### ```OLLAMA_NUM_PARALLEL```: Handle multiple requests simultaneously for a single model
        * ### ```OLLAMA_MAX_LOADED_MODELS```: Load multiple models simultaneously
    * ### To enable these features, set the environment variables for ollama serve. For more info see [this guide](https://github.com/ollama/ollama/blob/main/docs/faq.md#how-do-i-configure-ollama-server):
        ```
        OLLAMA_NUM_PARALLEL=4 OLLAMA_MAX_LOADED_MODELS=4 ollama serve
        ```
    * ### Setting environment variables on Windows: On Windows, Ollama inherits your user and system environment variables.
        * ### First Quit Ollama by clicking on it in the task bar.
        * ### Start the Settings (Windows 11) or Control Panel (Windows 10) application and search for environment variables.
        * ### Click on Edit environment variables for your account.
        * ### Edit or create a new variable for your user account for OLLAMA_HOST, OLLAMA_MODELS, etc.
        * ### Click OK/Apply to save.
        * ### Start the Ollama application from the Windows Start menu.
* ### Ollama Model File
    * ### First, you need to create a file named ```Modelfile``` without any file extension.
    * ### Basic Modelfile (An example of a Modelfile creating a mario blueprint)
        ```
        FROM llama3.1
        # sets the temperature to 1 [higher is more creative, lower is more coherent]
        PARAMETER temperature 1
        # sets the context window size to 4096, this controls how many tokens the LLM can use as context to generate the next token
        PARAMETER num_ctx 4096

        # sets a custom system message to specify the behavior of the chat assistant
        SYSTEM You are Mario from super mario bros, acting as an assistant.
        ```
        1. ### Save it as a file (e.g. Modelfile)
        2. ### ollama create choose-a-model-name -f <location of the file e.g. ./Modelfile>'
        3. ### ollama run choose-a-model-name
        4. ### Start using the model!
    * ### To view the Modelfile of a given model, use the ```ollama show --modelfile``` command.
    * ### 參考 -> [click me](https://github.com/ollama/ollama/blob/main/docs/modelfile.md)
* ### Ollama Docker Image
    ```
    # CPU only.

    docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama
    ```
    ```
    # Run model locally.

    docker exec -it ollama ollama run llama3:8b
    ```
    * ### Note: To execute basic commands targeting the Ollama container running in Docker, need to prepend it with the prefix ```docker exec -it ollama ...``` ("..." stands for basic commands of Ollama).
* ### MaxKB Quick Start
    ```
    docker run -d --name=maxkb -p 8080:8080 -v ~/.maxkb:/var/lib/postgresql/data 1panel/maxkb

    # Account: admin
    # Password: MaxKB@123..
    # Access Ollama: http://host.docker.internal:11434
    # The "-v" flag can also be used to mount a local host directory into the container.
    ```
    ```
    docker run -d --name=maxkb -p 8080:8080 -v LOCAL_FOLDER_LOCATION:/var/lib/postgresql/data 1panel/maxkb
    ```
    ```
    docker run -d --name=maxkb -p 8080:8080 -v LOCAL_FOLDER_LOCATION:/opt/maxkb/app -v LOCAL_FOLDER_LOCATION:/var/lib/postgresql/data 1panel/maxkb
    ```
* ### Migration of Images in Docker
    ```
    # Save.

    docker save IMAGE_NAME -o IMAGE_NAME.tar
    ```
    ```
    # Load.

    docker load -i IMAGE_NAME.tar
    ```
* ### Migration of Volumes in Docker
    ```
    # Backup.

    docker run --rm -v VOLUME_NAME:/volume busybox sh -c 'tar -cOzf - /volume' > volume-export.tgz

    # The "--rm" flag removes the container after it stops.
    # The "-v VOLUME_NAME:/volume" specifies the name of the volume to be exported and its mount point inside the container.
    # busybox: The name of the image running in the container. BusyBox is a small Linux distribution commonly used for lightweight container tasks.
    # sh -c 'tar -cOzf - /volume': The command running inside the container, which packages the specified volume into a compressed tar file.
    # > volume-export.tgz: Redirects the output of the "tar" command inside the container to a local file named "volume-export.tgz".
    ```
    ```
    # Restore.

    docker run --rm -i -v VOLUME_NAME:/volume busybox sh -c "tar -xzvf - -C /" < volume-export.tgz

    # -i: Allows the process inside the container to read data from standard input.
    # -v VOLUME_NAME:/volume: Specifies the name of the volume to be imported and its mount point inside the container.
    # sh -c "tar -xzvf - -C /": The command running inside the container, which uses the tar tool to extract the tar file from standard input to the root directory (/) of the container.
    # < volume-export.tgz: Redirects the local "tar" file named "volume-export.tgz" to the standard input of the container.
    ```
    * ### Note: Busybox is merely an intermediary image and container, theoretically replaceable with any similarly lightweight Docker application.
    * ### Note: Can achieve "Volume Migration" more conveniently using ```Volumes Backup & Share```, refer to the reference below for more information.
* ### Migration of Container in Docker
    ```
    # Docker container export.

    # The following commands produce the same result.
    docker export red_panda > latest.tar
    docker export --output="latest.tar" red_panda
    ```
    ```
    # Docker image import.

    # Import from a remote location.
    docker import https://example.com/exampleimage.tgz
    # Import from a local file.
    docker import /path/to/exampleimage.tgz
    ```
* ### To copy a running container's folder:
    * ### 找到容器的名稱或 ID
        ```
        docker ps
        ```
    * ### 使用 ```docker cp``` 命令將檔案複製到主機
        ```
        # 命令格式

        docker cp <容器 ID 或名稱>:<容器內要被複製出來的資料夾路徑> <主機資料夾路徑>

        docker cp <container_id>:/path/to/container/directory /path/to/host/directory
        ```
        ```
        # 命令示例: 將容器中的 opt 資料夾複製到主機當前工作目錄下的 opt 資料夾

        docker cp <容器ID或名稱>:/opt ./opt
        ```
    * ### 如果遇到 ```A Required Privilege Is Not Held By a Client``` 錯誤，通常是由於缺乏適當的權限來執行該操作，打開「命令提示符」或「PowerShell」時，右鍵點擊並選擇「以管理員身份運行」即可。
<br />

Steps for Offline Deployment by Docker
=====
* ### On a computer with internet access:
    * ### Download and install Docker Desktop.
    * ### Run the Ollama application in Docker and download an appropriate LLM model.
    * ### Run the MaxKB application in Docker and attempt to access Ollama.
    * ### Prepare the ```Image``` of busybox in Docker.
    * ### Save the ```Image(s)``` of the Ollama and MaxKB applications.
    * ### Backup the ```Volume``` of the Ollama application through busybox.
* ### Find a way to bring the following files into a computer that cannot access the internet:
    * ### Docker Desktop installer
    * ### ```Image``` of Ollama
    * ### ```Image``` of MaxKB
    * ### ```Image``` of busybox
    * ### ```Volume``` of Ollama (which is the LLM model)
* ### In a computer that cannot access the Internet:
    * ### Install Docker Desktop (Pay attention to WSL update issues).
    * ### Load the ```Image``` of the Ollama application.
    * ### Load the ```Image``` of the MaxKB application.
    * ### Load the ```Image``` of the busybox application.
    * ### Run the ```Image``` of Ollama as a ```Container```.
    * ### Run the ```Image``` of MaxKB as a ```Container```.
    * ### Restore the ```Volume``` of Ollama.
    * ### Enjoy using it !
<br />

Deploy MaxKB in a Windows 11 environment (A mixed bag)
=====
* ### Python Version: 3.11.9 -> [click me](https://www.python.org/downloads/release/python-3119/)
* ### PostgreSQL Version: 15.8 -> [click me](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads)
* ### Node.js ->[click me](https://nodejs.org/zh-cn)
    * ### Issue
        * ### Question: ```no such file or directory, open '......package.json'```
        * ### Answer: ```進入路徑 MaxKB\ui 資料夾並運行，因為 npm install 就是在運行資料夾中尋找 package.json 檔案並下載當中所定義的 dependencies```
* ### PostgreSQL: Default username and password.
    ```
    username: postgres
    password: 空
    ```
* ### Start the psql command line
    ```
    psql -U postgres
    ```
    * ### Issue
        * ### Question: ```psql: 無法將 "psql" 識別為 cmdlet、函數、腳本文件.....```
        * ### Answer: ```在文件資源管理器中進入 C:\Program Files\PostgreSQL\15\bin 資料夾路徑後開啟 cmd 輸入上方指令即可正常運行```
        * ### Node: ```應該也可透過將上方目錄添加到環境變量中解決，操作步驟參考下方 Add the vector plugin in PostgreSQL -> Then use nmake to build -> Issue -> Answer```
* ### Add the vector plugin in PostgreSQL
    * ### Ensure [C++ support in Visual Studio](https://learn.microsoft.com/en-us/cpp/build/building-on-the-command-line?view=msvc-170#download-and-install-the-tools) is installed, and run:
        ```
        call "C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Auxiliary\Build\vcvars64.bat"
        ```
        * ### Note: The exact path will vary depending on your Visual Studio version and edition.
        * ### Issue
            * ### Question: ```call: 無法將 "call" 識別為 cmdlet、函數、腳本文件......```
            * ### Answer: ```請在 cmd 中運行，誤於 PowerShell 中運行```
    * ### Then use nmake to build:
        ```
        set "PGROOT=C:\Program Files\PostgreSQL\16"
        cd %TEMP%
        git clone --branch v0.7.4 https://github.com/pgvector/pgvector.git
        cd pgvector
        nmake /F Makefile.win
        nmake /F Makefile.win install
        ```
        * ### Note: Must be run as an "administrator".
        * ### Note: ```%TEMP%``` can be any folder.
        * ### Issue
            * ### Question: ```"nmake" 不是內部或外部命令，也不是可運行的程序或批處理文件......```
            * ### Answer:
                ```
                將 Visual Studio 中的 VC/bin 目錄添加到環境變量中，可按以下步驟進行操作:
                1. 打開 "控制面板" -> "系統和安全" -> "系統" -> "高級系統設置" -> "環境變量"。
                2. 在 "用戶變量 or 系統變量" 中找到 "Path" 並按下編輯。
                3. 點擊 "新建" 後輸入 Visual Studio 的 VC/bin 目錄路徑 (例如: "C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Tools\MSVC\14.40.33807\bin\Hostx64\x64")。
                4. 按下 "確定" 保存修改後，關閉所有命令提示符窗口並重新打開一個新的命令提示符窗口，再次運行上述指令即可。
                ```
* ### Issue
    * ### Question: ```Error: No module named 'fcntl'```
    * ### Answer: ```The problem is gunicorn. It doesn't support Windows.```
* ### 別妄想了! 退坑!! -> [click me](https://blog.csdn.net/taotao_guiwang/article/details/140993737)
<br />

修改 VMware Fusion Virtual Machine Hard Disk
=====
* ### Step 1: VMware Fusion Menu bar -> Virtual Machine -> Shut Down (趁虛擬機不注意)
* ### Step 2: Virtual Machine -> Settings -> Hard Disk
* ### Step 3: Done ~

VMware Fusion Pro: 在 Windows 11 (VM) 上安裝 Ubuntu (WSL) 的奇幻歷險記
=====
* ### WSL 与 Ubuntu 的关系
    * ### WSL: 是 Windows 提供的一种功能，允许在 Windows 上运行 Linux 环境。WSL 并不完全模拟一个 Linux 系统，而是直接调用 Linux 内核接口来运行 Linux 应用程序。
    * ### Ubuntu: 是一种 Linux 发行版，可以在 WSL 上安装和运行。当在 WSL 中选择 Ubuntu 时，实际上是在 Windows 上安装和运行 Ubuntu 的 Linux 用户空间环境。
    * ### 总结来说: WSL 是一个平台，使得在 Windows 上可以运行 Ubuntu (或其它 Linux 发行版) 变得可能。Ubuntu 则是在 WSL 上可以安装并使用的具体 Linux 发行版。
* ### Step 1: 到 Microsoft Store 中下載 Ubuntu 並安裝。
    * ### Microsoft Store -> [click me](https://apps.microsoft.com/home?hl=zh-tw&gl=TW)
    * ### Ubuntu -> [click me](https://apps.microsoft.com/search?query=ubuntu&hl=zh-tw&gl=TW)
    * ### Ubuntu LTS (Long-Term Support) 是 Ubuntu 操作系统的一个特殊版本，旨在提供更长时间的支持和稳定性。与常规的 Ubuntu 版本相比，LTS 版本在以下几个方面有所不同:
        * ### 支持周期更长: 桌面版可获得 3 年支持，服务器版可获得 5 年支持。
        * ### 稳定性优先: LTS 版本主要关注稳定性和安全性，而不是引入最新功能。
        * ### 软件包更新较少: 与常规版本相比，LTS 版本中的软件包更新较少 (常规版首先引入，测试后移植到 LTS)。
        * ### 适合生产环境： 其稳定性和长期支持使 LTS 版本在服务器环境和企业生产环境中得到广泛应用。
        * ### 默认应用版本较为保守： LTS 版本中倾向于选择相对保守的默认应用程序版本。
        * ### 常规的 Ubuntu 約每 6 个月发布一次，其會包含最新的特性、改进和更新的软件包。
* ### Step 2: 開啟 Ubuntu，然後就會遇到一連串的問題。
* ### Step 3: WslRegisterDistribution failed with error: 0x8007019e
    * ### 透過管理員模式開啟 PowerShell 並啟用 Windows Subsystem for Linux (WSL)。
    * ### 輸入 ```Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux``` 後再輸入 ```y```。
    * ### 開啟 Ubuntu。
    * ### 文章參考 -> [click me](https://blog.csdn.net/qq_37109456/article/details/109669455)
* ### Step 4: WslRegisterDistribution failed with error: 0x800701bc
    * ### 下载安装适用于 x64 计算机的最新 WSL2 Linux 内核更新包。
    * ### 下载链接 -> [click me](https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi)
    * ### 開啟 Ubuntu。
    * ### 文章參考 -> [click me](https://blog.csdn.net/microsoft_mos/article/details/123627295)
* ### Step 5: WslRegisterDistribution failed with error: 0x80370102
    * ### 此錯誤通常表示虛擬機器平台功能 (Virtual Machine Platform) 或硬體虛擬化技術 (例如 Intel VT-x 或 AMD-V) 未啟用。這些功能對於 WSL 2 來說是必須的，但對於 WSL 1 則不是。
    * ### 可將預設的 WSL 版本設為 WSL 1，而不是 WSL 2。由於 WSL 1 不需要虛擬機器平台功能，因此這個操作能夠成功解決問題。
    * ### 透過管理員模式開啟 PowerShell。
        ```
        C:\Windows\System32> wsl --set-default-version 1
        the operation completed successfuly
        ```
        * ### 輸入 ```wsl --set-default-version 1```。
        * ### 若出現 ```the operation completed successfully``` 則恭喜老爺賀喜老爺。
    * ### 開啟 Ubuntu。
    * ### 設定帳號和密碼。
    * ### 文章參考 -> [click me](https://ithelp.ithome.com.tw/articles/10312130)
* ### Step 6: Done ~
* ### Tips: WSL Linux 子系统与 Windows 文件互操作
    * ### 从 Windows 进入 WSL 目录的方式: 在文件资源管理器中输入 ```\\wsl$```。
    * ### 从 Linux 下进入 Windows 文件夹方式: 终端输入 ```cd /mnt/```。
* ### Tips: WslRegisterDistribution failed with error: 0x80370102 的其它可能解決方案
    * ### 检查相关 Windows 功能是否开启
        * ### 控制面板 -> 程序 -> 程序和功能 -> 啟動或關閉 Windows 功能。
        * ### 檢查選項 ```適用於 Linux 的 Windows 子系統``` 是否勾選。
    * ### 透過管理員模式開啟 PowerShell 並輸入下方指令
        ```
        # 启用适用于 Linux 的 Windows 子系统
        dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart

        # 启用虚拟机功能
        dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
        ```
    * ### 下载 Linux 内核更新包並執行。
        ```
        https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi
        ```
    * ### 開啟 Ubuntu。
    * ### 文章參考 -> [click me](https://blog.csdn.net/q20010619/article/details/120660346)
<br />

Windows 11 (VM): 在 Ubuntu (WSL) 上安裝 MaxKB 的奇幻歷險記
=====
* ### 開始前須知: 如果在安裝過程中遇到錯誤訊息 ```... are you root?```，請加上 ```sudo```。
* ### Python
    ```
    # 更新系統軟體包：首先，更新你的系統軟體包列表。
    sudo apt update

    # 安裝依賴項：安裝必要的依賴項，以確保安裝 Python 時沒有問題。
    sudo apt install -y software-properties-common

    # 添加 deadsnakes PPA：這個 PPA（Personal Package Archive）提供了許多 Python 版本，包括 3.11。
    sudo add-apt-repository ppa:deadsnakes/ppa

    # 更新系統軟體包列表：再次更新軟體包列表以加載新的 PPA。
    sudo apt update

    # 安裝 Python 3.11.9：使用以下命令安裝指定的 Python 版本。
    sudo apt install python3.11

    # 檢查安裝版本：確認 Python 3.11.9 是否已成功安裝。
    python3.11 --version
    ```
* ### Git
    ```
    # 更新包列表
    sudo apt update

    # 安装 Git
    sudo apt install git

    # 验证安装
    git --version
    ```
* ### MaxKB
    ```
    # /home/你的用戶名

    # 克隆整个仓库
    git clone https://github.com/1Panel-dev/MaxKB.git

    # 切换到特定标签 (對於開源項目，永遠記得使用發行版本運行)
    cd MaxKB
    git tag
    git checkout v1.4.1
    ```
* ### 最好是在 MaxKB 的根目錄內建立和使用虛擬環境，這樣可以確保虛擬環境包含所有 MaxKB 所需的依賴和設定。
* ### 在 MaxKB 的根目錄內建立虛擬環境，也有助於避免與其他專案的依賴發生衝突。
* ### 若尚未進入 MaxKB 資料夾，請滾進去: ```cd MaxKB```。
* ### pip
    ```
    # 下载 get-pip.py 脚本
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py

    # 用 Python 3.11 来运行这个脚本
    python3.11 get-pip.py

    # 验证 pip 安装
    python3.11 -m pip --version
    ```
* ### venv
    ```
    # 安装 Python 3.11 的虚拟环境模块
    sudo apt install python3.11-venv

    # 创建一个虚拟环境
    python3.11 -m venv venv

    # 激活虚拟环境
    source venv/bin/activate

    # 验证 Python 與 pip 版本是否正確
    python -V
    pip -V
    ```
* ### poetry (run in venv)
    ```
    pip install poetry

    poetry install
    ```
* ### Node.js
    ```
    # 添加 NodeSource 的 PPA
    curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -

    # 安装 Node.js
    sudo apt install -y nodejs

    # 检查版本
    node -v
    npm -v

    # 在 ui 資料夾执行安装前端需要的依赖
    npm install

    # 嘗試启动项目
    npm run dev
    ```
* ### PostgreSQL (記得回到 MaxKB 資料夾中)
    ```
    # Import the repository signing key:
    sudo apt install curl ca-certificates
    sudo install -d /usr/share/postgresql-common/pgdg
    sudo curl -o /usr/share/postgresql-common/pgdg/apt.postgresql.org.asc --fail https://www.postgresql.org/media/keys/ACCC4CF8.asc

    # Create the repository configuration file:
    sudo sh -c 'echo "deb [signed-by=/usr/share/postgresql-common/pgdg/apt.postgresql.org.asc] https://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'

    # Update the package lists:
    sudo apt update

    # Install the latest version of PostgreSQL:
    # If you want a specific version, use 'postgresql-15' or similar instead of 'postgresql'
    sudo apt -y install postgresql-15
    ```
    ```
    # 确认安装是否成功
    dpkg -l | grep postgresql

    # 检查安装的版本
    psql --version

    # 启动 PostgreSQL 数据库
    sudo service postgresql start

    # 检查 PostgreSQL 服务的状态
    sudo service postgresql status

    # 登录 PostgreSQL 数据库
    sudo -u postgres psql

    # 退出命令行界面
    \q
    ```
* ### pgvector (建議在 "/home/你的用戶名" 中執行)
    ```
    mkdir tmp

    cd tmp

    git clone --branch v0.7.4 https://github.com/pgvector/pgvector.git

    cd pgvector

    make
    # 遇到 "Command 'make' not found" 執行 "sudo apt install make"
    make
    # 遇到 "make: gcc: No such file or directory" 執行 "sudo apt install gcc"
    make
    # 遇到 "fatal error: postgres.h: No such file or directory" 執行 "sudo apt install postgresql-server-dev-15"
    make

    sudo make install
    ```
* ### Create a MaxKB database
    ```
    sudo -u postgres psql

    CREATE DATABASE "maxkb";

    \c "maxkb";

    CREATE EXTENSION "vector";

    \q
    ```
* ### 啟動前準備
    * ### 如果有 Visual Studio Code 會很好 -> [click me](https://code.visualstudio.com/)
    * ### 准备配置文件 (在 MaxKB 資料夾中進行操作)
        ```
        sudo mkdir -p /opt/maxkb/conf
        sudo cp config_example.yml /opt/maxkb/conf
        ```
    * ### 配置 /opt/maxkb/conf/config_example.yml
        ```
        # 数据库配置
        DB_NAME: maxkb
        DB_HOST: localhost
        DB_PORT: 5432
        DB_USER: postgres
        DB_PASSWORD: Aa123456
        DB_ENGINE: django.db.backends.postgresql_psycopg2

        # 模型相关配置
        EMBEDDING_MODEL_PATH: /opt/maxkb/model/
        # 模型名称
        EMBEDDING_MODEL_NAME: /opt/maxkb/model/shibing624_text2vec-base-chinese
        ```
    * ### 幫 postgres 加上密碼
        ```
        # 登录 PostgreSQL 数据库
        sudo -u postgres psql

        # 修改密碼
        ALTER USER postgres WITH PASSWORD 'Aa123456';

        # 退出 PostgreSQL 命令行
        \q
        ```
    * ### 配置 PostgreSQL 以使用密码进行身份验证
        ```
        # 找到
        /etc/postgresql/{version}/main/pg_hba.conf
        # 將
        local   all             postgres                                peer
        # 改
        local   all             postgres                                md5

        # 重新启动 PostgreSQL 服务
        sudo service postgresql restart

        # 验证新用户设置
        psql -U postgres -W
        ```
* ### 原神 ~ 啟動 !!!
    ```
    # Ubuntu 1: 在 ui 資料夾启动项目

    npm run dev
    ```
    ```
    # Ubuntu 2: 在 MaxKB 資料夾中進行操作

    # 原神 ~ 啟動 !!!
    # 如果尚未啟動資料庫
    sudo service postgresql start
    # 啟動 MaxKB
    source venv/bin/activate
    python main.py start
    ```
    ```
    # 訪問
    http://localhost:3000/ui/login

    # 用户名與密码
    admin
    MaxKB@123..

    # 修改密碼
    Aa123456
    ```
* ### Note: 推薦使用 Ollama 支援 LLM 和 Embedding。
    * ### ```ollama run phi3```
    * ### ```ollama run gemma2```
    * ### ```ollama run llama3.1```
    * ### ```ollama pull nomic-embed-text```
    * ### ```ollama pull mxbai-embed-large```
* ### 在 Windows 上配置端口转发
    1. ### 打开命令提示符: 以管理员身份运行命令提示符 (cmd)。
    2. ### 设置端口转发
        ```
        netsh interface portproxy add v4tov4 listenaddress=173.0.0.120 listenport=8080 connectaddress=localhost connectport=3000

        netsh interface portproxy add v4tov4 listenaddress=173.0.0.120 listenport=8080 connectaddress=127.0.0.1 connectport=3000

        # 这将把外部访问 173.0.0.120:8080 的请求转发到 localhost or 127.0.0.1。
        ```
    3. ### 检查端口转发规则
        ```
        netsh interface portproxy show all
        ```
        * ### 若要删除所有端口转发规则请执行 ```netsh interface portproxy reset```。
    4. ### 配置防火墙: 打开 Windows 防火墙，添加入站规则，允许访问 8080 端口。
        * ### 通常情况下，在设置端口转发时，只需要配置入站规则，因为这是为了允许外部流量进入你的计算机并访问指定的端口。输出规则通常在默认情况下已经允许所有流量出去，所以不需要特别配置。
        * ### 输入和输出规则主要控制的是主动发起的流量，而被动响应的流量通常不受这些规则的限制。
<br />

将 WSL Ubuntu 分发打包并移植到離線电脑
=====
```
# 列出所有 WSL 分发
wsl --list --verbose

# 停止 Ubuntu 分发
wsl --terminate Ubuntu-24.04

# 导出 Ubuntu 分发
wsl --export Ubuntu-24.04 ubuntu.tar

# 导入 Ubuntu 分发
wsl --import Ubuntu <Install_Location> ubuntu_backup.tar
# wsl --import Ubuntu C:\WSL\Ubuntu ubuntu_backup.tar

# 列出所有 WSL 分发
wsl --list --verbose

# 启动特定分发
wsl -d Ubuntu-24.04

# 设置默认分发
wsl --set-default Ubuntu-24.04

# 启动默认分发
wsl
```
* ### 始終優先嘗試透過 WSL 2 執行所導入的分發: WSL 1 是一個將 Linux 系統調用翻譯為 Windows 系統調用的模擬環境，對於某些系統功能和文件系統的支持有限；而 WSL 2 則使用了真正的 Linux 核心，提供了一個完整的虛擬化環境，能夠更好地模擬和支持 Linux 系統的各種功能。
* ### WSL Export Automation (Batch file)
    ```
    @echo off
    rem 列出當前的 WSL 分發
    wsl -l -v

    rem 提示使用者是否要繼續執行下一步
    set /p input1=是否要繼續停止 Ubuntu-24.04 分發 (y/n)? 
    if /i "%input1%"=="n" goto :end

    rem 停止 Ubuntu-24.04 分發
    wsl --terminate Ubuntu-24.04

    rem 再次列出當前的 WSL 分發
    wsl -l -v

    rem 提示使用者是否要繼續執行下一步
    set /p input2=是否要繼續 export 出 Ubuntu-24.04 (y/n)? 
    if /i "%input2%"=="n" goto :end

    rem export 出 Ubuntu-24.04 分發並以日期命名 tar 檔案
    set "datetime=%date:~0,4%%date:~5,2%%date:~8,2%"
    wsl --export Ubuntu-24.04 %datetime%_Ubuntu-24.04.tar

    :end
    echo 程式已結束
    pause
    ```
<br />

簡體繁體轉換腳本
=====
```
import os
from opencc import OpenCC

# 設置轉換為繁體的轉換器
cc = OpenCC('s2twp')  # 's2twp' 是專門將簡體轉換為台灣正體（繁體）的轉換器，會包含一些台灣用詞習慣的轉換。

# 設置要處理的資料夾
src_folder = ''

# 遍歷 src 資料夾下的所有文件
for root, dirs, files in os.walk(src_folder):
    for file_name in files:
        file_path = os.path.join(root, file_name)

        # 讀取文件內容
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()

            # 將內容轉換為繁體
            converted_content = cc.convert(content)

            # 將轉換後的內容寫回文件
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(converted_content)

            print(f"已轉換文件: {file_path}")

        except Exception as e:
            # 如果文件不是文本格式（例如二進制文件），可能會導致錯誤
            print(f"跳過文件（無法轉換）: {file_path}，錯誤信息: {e}")
```
<br />

Reference
=====
* ### Ollama -> [click me](https://ollama.com/)
* ### Ollama GitHub -> [click me](https://github.com/ollama/ollama)
* ### Ollama Docker -> [click me](https://hub.docker.com/r/ollama/ollama)
* ### MaxKB GitHub -> [click me](https://github.com/1Panel-dev/MaxKB)
* ### Volumes Backup & Share -> [click me](https://hub.docker.com/extensions/docker/volumes-backup-extension)
* ### MaxKB Documentation -> [click me](https://maxkb.cn/docs/dev_manual/dev_environment/)
* ### pgvector -> [click me](https://github.com/pgvector/pgvector)
* ### VMware Fusion -> [click me](https://www.youtube.com/watch?v=QTs9sHN6W5A)
<br />
