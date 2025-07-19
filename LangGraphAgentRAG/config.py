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

config = Config()
