from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from models import Client, Base
from dotenv import load_dotenv
import os
import logging

logging.basicConfig(level=logging.ERROR)

load_dotenv()
DB_FILE = os.getenv('DB_FILE')
engine = create_engine(f"sqlite:///{DB_FILE}", echo=True)
Base.metadata.create_all(engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class ClientCreate(BaseModel):
    nombre: str
    email: str
    telefono: str

class ClientGet(BaseModel):
    id: int
    nombre: str
    email: str
    telefono: str

app = FastAPI()

# Dependencia para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/api/clients/", response_model=ClientGet)
def create_client(client: ClientCreate, db: Session = Depends(get_db)):
    db_client = db.query(Client).filter(Client.email == client.email).first()
    if db_client:
        logging.error(f"El cliente con este correo electrónico ya existe: {client.email}")
        raise HTTPException(status_code=400, detail="El cliente con este correo electrónico ya existe")
    db_client = Client.model_dump(client)
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client

@app.get("/api/clients/{client_id}", response_model=ClientGet)
def get_client(client_id: int, db: Session = Depends(get_db)):
    db_client = db.query(Client).filter(Client.id == client_id).first()
    if db_client is None:
        logging.error(f"Cliente no encontrado: {client_id}")
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return db_client

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)