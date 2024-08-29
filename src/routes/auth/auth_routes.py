from fastapi import APIRouter, status, Body
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from sqlmodel import select
from typing import Annotated

from ...app.dependencies.auth_dependencies import Oauth2SchemaDep
from ...app.models.auth.user_model import User
from ...app.dependencies.auth_dependencies import (
    GetCurrentUserDep,
    get_password_hash,
    verify_password,
)
from ...app.dependencies.common_dependencies import SessionDep
from ...app.validations.request_models.auth.create_user_model import CreateUserModel
from ...app.validations.request_models.auth.login_model import LoginModel
from ...app.validations.response_models.auth.login_response_model import (
    LoginSuccessModel,
)

router = APIRouter(prefix="/auth", tags=["auth_routes"], dependencies=[])


@router.get("/user", status_code=status.HTTP_200_OK)
def user(token: Oauth2SchemaDep):
    print("token :", token)

    return "authenticated user"


@router.get("/user/me")
async def read_users_me(current_user: GetCurrentUserDep):
    print("this is current user :", current_user)
    return current_user


@router.post("/user/create", status_code=status.HTTP_201_CREATED)
def create_user(body: Annotated[CreateUserModel, Body()], session=SessionDep):
    data = body.model_dump()

    hashed_password = get_password_hash(data["password"])

    data["password"] = hashed_password

    user = User(**data)

    try:
        session.add(user)
        session.commit()

    except:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST, body=jsonable_encoder(user)
        )

    return {"message": "User created successfully", "body": user}


@router.post("/login", status_code=status.HTTP_200_OK, response_model=LoginSuccessModel)
def login(body: Annotated[LoginModel, Body()], session=SessionDep):
    data = body.model_dump()

    query = select(User).where(User.username == data["username"])

    user = session.exec(query).first()

    if not user:
        return {
            "status": status.HTTP_404_NOT_FOUND,
            "message": "No Found.",
            "data": None,
        }
    
    else:
        validUser = verify_password(data["password"], user.password)

        if not validUser:
            return {
                "status": status.HTTP_401_UNAUTHORIZED,
                "message": "Username Or Password may be incorrect.",
                "data": None,
            }

        else:
            return {
                "status": status.HTTP_200_OK,
                "message": "Login successful",
                "data": user,
            }
