from pydantic import BaseModel, Field, ValidationError


class UserQuery(BaseModel):
    question: str = Field(
        min_length=3,
        max_length=1000,
        description="User question"
    )


def validate_input(question: str) -> str:
    """
    Validate user input using Pydantic.
    """

    try:
        validated = UserQuery(question=question)
        print("validate input done")
        return validated.question
    except ValidationError as e:
        raise ValueError(f"Invalid input: {e}")