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