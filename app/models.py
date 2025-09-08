from sqlalchemy import Column, ForeignKey, Integer, String, Date
from .database import Base

class Evento(Base):
    __tablename__ = "eventos"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    descripcion = Column(String)
    fecha = Column(Date)
    categoria = Column(String)
    precio = Column(Integer)
    cupos_disponibles = Column(Integer)


#para la parte de autenticacion jeje
class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)

class Entrada(Base):
    __tablename__ = "entradas"
    id = Column(Integer, primary_key=True, index=True)
    evento_id = Column(Integer, ForeignKey("eventos.id"))
    
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))

    estado = Column(String, default="vendida") 