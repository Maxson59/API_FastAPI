from fastapi import APIRouter, Response, HTTPException
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_401_UNAUTHORIZED
from schemas.user_schema import UserSchema, DataUserSchema
from config.db import engine
from models.users import users
from models.tickets import tickets
# Hashear password
# pip install werkzeug
from werkzeug.security import generate_password_hash, check_password_hash
from typing import List

user = APIRouter()


@user.get("/")
def root():
    return {"message": "Hola"}


# SELECT
@user.get("/api/user", response_model=List[UserSchema])
def get_users():
    with engine.connect() as conn:
        result = conn.execute(users.select()).fetchall()

        return result


@user.get("/api/user/{user_id}", response_model=UserSchema)
def get_user(user_id: str):
    with engine.connect() as conn:
        # .c hace referencia a columna 
        result = conn.execute(users.select().where(users.c.id == user_id)).first()

        return result


# CREATE
@user.post("/api/user", status_code=HTTP_201_CREATED)
def create_user(data_user: UserSchema):
    # con el entorno with hacemos que se cierre la conexion de la bd cuando se deje de utilizar
    with engine.connect() as conn:
        new_user = data_user.dict()
        new_user["user_password"] = generate_password_hash(data_user.user_password, "pbkdf2:sha256:30", 30)
       
        conn.execute(users.insert().values(new_user))

        return Response(status_code=HTTP_201_CREATED)
    

# Verificar si el usuario existe
@user.post("/api/user/login", status_code=200)
def user_login(data_user: DataUserSchema):
    with engine.connect() as conn:
        result = conn.execute(users.select().where(users.c.user_name == data_user.user_name)).first()
        print(result)
        # Si no existe nos devuelve None
        if result != None:
            # result[3] nos da el tercer valor de la tupla de resultado, es decir, la contraseña hasheada
            check_password = check_password_hash(result[3], data_user.user_password)

            if check_password:
               print(result)
               return {
                   "status": 200,
                   "message": "Access success",
                   "id_user": result[0]
               }

        return {
            "status": HTTP_401_UNAUTHORIZED,
            "message": "Access denied",
            "id_user": None
        }

# UPDATE
@user.put("/api/user/{user_id}", response_model=UserSchema)
def update_user(user_id: str, data_update: UserSchema):
    with engine.connect() as conn:
        encryp_pass = generate_password_hash(data_update.user_password, "pbkdf2:sha256:30", 30)

        conn.execute(users.update().values(user_name=data_update.user_name, user_email=data_update.user_email, user_password=encryp_pass).where(users.c.id == user_id))

        result = conn.execute(users.select().where(users.c.id == user_id)).first()

        return result
    
# DELETE
@user.delete("/api/user/{user_id}", status_code=HTTP_204_NO_CONTENT)
def delete_user(user_id: str):
    with engine.connect() as conn:
        conn.execute(users.delete().where(users.c.id == user_id))

        return Response(status_code=HTTP_204_NO_CONTENT)
    

# SHOW ALL TICKETS FROM USER
@user.get("/api/user/{user_id}/showtickets", status_code=HTTP_201_CREATED)
def get_user(user_id: str):
    with engine.connect() as conn:
        result = conn.execute(tickets.select().where(tickets.c.owner == user_id)).fetchall()

        return result

