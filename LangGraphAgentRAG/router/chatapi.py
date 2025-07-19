from fastapi import APIRouter
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from rag.retriever import Retriever
from llm.llmhandler import llm_handler
from tool.agent import agent
from graph.agentworkflow import AgentWorkflow
from graph.agentstate import AgentStateInitializer
from rag.kbfilepipeline import kb_file_pipeline
from tool.ragtool import RAGTool
from llm.chathistoryhandler import ChatHistoryHandler

router = APIRouter()

"""
{
  "category": "測試專用",
  "question": "給我全彩公雞圖",
  "chat_histories": []
}

{
  "category": "測試專用",
  "question": "給我所有公雞的參數表格",
  "chat_histories": []
}

{
  "category": "",
  "question": "請問我是誰",
  "chat_histories": [
	{
		"role": "user",
		"content": "您好，我是野原新之助。"
	},
	{
		"role": "bot",
		"content": "您好，野原新之助先生！\n\n很高興能為您服務。"
	},
	{
		"role": "user",
		"content": "您好，我今年五歲。"
	},
	{
		"role": "bot",
		"content": "您好！很高興認識您。您今年五歲，真是個可愛的小朋友！"
	}
  ]
}

{
  "category": "",
  "question": "請問我幾歲",
  "chat_histories": [
	{
		"role": "user",
		"content": "您好，我是野原新之助。"
	},
	{
		"role": "bot",
		"content": "您好，野原新之助先生！\n\n很高興能為您服務。"
	},
	{
		"role": "user",
		"content": "您好，我今年五歲。"
	},
	{
		"role": "bot",
		"content": "您好！很高興認識您。您今年五歲，真是個可愛的小朋友！"
	}
  ]
}
"""

class Request(BaseModel):
    category: str = ""
    question: str = ""
    chat_histories: list = list()

@router.get("/categories")
def categories():
    print(f"🤖 [ChatAPI][/categories] 收到請求")

    return JSONResponse(content=kb_file_pipeline.get_categories(), status_code=200)

@router.post("/talk/rag")
def talk_rag(request: Request):
    print(f"🤖 [ChatAPI][/talk/rag] 收到請求 {request}")

    retrieved_results = Retriever.search(request.category, request.question)

    answer = llm_handler.generate_response(retrieved_results, request.question, request.chat_histories)

    return JSONResponse(content={
        "answer": answer,
        "retrieved_results": retrieved_results
    }, status_code=200)

@router.post("/talk/agent")
def talk_agent(request: Request):
    print(f"🤖 [ChatAPI][/talk/agent] 收到請求 {request}")

    rag_tool = RAGTool(request.category)

    messages = ChatHistoryHandler.generate_message(request.chat_histories, request.question)

    answer = agent.gen_multi_tool_agent(rag_tool).invoke(messages)["output"]

    return JSONResponse(content={
        "answer": answer,
        "retrieval_records": rag_tool.get_retrieval_records()
    }, status_code=200)

@router.post("/talk/graph")
def talk_graph(request: Request):
    print(f"🤖 [ChatAPI][/talk/graph] 收到請求 {request}")

    rag_tool = RAGTool(request.category)

    agent_state = AgentStateInitializer.custom(request.question)
    agent_state = AgentWorkflow(
        chat_histories=request.chat_histories, extra_tool=rag_tool
    ).get_workflow().invoke(agent_state)

    return JSONResponse(content={
        "answer": agent_state["answers"],
        "executed_action": agent_state["executed_action"],
        "retrieval_records": rag_tool.get_retrieval_records()
    }, status_code=200)
