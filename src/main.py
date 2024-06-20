from fastapi import FastAPI
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi.staticfiles import StaticFiles

from redis import asyncio as aioredis
from .config import REDIS_HOST, REDIS_PORT

from starlette.middleware.cors import CORSMiddleware

from src.auth.schemas import UserRead, UserCreate
from src.auth.base_config import auth_backend, fastapi_users

from src.operations.router import router as router_operation

from src.tasks.router import router as router_task

from src.pages.router import router as router_pages

from src.chat.router import router as router_chat


app = FastAPI(
    title="Trading App"
)


app.mount("/static", StaticFiles(directory="src/static"), name="static")


app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth",
    tags=["Auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["Auth"],
)


app.include_router(router_operation)
app.include_router(router_task)
app.include_router(router_pages)
app.include_router(router_chat)


origins = [
    "http://localhost:5000",
    "http://127.0.0.1:5000",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=[
        "Content-Type",
        "Set-Cookie",
        "Access-Control-Allow-Headers",
        # "Access-Control-Allow-Origin",
        "Authorization",
    ],
)


@app.on_event("startup")
async def startup():
    redis = aioredis.from_url(f"redis://{REDIS_HOST}:{REDIS_PORT}")
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
