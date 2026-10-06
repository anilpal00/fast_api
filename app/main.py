from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.core.exceptions import UserNotFoundException, DuplicateUserException
from app.api.v1.router import api_router

app = FastAPI(
    title = "FastApi Learning Project",
    version = "1.0.0"
)

app.include_router(api_router)

@app.exception_handler(UserNotFoundException)
async def user_not_found_handler(
    request: Request,
    exc: UserNotFoundException
):
    return JSONResponse(
        status_code=404,
        content={
            "error": "USER_NOT_FOUND",
            "message": exc.message
        }
    )


@app.exception_handler(DuplicateUserException)
async def duplicate_user_handler(
    request: Request,
    exc: DuplicateUserException
):
    return JSONResponse(
        status_code=409,
        content={
            "error": "DUPLICATE_USER",
            "message": exc.message
        }
    )