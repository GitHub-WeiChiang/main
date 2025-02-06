import ollama

class LLMHandler:
    def __init__(self, model_name="gemma2:9b"):
        self.model_name = model_name

    def generate_response(self, prompt, temperature=0.7):
        """ 使用 LLM 生成回應，確保提供明確的系統指令 """
        messages = [
            {"role": "system", "content": "請根據以下內容回答問題：" },  # 增加系統指令，讓 LLM 產生更準確的回應
            {"role": "user", "content": prompt}
        ]
        response = ollama.chat(
            model=self.model_name,
            messages=messages,
            options={"temperature": temperature}
        )
        return response["message"]["content"]

    def embed_text(self, text):
        """ 產生文字的向量表示，用於 FAISS 相似度比對 """
        embedding_result = ollama.embeddings(model=self.model_name, prompt=text)
        return embedding_result["embedding"]

llm_handler = LLMHandler()
