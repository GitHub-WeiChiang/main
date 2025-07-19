CacheRAG
=====
Schedule
-----
* ### Day 1: 20250127
    - [x] Flowchart
* ### Day 2: 20250128
    - [x] Front-end: Web
* ### Day 3: 20250129
    - [x] Back-end: Cache
* ### Day 4: 20250130
    - [x] Back-end: RAG
* ### Day 5: 20250131
    - [x] Done: Other concluding matters
<br />

QuickStart
-----
```
ollama pull nomic-embed-text

ollama pull gemma2:9b
```
```
docker pull pgvector/pgvector:pg17

docker run --name pgvector -e POSTGRES_PASSWORD=postgres -d -p 5432:5432 pgvector/pgvector:pg17
```
```
cd Back-end

# Base on Python 3.11.7
python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt

python main.py
```
<br />

Flowchart
-----
<table style="border-collapse: collapse; border: 1px solid black;">
    <tr>
        <th>問答系統流程圖 (會實作)</th>
        <th>知識庫構建流程圖 (不實作)</th>
    </tr>
    <tr>
        <td style="padding: 5px;background-color:#fff;">
            <img src= "https://raw.githubusercontent.com/GitHub-WeiChiang/main/refs/heads/main/CacheRAG/%E5%95%8F%E7%AD%94%E7%B3%BB%E7%B5%B1%E6%B5%81%E7%A8%8B%E5%9C%96.png" />
        </td>
        <td style="padding: 5px;background-color:#fff;">
            <img src= "https://raw.githubusercontent.com/GitHub-WeiChiang/main/refs/heads/main/CacheRAG/%E7%9F%A5%E8%AD%98%E5%BA%AB%E6%A7%8B%E5%BB%BA%E6%B5%81%E7%A8%8B%E5%9C%96.png" />
        </td>
    </tr>
</table>
<br />

Screenshots
-----
<table style="border-collapse: collapse; border: 1px solid black;">
    <tr>
        <td style="padding: 5px;background-color:#fff;">
            <img src= "https://raw.githubusercontent.com/GitHub-WeiChiang/main/refs/heads/main/CacheRAG/screenshot1.png" />
        </td>
        <td style="padding: 5px;background-color:#fff;">
            <img src= "https://raw.githubusercontent.com/GitHub-WeiChiang/main/refs/heads/main/CacheRAG/screenshot2.png" />
        </td>
    </tr>
    <tr>
        <td style="padding: 5px;background-color:#fff;">
            <img src= "https://raw.githubusercontent.com/GitHub-WeiChiang/main/refs/heads/main/CacheRAG/screenshot3.png" />
        </td>
        <td style="padding: 5px;background-color:#fff;">
            <img src= "https://raw.githubusercontent.com/GitHub-WeiChiang/main/refs/heads/main/CacheRAG/screenshot4.png" />
        </td>
    </tr>
    <tr>
        <td style="padding: 5px;background-color:#fff;">
            <img src= "https://raw.githubusercontent.com/GitHub-WeiChiang/main/refs/heads/main/CacheRAG/screenshot5.png" />
        </td>
        <td style="padding: 5px;background-color:#fff;">
            <img src= "https://raw.githubusercontent.com/GitHub-WeiChiang/main/refs/heads/main/CacheRAG/screenshot6.png" />
        </td>
    </tr>
</table>
<br />
