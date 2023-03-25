from sqlalchemy import Column, Integer, String, ForeignKey, Table
from config.db import engine, metadata

users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("user_name", String(50), nullable=False),
    Column("user_email", String(50), nullable=False),
    Column("user_password", String(50), nullable=False),
    Column("user_telephone", String(50), nullable=False),
)

metadata.create_all(engine)