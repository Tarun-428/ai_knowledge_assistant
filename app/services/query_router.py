def detect_query_type(question: str):

    summary_keywords = [
        "summarize",
        "summary",
        "goal",
        "objective",
        "overview",
        "main idea"
    ]

    q = question.lower()

    for word in summary_keywords:

        if word in q:
            return "summary"

    return "rag"