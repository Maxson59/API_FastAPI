from fastapi import FastAPI, Path, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from routers.rt_users import user
from routers.rt_tickets import ticket
import uvicorn

app = FastAPI()

#["http://localhost:8100"]

app.include_router(user)
app.include_router(ticket)

# Permitir cualquier origen
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)