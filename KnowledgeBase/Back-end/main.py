from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from api import router

app = FastAPI()

# 設定 CORS，允許前端請求
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 允許所有來源（前端）訪問
    allow_credentials=True,
    allow_methods=["*"],   # 允許所有 HTTP 方法（GET, POST, OPTIONS 等）
    allow_headers=["*"],   # 允許所有 Headers
)

# 載入 API 路由
app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
