from config import config

class Retriever:
    @staticmethod
    def search(category, context):
        if not category:
            return list()

        category_params = config.RAG_PARAMS.get(category, config.RAG_PARAMS["DEFAULT"])

        documents = config.PG_VECTOR.similarity_search_with_score(
            context, k=category_params["TOP_K"], filter={"category": category}
        )

        results = list()

        for document, score in documents:
            results.append({
                "category": document.metadata.get("category"),
                "file": document.metadata.get("file"),
                "index": document.metadata.get("index"),
                "mtime": document.metadata.get("mtime"),
                "content": document.page_content,
                "similarity": round(1 - score, 2)
            })

        return results
