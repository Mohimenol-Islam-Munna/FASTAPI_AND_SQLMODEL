from fastapi import APIRouter, status, Depends
from typing import Annotated
from ...app.dependencies.auth_dependencies import Oauth2SchemaDep
from ...app.models.auth.user_model import User
from ...app.dependencies.auth_dependencies import GetCurrentUserDep

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
def create_user(body: Annotated[CreateUserModel, Body()])