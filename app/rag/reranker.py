from sentence_transformers import CrossEncoder


class Reranker:

    def __init__(self):
        self.model = CrossEncoder("BAAI/bge-reranker-base")

    def rerank(self, query: str, docs: list, top_k: int = 4):

        pairs = [[query, doc.page_content] for doc in docs]

        scores = self.model.predict(pairs)

        scored_docs = list(zip(docs, scores))

        scored_docs.sort(key=lambda x: x[1], reverse=True)

        return [doc for doc, _ in scored_docs[:top_k]]


reranker = Reranker()