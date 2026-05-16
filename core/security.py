from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext   
from jose import JWTError, jwt
import os 
from datetime import datetime, timedelta
from dotenv import load_dotenv
load_dotenv()

ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))
ALGOTITHM = os.getenv("ALGORITHM")
SECRET_KEY = os.getenv("SECRET_KEY")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/auth/login"
)

def hash_password(password: str) -> str:
    # Bcrypt has a 72-byte limit for passwords
    return pwd_context.hash(password[:72])

def verify_password(plain_password: str, hashed_password: str) -> bool:
    # Truncate to 72 bytes for verification as well
    return pwd_context.verify(plain_password[:72], hashed_password)


def create_token(id_user: int, token_type: str, token_duration=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)) -> str:
    expire = datetime.utcnow() + token_duration
    dict_info = {"sub": str(id_user), "type": token_type, "exp": expire}
    encoded_jwt = jwt.encode(dict_info, SECRET_KEY, ALGOTITHM)
    return encoded_jwt


def verify_token(token: str, expected_type: str) -> str:
    
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGOTITHM])

        token_type: str = payload.get("type")

        if token_type != expected_type:
            raise ValueError("Invalid token type")
        return payload
    
    except JWTError:
        raise ValueError("Invalid token")