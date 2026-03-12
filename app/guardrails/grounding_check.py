from langchain_core.documents import Document


def check_grounding(answer: str, docs: list[Document]) -> bool:
    """
    Verify that the answer is grounded in retrieved documents.
    """

    context_text = " ".join([doc.page_content for doc in docs]).lower()

    answer_words = answer.lower().split()

    match_count = sum(1 for word in answer_words if word in context_text)

    grounding_score = match_count / max(len(answer_words), 1)
    print("grounding checking  done")

    return grounding_score > 0.2