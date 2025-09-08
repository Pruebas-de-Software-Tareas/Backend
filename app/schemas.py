from typing import Optional
from pydantic import BaseModel
from datetime import date

class EventoBase(BaseModel):
    nombre: str
    descripcion: str
    fecha: date
    categoria: str
    precio: int
    cupos_disponibles: int

class EventoCreate(EventoBase):
    pass

class Evento(EventoBase):
    id: int
    class Config:
        orm_mode = True

class UsuarioBase(BaseModel):
    username: str

class UsuarioCreate(UsuarioBase):
    password: str

class Usuario(UsuarioBase):
    id: int
    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None