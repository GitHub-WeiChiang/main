MaxKB
=====
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
    ```
    docker cp <container_id>:/path/to/container/directory /path/to/host/directory
    ```
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
===
* ### Step 1: VMware Fusion Menu bar -> Virtual Machine -> Shut Down
* ### Step 2: Virtual Machine -> Settings -> Hard Disk
* ### Step 3: Done ~

VMware Fusion Pro: 在 Windows 11 (VM) 上安裝 Ubuntu (WSL) 的奇幻歷險記
===
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
    * ### 透過管理員模式開啟 PowerShell。
    * ### 輸入 ```Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux``` 後再輸入 ```y```。
    * ### 開啟 Ubuntu。
    * ### 文章參考 -> [click me](https://blog.csdn.net/qq_37109456/article/details/109669455)
* ### Step 4: WslRegisterDistribution failed with error: 0x800701bc
    * ### 下载安装适用于 x64 计算机的最新 WSL2 Linux 内核更新包。
    * ### 下载链接 -> [click me](https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi)
    * ### 開啟 Ubuntu。
    * ### 文章參考 -> [click me](https://blog.csdn.net/microsoft_mos/article/details/123627295)
* ### Step 5-1: WslRegisterDistribution failed with error: 0x80370102
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
* ### Step 5-2: WslRegisterDistribution failed with error: 0x80370102
    * ### 透過管理員模式開啟 PowerShell。
    * ### 輸入 ```wsl --set-default-version 1```。
    * ### 若出現 ```the operation completed successfully``` 則恭喜老爺賀喜老爺。
    ```
    C:\Windows\System32> wsl --set-default-version 1
    the operation completed successfuly
    ```
    * ### 開啟 Ubuntu。
    * ### 設定帳號和密碼。
    * ### 文章參考 -> [click me](https://ithelp.ithome.com.tw/articles/10312130)
* ### Step 6: Done ~
* ### Tips: WSL Linux 子系统与 Windows 文件互操作
    * ### 从 Windows 进入 WSL 目录的方式: 在文件资源管理器中输入 ```\\wsl$```。
    * ### 从 Linux 下进入 Windows 文件夹方式: 终端输入 ```cd /mnt/```。
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