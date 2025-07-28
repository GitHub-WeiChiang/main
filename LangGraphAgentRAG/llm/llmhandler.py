import copy

from langchain_ollama import OllamaLLM
from langchain.prompts import ChatPromptTemplate
from langchain.prompts import SystemMessagePromptTemplate
from langchain.prompts import HumanMessagePromptTemplate
from langchain.prompts import AIMessagePromptTemplate

from config import config
from llm.chathistoryhandler import ChatHistoryHandler

class LLMHandler:
    def __init__(self):
        self.__OLLAMA_LLM = OllamaLLM(
            model=config.LLM_MODEL,
            temperature=config.DEFAULT_TEMPERATURE,
            base_url=config.OLLAMA_BASE_URL
        )

        self.__MESSAGES = [
            SystemMessagePromptTemplate.from_template("您是一位智能助理，協助用戶解決所遇到的問題。"),
            HumanMessagePromptTemplate.from_template("已知資訊：\n{data}\n\n\n用戶問題：\n{question}"),
            AIMessagePromptTemplate.from_template("若有需要，請根據已知資訊提供準確的答覆；若無法回答，請誠實告知用戶。"),
        ]

    def generate_response(self, retrieve_chunks, question, chat_histories=None):
        messages = copy.deepcopy(self.__MESSAGES)

        messages[1:1] = ChatHistoryHandler.generate_message(chat_histories)

        data = "\n\n".join(chunk["content"] for chunk in retrieve_chunks) if retrieve_chunks else "尚無相關已知資訊。"

        chain = ChatPromptTemplate.from_messages(messages) | self.__OLLAMA_LLM

        return chain.invoke({"data": data, "question": question})

llm_handler = LLMHandler()
