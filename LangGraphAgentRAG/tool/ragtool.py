from langchain.tools import tool

from rag.retriever import Retriever
from llm.llmhandler import llm_handler

class RAGTool:
    def __init__(self, category):
        self.__category = category
        self.__retrieval_records = list()

    def __get_func(self):
        def run_basic_retriever(query: str = "") -> str:
            """
            這個工具會透過向量檢索的方式查詢指定知識庫的相關內容，
            並將匹配到的資訊與用戶問題傳送給此工具內部的 LLM 進行答覆，
            適用於當用戶提出特定領域知識的提問。

            :param query: 用戶問題。
            :type query: str

            :return: LLM 針對用戶問題並參考匹配到的資訊所生成的回覆。
            :rtype: str

            :適用場景:
                - 用戶針對特定領域知識的提問。

            :輸入範例:
                - 攝影機沒有畫面如何排查
                - 空調故障怎麼辦
                - 有哪些行車安全規範
            """

            retrieved_results = Retriever.search(self.__category, query)
            answer = llm_handler.generate_response(retrieved_results, query)

            self.__retrieval_records.append({
                "query": query,
                "retrieved_results": retrieved_results
            })

            return answer

        return run_basic_retriever

    def get_retrieval_records(self):
        return self.__retrieval_records

    def get_tools(self):
        return [
            tool(self.__get_func()),
        ]
