from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import validates
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Client(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    telefono = Column(String, index=True)

    @validates('name')
    def validate_name(self, key, name):
        if not name:
            raise ValueError("El nombre del cliente no puede estar vacío.")
        return name
    
    @classmethod
    def model_dump(cls, instance):
        return cls(**instance.dict())