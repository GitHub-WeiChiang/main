from langchain_ollama import OllamaLLM
from langchain.agents import initialize_agent, AgentType

from config import config
from tool.commontool import CommonTool
from tool.patool import PATool
from tool.nmstool import NMSTool

class Agent:
    def __init__(self):
        self.__OLLAMA_LLM = OllamaLLM(
            model=config.LLM_MODEL,
            temperature=config.LOW_TEMPERATURE,
            base_url=config.OLLAMA_BASE_URL
        )

        self.__DEFAULT_TOOLS = [
            *CommonTool.get_tools(),
            *PATool.get_tools(),
            *NMSTool.get_tools(),
        ]

    def gen_single_tool_agent(self, tool):
        agent_executor =  initialize_agent(
            tools=[tool],
            llm=self.__OLLAMA_LLM,
            agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
            verbose=True
        )

        agent_executor.max_iterations = config.AGENT_MAX_ITER
        agent_executor.early_stopping_method = config.AGENT_STOP_METHOD

        return agent_executor

    def gen_multi_tool_agent(self, extra_tool=None):
        tools = self.get_default_tools() if extra_tool is None else self.get_default_tools() + extra_tool.get_tools()

        agent_executor =  initialize_agent(
            tools=tools,
            llm=self.__OLLAMA_LLM,
            agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
            verbose=True
        )

        agent_executor.max_iterations = config.AGENT_MAX_ITER
        agent_executor.early_stopping_method = config.AGENT_STOP_METHOD

        return agent_executor

    def get_default_tools(self):
        return self.__DEFAULT_TOOLS

agent = Agent()
