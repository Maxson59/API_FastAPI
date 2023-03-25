from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table
from config.db import engine, metadata

tickets = Table(
    "tickets",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name_event", String(50), nullable=False),
    Column("code", String(50), nullable=False),
    Column("location", String(50), nullable=False),
    Column("date", String(50), nullable=False),
    Column("price", Float, nullable=False),
    Column("transaction_counter", Integer, nullable=False),
    Column("owner", Integer, nullable=False),
)

metadata.create_all(engine)