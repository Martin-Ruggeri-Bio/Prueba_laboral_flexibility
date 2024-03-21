import argparse
import os

def borrar_archivo(nombre_archivo):
    try:
        os.remove(nombre_archivo)
        print(f"El archivo '{nombre_archivo}' ha sido borrado exitosamente.")
    except FileNotFoundError:
        print(f"Error: El archivo {nombre_archivo} no existe.")
    except PermissionError:
        print(f"Error: Permiso denegado para borrar el archivo {nombre_archivo}.")
    except Exception as e:
        print(f"No se pudo borrar el archivo '{nombre_archivo}': {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Borra un archivo dado.")
    parser.add_argument("archivo", metavar="ARCHIVO", type=str, help="Ruta del archivo a borrar")
    args = parser.parse_args()

    borrar_archivo(args.archivo)