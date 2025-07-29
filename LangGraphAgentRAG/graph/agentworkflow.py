import warnings
import functools

from langgraph.graph import StateGraph, END

from tool.agent import agent
from graph.agentstate import AgentState
from graph.supervisornode import SupervisorNode
from llm.chathistoryhandler import ChatHistoryHandler

warnings.filterwarnings("ignore", category=DeprecationWarning)

class AgentWorkflow:
    def __init__(self, chat_histories=None, extra_tool=None):
        self.__WORKFLOW = StateGraph(AgentState)

        self.__WORKFLOW.add_node("supervisor", SupervisorNode.supervisor)
        self.__WORKFLOW.set_entry_point("supervisor")

        self.__CONDITIONAL_MAP = dict()

        tools = agent.get_default_tools() if extra_tool is None else agent.get_default_tools() + extra_tool.get_tools()

        for tool in tools:
            node = functools.partial(
                AgentWorkflow.__generate_agent_node,
                agent_instance=agent.gen_custom_agent(tool),
                agent_name=tool.name,
                chat_histories=chat_histories
            )

            self.__WORKFLOW.add_node(tool.name, node)
            self.__WORKFLOW.add_edge(tool.name, "supervisor")
            self.__CONDITIONAL_MAP[tool.name] = tool.name

        self.__CONDITIONAL_MAP["FINISH"] = END

        self.__WORKFLOW.add_conditional_edges(
            "supervisor",
            lambda agent_state: agent_state["next_action"],
            self.__CONDITIONAL_MAP
        )

    @staticmethod
    def __generate_agent_node(agent_state: AgentState, agent_instance, agent_name, chat_histories):
        messages = ChatHistoryHandler.generate_message(chat_histories, agent_state["query"])

        answer = agent_instance.invoke(messages)["output"]

        agent_state["executed_action"].append(agent_name)
        agent_state["answers"].append(answer)

        return agent_state

    def get_workflow(self):
        return self.__WORKFLOW.compile()
