from typing import TypedDict

class AgentState(TypedDict):
    query: str
    next_action: str
    executed_action: list
    answers: list | str

class AgentStateInitializer:
    @staticmethod
    def custom(query):
        return AgentState(
            query=query,
            next_action="",
            executed_action=list(),
            answers=list()
        )
