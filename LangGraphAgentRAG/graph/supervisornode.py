from graph.agentstate import AgentState
from langchain_ollama import OllamaLLM
from langchain.prompts import ChatPromptTemplate
from langchain.prompts import SystemMessagePromptTemplate
from langchain.prompts import HumanMessagePromptTemplate
from langchain.prompts import AIMessagePromptTemplate

from config import config

class SupervisorNode:
    __OLLAMA_LLM = OllamaLLM(
        model=config.LLM_MODEL,
        temperature=config.LOW_TEMPERATURE,
        base_url=config.OLLAMA_BASE_URL
    )

    __CHAT_REC_PROMPT_TPL = ChatPromptTemplate.from_messages([
        SystemMessagePromptTemplate.from_template(
            """
            你是一個專業的工具推薦助理，
            負責依用戶的原始問題和已經答覆的內容，
            分析是否需要使用額外的工具來解決問題。

            職責：
            1. 檢視用戶的原始問題和已經答覆的內容。
            2. 評估是否需要額外的工具來解決問題。
            3. 若不需要使用工具或工具清單中沒有合適的工具，請回傳字串 FINISH。
            4. 若需要使用工具，請從工具清單中挑選合適的工具，並回傳該工具的名稱。
            5. 僅在必要時才推薦工具，且一次只能推薦一個工具。
            6. 一個工具只能用一次，不可以推薦已經使用過的工具。
            """
        ),
        SystemMessagePromptTemplate.from_template(
            """
            工具清單：
            get_current_time：這個工具用於查詢即時的日期與時間資訊，適用於用戶想了解當前的日期與時間之場景。
            get_weather：這個工具用於查詢特定月分與日期的天氣資訊，適用於用戶想了解特定的月分與日期天氣之場景。
            is_employee_present：這個工具用於查詢一位指定員工即時到勤資訊，適用於用戶想了解一位指定員工的即時到勤資訊之場景。
            open_port：這個工具用於開啟指定網路設備交換器的特定埠號，適用於用戶想開啟指定網路設備交換器特定埠號之場景。
            close_port：這個工具用於關閉指定網路設備交換器的特定埠號，適用於用戶想關閉指定網路設備交換器特定埠號之場景。
            set_description：這個工具用於添加指定網路設備交換器的特定埠號功能描述，適用於用戶想添加指定網路設備交換器特定埠號功能描述之場景。
            run_basic_retriever：這個工具會透過向量檢索的方式查詢指定知識庫的相關內容，並將匹配到的資訊與用戶問題傳送給此工具內部的 LLM 進行答覆，適用於當用戶提出特定領域知識的提問。

            備註：
            當你認為沒有合適的工具時請嘗試使用 run_basic_retriever 這個工具。

            回傳範例：
            get_current_time
            get_weather
            is_employee_present
            open_port
            close_port
            set_description
            run_basic_retriever
            FINISH
            """
        ),
        HumanMessagePromptTemplate.from_template("用戶原始問題：\n{query}\n\n已經答覆內容：\n{answers}"),
        AIMessagePromptTemplate.from_template("已經使用過的工具：{executed_action}")
    ])

    __CHAT_COMBINE_PROMPT_TPL = ChatPromptTemplate.from_messages([
        SystemMessagePromptTemplate.from_template(
            """
            你是一個專業的資訊彙整助理，若有需要則執行下方作業：
            1. 負責將所提供的資訊進行彙整。
            2. 請以所提供的資訊為基礎答覆。
            3. 無須提及你將資訊彙整的事情。
            """
        ),
        HumanMessagePromptTemplate.from_template("用戶原始問題：\n{query}\n\n已經答覆內容：\n{answers}"),
    ])

    @classmethod
    def supervisor(cls, agent_state: AgentState) -> AgentState:
        answers = "\n".join(
            agent_state["answers"]
        ) if agent_state["answers"] else "尚未答覆任何內容。"

        executed_action = ", ".join(
            agent_state["executed_action"]
        ) if agent_state["executed_action"] else "尚未使用任何工具。"

        chain = cls.__CHAT_REC_PROMPT_TPL | cls.__OLLAMA_LLM

        next_action = chain.invoke({
            "query": agent_state["query"],
            "answers": answers,
            "executed_action": executed_action
        })

        agent_state["next_action"] = next_action.strip()

        if agent_state["next_action"] == "FINISH":
            _chain = cls.__CHAT_COMBINE_PROMPT_TPL | cls.__OLLAMA_LLM

            agent_state["answers"] = _chain.invoke({
                "query": agent_state["query"],
                "answers": agent_state["answers"]
            })

        return agent_state
