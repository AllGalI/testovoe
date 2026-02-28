import uvicorn
from fastapi import FastAPI
from contextlib import asynccontextmanager

from src.configs.db import Sessionmaker, seed_data
from src.routes import *

@asynccontextmanager
async def lifespan(app: FastAPI):
    with Sessionmaker() as session:
        seed_data(session)

    yield

app = FastAPI(lifespan=lifespan)

app.include_router(router_activities)
app.include_router(routre_buildings)
app.include_router(route_orrganization)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)