from fastapi import APIRouter, status, Depends, Body
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import Annotated

from ...app.dependencies.auth_dependencies import Oauth2SchemaDep
from ...app.models.auth.user_model import User
from ...app.dependencies.auth_dependencies import GetCurrentUserDep, get_password_hash
from ...app.dependencies.common_dependencies import SessionDep
from ...app.validations.request_models.auth.create_user_model import CreateUserModel

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
