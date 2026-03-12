from collections import defaultdict
from typing import List


class ConversationMemory:
    """
    Simple in-memory conversation store
    """

    def __init__(self):
        self.store = defaultdict(list)

    def add_message(self, conversation_id: str, role: str, content: str):
        self.store[conversation_id].append(
            {"role": role, "content": content}
        )

    def get_history(self, conversation_id: str) -> List[dict]:
        return self.store[conversation_id]

    def clear(self, conversation_id: str):
        self.store[conversation_id] = []


memory_store = ConversationMemory()