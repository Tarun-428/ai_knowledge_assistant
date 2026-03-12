from app.services.redis_client import redis_client


def add_message(conversation_id, role, content,ttl_seconds=300):
    key = f"chat:{conversation_id}"
    redis_client.rpush(
        key,
        f"{role}:{content}"
    )
    redis_client.expire(key, ttl_seconds)



def get_history(conversation_id):

    history = redis_client.lrange(
        f"chat:{conversation_id}",
        0,
        -1
    )


    return history