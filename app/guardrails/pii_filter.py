import re


EMAIL_PATTERN = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
PHONE_PATTERN = r"\b\d{10}\b"


def filter_pii(text: str) -> str:
    """
    Mask PII data in responses.
    """

    text = re.sub(EMAIL_PATTERN, "[EMAIL REDACTED]", text)

    text = re.sub(PHONE_PATTERN, "[PHONE REDACTED]", text)
    print("piii filteringg done")
    return text