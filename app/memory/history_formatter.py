import json

def format_history(messages: list) -> str:
    """
    Convert conversation messages (JSON strings or dicts) into text
    """
    formatted = []

    for msg in messages:
        # 1. If it's a JSON string from Redis, parse it into a dict
        if isinstance(msg, (str, bytes)):
            try:
                msg = json.loads(msg)
            except json.JSONDecodeError:
                # Fallback if the string isn't JSON (e.g. "user: hello")
                formatted.append(str(msg))
                continue

        # 2. Extract values from the dictionary
        role = msg.get("role", "admin")
        content = msg.get("content", "")

        formatted.append(f"{role}: {content}")

    return "\n".join(formatted)
