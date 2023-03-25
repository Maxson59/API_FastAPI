from sqlalchemy import create_engine, MetaData

DATABASE_URL = "sqlite:///./datab.sqlite3?check_same_thread=False"

engine = create_engine(DATABASE_URL)

metadata = MetaData()

