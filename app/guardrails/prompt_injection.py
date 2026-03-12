import re


INJECTION_PATTERNS = [
    r"ignore previous instructions",
    r"disregard system prompt",
    r"reveal system prompt",
    r"show hidden instructions",
    r"bypass security",
]


def detect_prompt_injection(text: str) -> bool:
    """
    Detect possible prompt injection attempts.
    """

    text_lower = text.lower()

    for pattern in INJECTION_PATTERNS:
        if re.search(pattern, text_lower):
            return True
    print("prompt injection done")

    return False