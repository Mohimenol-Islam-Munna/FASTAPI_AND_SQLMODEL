from fastapi import Request
import time

async def auth_middleware(request: Request, call_next):
    print("----------This is auth middleware 7860 --------------")

    print("request :", request)
    
    start_time = time.time()

    response = await call_next(request)

    print("response :", response)

    process_time = time.time() - start_time

    response.headers["X-Process-Time"] = str(process_time)

    return response