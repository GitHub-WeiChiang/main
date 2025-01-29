from fastapi import APIRouter
from pydantic import BaseModel
import numpy as np
from faiss_index import faiss_handler
from llm import llm_handler
from config import config

router = APIRouter()

class QuestionRequest(BaseModel):
    question: str
    top_k: int = 5
    temperature: float = 0.7

@router.post("/ask")
async def ask_question(request: QuestionRequest):
    """處理前端的問答請求，透過 FAISS 檢索匹配最相關的回應"""

    # 產生查詢向量
    question_vector = np.array([llm_handler.embed_text(request.question)])

    # 同時搜尋固定回覆 & 彈性回覆
    fixed_distance, fixed_index = faiss_handler.search_fixed(question_vector)
    elastic_distance, elastic_index = faiss_handler.search_elastic(question_vector)

    # 選擇最小距離的匹配結果
    if fixed_distance is not None and elastic_distance is not None:
        if fixed_distance < elastic_distance and fixed_distance < faiss_handler.threshold:
            matched_key = faiss_handler.fixed_keys[fixed_index]
            print(f"[API] 固定回覆匹配: {matched_key}, 距離: {fixed_distance}")
            return {"answer": config["固定回覆"][matched_key], "source": "Cache"}
        elif elastic_distance < faiss_handler.threshold:
            matched_key = faiss_handler.elastic_keys[elastic_index]
            prompt = config["彈性回覆"][matched_key]  # 取得 `value` 作為 LLM 提示詞
            print(f"[API] 彈性回覆匹配: {matched_key}, 距離: {elastic_distance}")
            response = llm_handler.generate_response(f"{prompt}\n\n{request.question}", request.temperature)  # 把 `prompt` + `問題` 一起交給 LLM
            return {"answer": response, "source": "CAG"}

    # 如果只有一個匹配到，就返回該匹配
    if fixed_distance is not None and fixed_distance < faiss_handler.threshold:
        matched_key = faiss_handler.fixed_keys[fixed_index]
        print(f"[API] 固定回覆匹配: {matched_key}, 距離: {fixed_distance}")
        return {"answer": config["固定回覆"][matched_key], "source": "Cache"}

    if elastic_distance is not None and elastic_distance < faiss_handler.threshold:
        matched_key = faiss_handler.elastic_keys[elastic_index]
        prompt = config["彈性回覆"][matched_key]  # 取得 `value` 作為 LLM 提示詞
        print(f"[API] 彈性回覆匹配: {matched_key}, 距離: {elastic_distance}")
        response = llm_handler.generate_response(f"{prompt}\n\n{request.question}", request.temperature)  # 把 `prompt` + `問題` 一起交給 LLM
        return {"answer": response, "source": "CAG"}

    # 比對指定操作 (開啟/關閉系統)
    command_distance, command_index = faiss_handler.search_command(question_vector)
    if command_distance is not None and command_distance < faiss_handler.threshold:
        matched_key = faiss_handler.command_keys[command_index]
        print(f"[API] 指定操作匹配: {matched_key}, 距離: {command_distance}")
        return {"answer": config["指定操作"][matched_key], "source": "Subsystem"}

    # 若無匹配則回傳未知
    return {"answer": "尚無法回答此問題，請稍後再試。", "source": "Unknown"}
