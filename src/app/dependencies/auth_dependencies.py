from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from typing import Annotated
from passlib.context import CryptContext

from ..models.auth.user_model import User

SECRET_KEY = "fastapi_sqlmodel"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_schema = OAuth2PasswordBearer(tokenUrl="token")

Oauth2SchemaDep = Annotated[str, Depends(oauth2_schema)]

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password):
    return pwd_context.hash(password)


def verify_password(plain_password, hashed_password):
    print("@@@@@@@ plain_password :", plain_password)
    print("@@@@@@@ hashed_password :", hashed_password)
    
    return pwd_context.verify(plain_password, hashed_password)


def fake_decode_token(token):
    print("token inside fake decode :", token)

    return User(
        username=token + "fakedecoded", email="john@example.com", full_name="John Doe"
    )


async def get_current_user(token: Oauth2SchemaDep):
    user = fake_decode_token(token)
    return user


GetCurrentUserDep = Annotated[User, Depends(get_current_user)]