from passlib.context import CryptContext

# bcrypt hashing context
pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


def hash_password(password: str) -> str:
    """
    Hash a plain password before storing in DB.
    """
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verify password during login.
    """
    return pwd_context.verify(plain_password, hashed_password)