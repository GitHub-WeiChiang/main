from config import config

class Retriever:
    @staticmethod
    def search(category, context):
        if not category:
            return list()

        category_params = config.RAG_PARAMS.get(category, config.RAG_PARAMS["DEFAULT"])

        retriever = config.PG_VECTOR.as_retriever(
            search_type="similarity_score_threshold",
            search_kwargs={
                "k": category_params["TOP_K"],
                "score_threshold": category_params["SCORE_THRESHOLD"],
                "filter": {"category": category}}
        )
        documents = retriever.invoke(context)

        results = list()

        for document in documents:
            results.append({
                "category": document.metadata.get("category"),
                "file": document.metadata.get("file"),
                "index": document.metadata.get("index"),
                "mtime": document.metadata.get("mtime"),
                "content": document.page_content
            })

        return results
