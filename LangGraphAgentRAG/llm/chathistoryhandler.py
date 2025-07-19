from langchain.schema import HumanMessage
from langchain.schema import AIMessage
from langchain.schema import SystemMessage

class ChatHistoryHandler:
    @staticmethod
    def generate_message(chat_histories, question=None):
        messages = list()

        messages.append(SystemMessage(content="如果需要呈現圖片或表格，請以 Markdown 格式回傳。"))

        if chat_histories is None:
            return messages

        for chat_history in chat_histories:
            messages.append(
                HumanMessage(content=chat_history["content"])
                if chat_history["role"] == "user" else
                AIMessage(content=chat_history["content"])
            )

        if question is not None:
            messages.append(HumanMessage(content=question))

        return messages
