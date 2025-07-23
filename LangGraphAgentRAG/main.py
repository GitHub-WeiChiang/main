import uvicorn

from fastapi_offline import FastAPIOffline
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from config import config
from router import chatapi
from router import fakeapi
from rag.kbfilepipeline import kb_file_pipeline

app = FastAPIOffline(
    title="knowledge-base-agent",
    version='0.0.1',
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def index():
    return FileResponse("static/index.html")

app.include_router(chatapi.router, prefix=config.API_PREFIX)
app.include_router(fakeapi.router, prefix=config.API_PREFIX)

kb_file_pipeline.run()

if __name__ == "__main__":
    uvicorn.run(
        app=app,
        host=config.HOST,
        port=config.PORT
    )
