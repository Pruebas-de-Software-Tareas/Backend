from fastapi import FastAPI, Depends
from fastapi import security
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine, Base
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from datetime import timedelta
from jose import JWTError
from fastapi.middleware.cors import CORSMiddleware
from . import security 

Base.metadata.create_all(bind=engine)

app = FastAPI()
origins = [
    "http://localhost:5173", 
    "http://localhost:3000",  
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_current_user(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    """Dependencia para obtener el usuario actual a partir del token."""
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="No se pudieron validar las credenciales",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = security.jwt.decode(token, security.SECRET_KEY, algorithms=[security.ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = schemas.TokenData(username=username)
    except JWTError:
        raise credentials_exception
    
    user = crud.get_user_by_username(db, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user



@app.post("/register/", response_model=schemas.Usuario)
def register_user(user: schemas.UsuarioCreate, db: Session = Depends(get_db)):
    """Endpoint para registrar un nuevo usuario."""
    db_user = crud.get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="El nombre de usuario ya está registrado")
    return crud.create_user(db=db, user=user)

@app.post("/token", response_model=schemas.Token)
def login_for_access_token(db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()):
    """Endpoint para iniciar sesión y obtener un token."""
    user = crud.get_user_by_username(db, form_data.username)
    if not user or not security.verify_password(form_data.password, user.hashed_password):
     raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Usuario o contraseña incorrectos",
        headers={"WWW-Authenticate": "Bearer"},
    )

    access_token_expires = timedelta(minutes=security.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = security.create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}




@app.post("/eventos/", response_model=schemas.Evento)
def crear_evento(
    evento: schemas.EventoCreate, 
    db: Session = Depends(get_db), 
    current_user: models.Usuario = Depends(get_current_user) 
):
    
    return crud.crear_evento(db=db, evento=evento)

@app.get("/eventos/")
def leer_eventos(db: Session = Depends(get_db)):
    return crud.obtener_eventos(db)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
