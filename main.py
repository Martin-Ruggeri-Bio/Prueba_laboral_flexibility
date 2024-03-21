from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Cliente, Cuenta
from services import actualizar_balance_por_nombre_cliente
from dotenv import load_dotenv
import os

def crear_tablas(engine):
    Base.metadata.create_all(engine)

def cargar_datos(session):
    # Insertar clientes
    cliente1 = Cliente(name='Cliente1')
    cliente2 = Cliente(name='Cliente2')
    cliente3 = Cliente(name='Cliente3')
    session.add_all([cliente1, cliente2, cliente3])
    session.commit()

    # Insertar cuentas
    cuenta1_cliente1 = Cuenta(balance=100, cliente=cliente1)
    cuenta2_cliente1 = Cuenta(balance=200, cliente=cliente1)
    cuenta1_cliente2 = Cuenta(balance=150, cliente=cliente2)
    cuenta2_cliente2 = Cuenta(balance=250, cliente=cliente2)
    cuenta1_cliente3 = Cuenta(balance=300, cliente=cliente3)
    cuenta2_cliente3 = Cuenta(balance=400, cliente=cliente3)
    session.add_all([cuenta1_cliente1, cuenta2_cliente1, cuenta1_cliente2, cuenta2_cliente2, cuenta1_cliente3, cuenta2_cliente3])
    session.commit()

if __name__ == "__main__":
    load_dotenv()
    
    # MySQL connection string
    # DB_USER = os.getenv('DB_USER')
    # DB_PASSWORD = os.getenv('DB_PASSWORD')
    # DB_HOST = os.getenv('DB_HOST')
    # DB_NAME = os.getenv('DB_NAME')
    # connection_string = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
    
    DB_FILE = os.getenv('DB_FILE')
    try:
        engine = create_engine(f"sqlite:///{DB_FILE}", echo=True)
        Session = sessionmaker(bind=engine)
        session = Session()

        crear_tablas(engine)
        cargar_datos(session)
        nombre_cliente = "Cliente1"
        actualizar_balance_por_nombre_cliente(session, nombre_cliente)

    except Exception as e:
        print(e)
    finally:
        session.close()