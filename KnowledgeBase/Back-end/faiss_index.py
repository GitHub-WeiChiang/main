import faiss
import numpy as np
from config import config
from llm import llm_handler

class FAISSHandler:
    def __init__(self):
        self.fixed_keys = list(config["固定回覆"].keys())
        self.elastic_keys = list(config["彈性回覆"].keys())
        self.command_keys = list(config["指定操作"].keys())  # 指定操作鍵值

        # 設定統一閾值，避免重複定義
        self.threshold = 1800

        # 產生嵌入向量
        self.fixed_vectors = np.vstack([llm_handler.embed_text(text) for text in self.fixed_keys]).astype(np.float32)
        self.elastic_vectors = np.vstack([llm_handler.embed_text(text) for text in self.elastic_keys]).astype(np.float32)
        self.command_vectors = np.vstack([llm_handler.embed_text(text) for text in self.command_keys]).astype(np.float32)  # 指定操作嵌入

        # 建立 FAISS 索引
        self.fixed_index = faiss.IndexFlatL2(self.fixed_vectors.shape[1])
        self.elastic_index = faiss.IndexFlatL2(self.elastic_vectors.shape[1])
        self.command_index = faiss.IndexFlatL2(self.command_vectors.shape[1])  # 指定操作索引

        self.fixed_index.add(self.fixed_vectors)
        self.elastic_index.add(self.elastic_vectors)
        self.command_index.add(self.command_vectors)  # 加入 FAISS

    def search_fixed(self, query_vector):
        """ 查找固定回覆，使用 `self.threshold` """
        D, I = self.fixed_index.search(query_vector, 1)
        print(f"[固定回覆] 查詢距離: {D[0][0]}, 閾值: {self.threshold}")
        return (D[0][0], I[0][0]) if D[0][0] < self.threshold else (None, None)

    def search_elastic(self, query_vector):
        """ 查找彈性回覆，使用 `self.threshold` """
        D, I = self.elastic_index.search(query_vector, 1)
        print(f"[彈性回覆] 查詢距離: {D[0][0]}, 閾值: {self.threshold}")
        return (D[0][0], I[0][0]) if D[0][0] < self.threshold else (None, None)

    def search_command(self, query_vector):
        """ 查找指定操作，使用 `self.threshold` """
        D, I = self.command_index.search(query_vector, 1)
        print(f"[指定操作] 查詢距離: {D[0][0]}, 閾值: {self.threshold}")
        return (D[0][0], I[0][0]) if D[0][0] < self.threshold else (None, None)

faiss_handler = FAISSHandler()
