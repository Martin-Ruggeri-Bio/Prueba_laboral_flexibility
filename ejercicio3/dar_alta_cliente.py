import requests
import os
from dotenv import load_dotenv

load_dotenv()

SERVICE_URL = os.getenv('SERVICE_URL')

def create_client(client_data):
    try:
        post_response = requests.post(SERVICE_URL, json=client_data)

        if post_response.status_code == 200 or post_response.status_code == 201:
            client_id = post_response.json().get('id')
            get_response = requests.get(f"{SERVICE_URL}/{client_id}")

            if get_response.status_code == 200 and get_response.json() == client_data:
                return "El cliente fue dado de alta correctamente."
            else:
                return "Error: No se pudo verificar si el cliente fue dado de alta correctamente."
        else:
            return f"Error: No se pudo dar de alta al cliente. Código de estado: {post_response.status_code}: {post_response.text}"
    except requests.exceptions.RequestException as e:
        return f"Error: Ocurrió un problema con la solicitud. Detalles: {e}"


if __name__ == "__main__":
    client_info = {
        "nombre": "Juan Pérez",
        "email": "juan.perez@example.com",
        "telefono": "1234567890"
    }
    print(create_client(client_info))
