from sqlalchemy.orm import Session
from . import models, schemas
#ejemplo simple para el crud, es para parobar si es que funciona la base
def crear_evento(db: Session, evento: schemas.EventoCreate):
    db_evento = models.Evento(**evento.dict())
    db.add(db_evento)
    db.commit()
    db.refresh(db_evento)
    return db_evento

def obtener_eventos(db: Session):
    return db.query(models.Evento).all()
