import redis.asyncio as redis
import uvicorn
from fastapi import FastAPI
from sqlalchemy import create_engine, Integer, Column, String
from sqlalchemy.orm import sessionmaker, declarative_base

from config import settings

app = FastAPI(title="FastAPI, Docker, Redis, Postgres")

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)


engine = create_engine(settings.postgresql_uri, echo=True)

Base.metadata.create_all(engine)

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


if __name__ == '__main__':
    uvicorn.run("main:app", host=settings.host, port=settings.fast_api_port, reload=True)
