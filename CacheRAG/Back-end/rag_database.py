import os
import glob
import datetime
import psycopg2
from langchain_community.document_loaders import Docx2txtLoader  # 讀取 Word 文件
from langchain.text_splitter import RecursiveCharacterTextSplitter  # 文本切分
from langchain.embeddings import OllamaEmbeddings  # 產生嵌入向量
from langchain.vectorstores import PGVector  # 連接 pgvector

# 設定 pgvector 連線資訊
PGVECTOR_DB_URL = "postgresql://postgres:postgres@localhost:5432/postgres"

# 設定 Word 文件存放的資料夾
DOCS_DIR = "doc/"

class RAGDatabase:
    def __init__(self):
        self.embeddings = OllamaEmbeddings(model="nomic-embed-text:latest")  # 產生向量
        
        # 初始化 PGVector，確保資料表存在
        self.vector_store = PGVector(embedding_function=self.embeddings, connection_string=PGVECTOR_DB_URL)
        
        # 啟動時自動處理 Word 文件
        self.load_documents_from_directory()

    def load_documents_from_directory(self):
        """ 自動讀取 doc/ 內的所有 Word 文件，向量化並存入 pgvector """
        word_files = glob.glob(os.path.join(DOCS_DIR, "*.docx"))  # 獲取 doc/ 內所有 Word 文件

        if not word_files:
            print("⚠️ [RAG] 沒有找到 Word 文件，請確認 doc/ 內是否有可處理的檔案。")
            return

        for file_path in word_files:
            self.load_and_store_document(file_path)

    def load_and_store_document(self, file_path):
        """ 讀取單個 Word 文件並存入向量資料庫 """
        doc_name = os.path.basename(file_path)  # 取得文件名稱
        last_modified_time = os.path.getmtime(file_path)  # 取得檔案最後修改時間
        last_modified_str = datetime.datetime.fromtimestamp(last_modified_time).isoformat()

        print(f"📂 [RAG] 正在處理文件: {doc_name}")

        # 讀取文件
        loader = Docx2txtLoader(file_path)
        documents = loader.load()

        # 分割文本為 chunk
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
        split_docs = text_splitter.split_documents(documents)

        # **確保每個 chunk 都有 metadata**
        for chunk in split_docs:
            chunk.metadata = {"source": doc_name, "last_modified": last_modified_str}  # 存入修改時間

        # **檢查向量資料庫是否已經有相同的文件**
        if self.document_exists(doc_name, last_modified_str):
            print(f"✅ [RAG] {doc_name} 已存在於向量資料庫，且修改時間未變更，跳過存入。")
            return

        # 存入向量資料庫
        self.vector_store.add_documents(split_docs)
        print(f"✅ [RAG] {doc_name} 已成功存入向量資料庫，共 {len(split_docs)} 個 chunk。")

    def document_exists(self, doc_name, last_modified_str):
        """ 使用 SQL 查詢 pgvector 資料庫中的 metadata 來判斷是否有相同的檔案名稱與修改時間 """
        try:
            conn = psycopg2.connect(PGVECTOR_DB_URL)
            cursor = conn.cursor()
            
            query = """
            SELECT cmetadata->>'last_modified'
            FROM langchain_pg_embedding
            WHERE cmetadata->>'source' = %s
            LIMIT 1;
            """
            cursor.execute(query, (doc_name,))
            result = cursor.fetchone()
            
            cursor.close()
            conn.close()

            if result:
                existing_time = result[0]
                if existing_time == last_modified_str:
                    return True  # 若修改時間相同，視為已存在
        except Exception as e:
            print(f"❌ [RAG] 查詢向量資料庫時發生錯誤: {e}")

        return False

    def search_rag(self, query_text, top_k=3):
        """ 在 pgvector 資料庫中搜尋最相關的 chunk，返回多個匹配結果 """
        retriever = self.vector_store.as_retriever(search_kwargs={"k": top_k})
        docs = retriever.get_relevant_documents(query_text)

        if docs:
            doc_names = [doc.metadata.get("source", "未知文件") for doc in docs]  # 取得所有文件名稱
            doc_chunks = [doc.page_content for doc in docs]  # 取得所有 chunk 內容
            return doc_names, doc_chunks
        return [], []

# 初始化 RAG 模組，確保 FastAPI 啟動時加載文件
rag_handler = RAGDatabase()
