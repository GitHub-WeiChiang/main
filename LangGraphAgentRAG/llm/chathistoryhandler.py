from langchain.schema import HumanMessage
from langchain.schema import AIMessage
from langchain.schema import SystemMessage

from config import config

class ChatHistoryHandler:
    @staticmethod
    def generate_message(chat_histories, question=None):
        messages = list()

        messages.append(SystemMessage(content="請儘量呈現圖片與表格。"))
        messages.append(SystemMessage(content="請以 Markdown 格式字串呈現圖片與表格。"))
        messages.append(SystemMessage(content="請勿修改 Markdown 圖片格式的網址。"))
        messages.append(SystemMessage(content="請完整且詳盡的答覆。"))

        if chat_histories is None:
            return messages

        chat_histories = chat_histories[-config.MAX_CHAT_HISTORY_MESSAGES:]

        for chat_history in chat_histories:
            messages.append(
                HumanMessage(content=chat_history["content"])
                if chat_history["role"] == "user" else
                AIMessage(content=chat_history["content"])
            )

        if question is not None:
            messages.append(HumanMessage(content=question))

        return messages
