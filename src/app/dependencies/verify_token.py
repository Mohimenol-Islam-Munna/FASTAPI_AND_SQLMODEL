from fastapi import HTTPException

def verify_access_token():
    print("this is verify access token handler")
    raise HTTPException(status_code=401, detail="Your are not authenticated")


class verify_refresh_token:
    def __init__(self) -> None:
        print("this is verify refresh token handler")
