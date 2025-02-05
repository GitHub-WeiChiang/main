from fastapi import FastAPI
from model import cag_generate
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI()

# 提供前端靜態文件
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def serve_index():
    return FileResponse("static/index.html")

# 設定 CORS，允許前端請求
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 允許所有來源（前端）訪問
    allow_credentials=True,
    allow_methods=["*"],   # 允許所有 HTTP 方法（GET, POST, OPTIONS 等）
    allow_headers=["*"],   # 允許所有 Headers
)

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
async def chat(request: ChatRequest):
    response = cag_generate(request.message)
    return {"response": response}
