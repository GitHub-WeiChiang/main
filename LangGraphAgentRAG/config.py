import os
import yaml

from langchain_ollama import OllamaEmbeddings
from langchain_postgres import PGVector

class Config:
    def __init__(self):
        self.HOST = "localhost"
        self.PORT = 8888

        self.API_PREFIX = "/api"
        self.IMG_PREFIX = "/static/imgs"

        self.EMBED_MODEL = "nomic-embed-text:latest"
        self.OLLAMA_BASE_URL = "http://localhost:11434/"
        self.PGVECTOR_CONN = "postgresql://postgres:postgres@localhost:5432/postgres"
        self.PG_VECTOR = PGVector(
            embeddings=OllamaEmbeddings(model=self.EMBED_MODEL, base_url=self.OLLAMA_BASE_URL),
            connection=self.PGVECTOR_CONN
        )

        self.DOCS_ROOT = "./doc"
        self.IMGS_ROOT_PATH = "/static/imgs"
        self.IMGS_ROOT_OS = "./static/imgs"

        self.LLM_MODEL = "gemma3:12b"

        self.LOW_TEMPERATURE = 0
        self.DEFAULT_TEMPERATURE = 0.3

        self.RAG_PARAMS = dict()
        with open(os.path.join(self.DOCS_ROOT, "rag_params.yaml"), encoding="utf-8") as file:
            self.RAG_PARAMS = yaml.safe_load(file)

        self.BF_SALT = "SALT"
        self.SPLIT_TAG = "-->"

        self.CSCO_T_SW_CONN_INFO = ("xxx.xxx.xxx.xxx", 22, 'admin', 'Aa123456')

        self.REMOTE_CTRL_COMMAND_INTERVAL_TIME = 1
        self.SSH_TIMEOUT = 5

        self.MAX_CHAT_HISTORY_MESSAGES = 4

        self.AGENT_MAX_ITER = 2
        self.AGENT_STOP_METHOD = "generate"

        self.HASH_NAME_LEN = 5

config = Config()
