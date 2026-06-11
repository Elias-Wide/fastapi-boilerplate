from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.api.endpoints.v1.routers import api_v1_router as main_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(main_router, prefix='/api')
