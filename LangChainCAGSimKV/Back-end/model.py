from langchain_ollama import OllamaLLM
from langchain.schema import AIMessage, HumanMessage
from config import OLLAMA_MODEL, MAX_HISTORY_SIZE

# 知識庫（固定置頂，不會變動）
preloaded_knowledge = """
已知知識如下，僅在有需要時使用：
1. 生死格鬥沙灘排球維納斯璀璨假期：是Team Ninja開發、光榮特庫摩發行生死格鬥系列的沉浸式戀愛冒險遊戲。本作發生在維納斯群島，預計2025年3月6日發行。
2. 遊戲玩法：以章節的形式進行。伴隨著故事的推進，身為新手島主的玩家需要完成工作，同時和女孩加深關係。
3. 登場角色：海咲、穗香、環、菲歐娜、七海、伊莉絲。
"""

# 初始化 Ollama
llm = OllamaLLM(model=OLLAMA_MODEL)

# 快取對話歷史（最多 10 次對話 = 20 條訊息）
chat_history = []

def cag_generate(user_input: str) -> str:
    """模擬 CAG 快取機制，支援多輪對話但知識庫固定"""
    
    # 只保留最近 10 次對話（20 條訊息）
    recent_history = chat_history[-(MAX_HISTORY_SIZE * 2):]

    # 建構 Prompt（知識庫 + 最近 10 次對話）
    messages = [AIMessage(content=preloaded_knowledge)] + recent_history + [HumanMessage(content=user_input)]

    # 呼叫 LLM
    response = llm.invoke(messages)

    # 更新對話紀錄
    chat_history.append(HumanMessage(content=user_input))
    chat_history.append(AIMessage(content=response))

    # 確保只保留最近 10 次對話
    if len(chat_history) > MAX_HISTORY_SIZE * 2:
        chat_history.pop(0)
        chat_history.pop(0)

    return response
