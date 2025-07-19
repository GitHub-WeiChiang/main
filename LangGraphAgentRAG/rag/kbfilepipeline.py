import os
import datetime
import psycopg2

from langchain.text_splitter import RecursiveCharacterTextSplitter
from colorama import Fore, Style

from config import config
from rag.imagehandler import ImageHandler
from rag.docxhandler import DocxHandler
from rag.pgvectorhandler import pg_vector_handler

class KBFilePipeline:
    def __init__(self):
        self.__categories = list()
        self.__documents = dict()
        self.__contents = dict()

        self.__conn = psycopg2.connect(config.PGVECTOR_CONN)

    def __get_categories(self):
        if not os.path.exists(config.DOCS_ROOT):
            print("❌ [KBFilePipeline] " + Fore.YELLOW + f"資料夾 '{config.DOCS_ROOT}' 不存在！" + Style.RESET_ALL)
            raise FileNotFoundError()

        self.__categories = [
            folder for folder in os.listdir(config.DOCS_ROOT) if os.path.isdir(os.path.join(config.DOCS_ROOT, folder))
        ]

        print("✅ [KBFilePipeline] " + Fore.BLUE + "獲取知識庫主題列表。" + Style.RESET_ALL)

    def __get_documents(self):
        for category in self.__categories:
            category_path = os.path.join(config.DOCS_ROOT, category)

            self.__documents[category] = [
                file for file in os.listdir(str(category_path)) if file.endswith(".docx")
            ]

        print("✅ [KBFilePipeline] " + Fore.BLUE + "獲取知識庫文件列表。" + Style.RESET_ALL)

    def __get_contents(self):
        has_documents = False

        for category, files in self.__documents.items():
            category_path = os.path.join(config.DOCS_ROOT, category)

            self.__contents[category] = dict()

            for file in files:
                file_path = os.path.join(str(category_path), file)
                mtime = datetime.datetime.fromtimestamp(os.path.getmtime(file_path)).isoformat()

                if pg_vector_handler.has_file(category, file):
                    if mtime == pg_vector_handler.get_mtime(category, file):
                        print("🔹 [KBFilePipeline] " + Fore.BLUE + f"文件 '{file}' 已存在且未修改，跳過存入。" + Style.RESET_ALL)
                        continue

                    pg_vector_handler.del_file(category, file)
                    ImageHandler.remove_img_folder(category, file)

                    print("⚠️ [KBFilePipeline] " + Fore.BLUE + f"文件 '{file}' 已存在但有更新，將刪除現有版本，稍後存入更新版。" + Style.RESET_ALL)

                ImageHandler.create_img_folder(category, file)

                documents = DocxHandler.load_docx_file(file_path)

                self.__contents[category][file] = {
                    "documents": documents,
                    "mtime": mtime
                }

                has_documents = True

        if has_documents:
            print("✅ [KBFilePipeline] " + Fore.BLUE + "獲取知識庫文件內容。" + Style.RESET_ALL)

    def __store_contents(self):
        for category, files in self.__contents.items():
            category_params = config.RAG_PARAMS.get(category, config.RAG_PARAMS["DEFAULT"])

            text_splitter = RecursiveCharacterTextSplitter(
                chunk_size=category_params["CHUNK_SIZE"],
                chunk_overlap=category_params["CHUNK_OVERLAP"]
            )

            for file, file_info in files.items():
                print("📂 [KBFilePipeline] " + Fore.WHITE + f"正在處理文件 '{file}'" + Style.RESET_ALL)

                split_docs = text_splitter.split_documents(file_info["documents"])

                for index, chunk in enumerate(split_docs):
                    chunk.metadata = {
                        "category": category,
                        "file": file,
                        "index": index,
                        "mtime": file_info["mtime"]
                    }

                config.PG_VECTOR.add_documents(split_docs)

                print("✅ [KBFilePipeline] " + Fore.BLUE + f"文件 '{file}' 已成功存入向量資料庫，共 '{len(split_docs)}' 個 chunk。" + Style.RESET_ALL)

    def __cleanup_deleted_documents(self):
        stored_files = pg_vector_handler.get_filenames()
        current_files = set()

        for category, files in self.__documents.items():
            for file in files:
                current_files.add(category + config.SPLIT_TAG + file)

        deleted_files = stored_files - current_files

        if not deleted_files:
            print("🔹 [KBFilePipeline] " + Fore.BLUE + "沒有需要刪除的舊文件，所有內容已與本地端同步。" + Style.RESET_ALL)
            return

        for file in deleted_files:
            cat, fil = file.split(config.SPLIT_TAG)
            pg_vector_handler.del_file(cat, fil)

        print("✅ [KBFilePipeline] " + Fore.BLUE + f"已清除 '{len(deleted_files)}' 個已刪除文件的向量數據。" + Style.RESET_ALL)

    def __close_conn(self):
        self.__conn.close()

    def run(self):
        self.__get_categories()
        self.__get_documents()
        self.__get_contents()
        self.__store_contents()
        self.__cleanup_deleted_documents()
        self.__close_conn()

        print("🥳 [KBFilePipeline] " + Fore.GREEN + "知識庫載入流程執行完畢。" + Style.RESET_ALL)

    def get_categories(self):
        return self.__categories

kb_file_pipeline = KBFilePipeline()
