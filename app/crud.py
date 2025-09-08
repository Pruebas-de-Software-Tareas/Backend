from sqlalchemy import func
from sqlalchemy.orm import Session
from . import models, schemas
from sqlalchemy.orm import Session
from . import models, schemas, security
#ejemplo simple para el crud, es para parobar si es que funciona la base
def crear_evento(db: Session, evento: schemas.EventoCreate):
    db_evento = models.Evento(**evento.dict())
    db.add(db_evento)
    db.commit()
    db.refresh(db_evento)
    return db_evento

def obtener_eventos(db: Session):
    return db.query(models.Evento).all()

def generar_reporte_eventos(db: Session):
    total_eventos = db.query(func.count(models.Evento.id)).scalar()  
    suma_cupos = db.query(func.sum(models.Evento.cupos_disponibles)).scalar()  
    eventos_agotados = db.query(func.count(models.Evento.id)).filter(models.Evento.cupos_disponibles == 0).scalar()  

    return {
        "total_eventos": total_eventos,
        "suma_cupos_disponibles": suma_cupos or 0,
        "eventos_agotados": eventos_agotados
    }

def get_user_by_username(db: Session, username: str):
    """Busca un usuario por su nombre de usuario."""
    return db.query(models.Usuario).filter(models.Usuario.username == username).first()

def create_user(db: Session, user: schemas.UsuarioCreate):
    """Crea un nuevo usuario con contraseña hasheada."""
    hashed_password = security.get_password_hash(user.password)
    db_user = models.Usuario(username=user.username, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user