import redis.asyncio as redis
from fastapi import FastAPI
from sqlalchemy.orm import sessionmaker

from .db import engine

app = FastAPI(title="FastAPI, Docker, Redis, Postgres")

Session = sessionmaker(bind=engine)

redis_connection = redis.Redis(host="redis")


@app.get("/")
async def read_root():
    return []


@app.on_event("startup")
async def startup_db():
    print(f"Ping successful: {await redis_connection.ping()}")
    return


@app.on_event("shutdown")
async def shutdown_db():
    await redis_connection.close()
    return
