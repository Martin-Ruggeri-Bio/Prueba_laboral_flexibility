from sqlalchemy import Column, Integer, String, ForeignKey, Numeric
from sqlalchemy.orm import relationship, validates
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Cliente(Base):
    __tablename__ = 'clientes'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

    cuentas = relationship('Cuenta', back_populates='cliente')

    @validates('name')
    def validate_name(self, key, name):
        if not name:
            raise ValueError("El nombre del cliente no puede estar vacío.")
        return name

class Cuenta(Base):
    __tablename__ = 'cuentas'

    id = Column(Integer, primary_key=True, index=True)
    balance = Column(Numeric(10, 2), nullable=False)
    cliente_id = Column(Integer, ForeignKey('clientes.id'), nullable=False)

    cliente = relationship('Cliente', back_populates='cuentas')

    @validates('balance')
    def validate_balance(self, key, balance):
        if balance < 0:
            raise ValueError("El balance de la cuenta no puede ser negativo.")
        return balance