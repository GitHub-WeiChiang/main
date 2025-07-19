LangChainSimulationCAG
=====
QuickStart
-----
```
ollama pull gemma2:9b
```
```
cd Back-end

# Base on Python 3.11.7
python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt

uvicorn main:app --reload
```
<br />

Flowchart
-----
<table style="border-collapse: collapse; border: 1px solid black;">
    <tr>
        <th>RAG vs. CAG</th>
    </tr>
    <tr>
        <td style="padding: 5px;background-color:#fff;">
            <img src= "https://raw.githubusercontent.com/GitHub-WeiChiang/main/refs/heads/main/LangChainSimulationCAG/RAGvsCAG_CacheAugmentedGeneration.jpg" />
        </td>
    </tr>
</table>
<br />

Reference
=====
* ### Don't Do RAG: When Cache-Augmented Generation is All You Need for Knowledge Tasks
<br />
