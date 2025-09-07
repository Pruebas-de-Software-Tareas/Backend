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
