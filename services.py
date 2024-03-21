
from models import Cliente


def actualizar_balance_por_nombre_cliente(session, nombre_cliente):
    try:
        clientes = session.query(Cliente).filter_by(name=nombre_cliente).all()
        
        if not clientes:
            raise Exception(f"Error: No se encontró ningún cliente con el nombre {nombre_cliente}.")
        if len(clientes) > 1:
            raise Exception(f"Error: Hay más de un cliente con el nombre {nombre_cliente}.")
        
        cliente = clientes[0]

        if not cliente.cuentas:
            raise Exception(f"El cliente {nombre_cliente} no tiene cuentas asociadas.")

        for cuenta in cliente.cuentas:
            cuenta.balance = 0
        session.commit()
        print(f"Se han actualizado los balances de cuenta para el cliente: {nombre_cliente}")
    except Exception as e:
        print(e)
