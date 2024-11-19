import requests  # Importa la biblioteca requests para hacer peticiones HTTP

def obtener_usuarios(url='http://localhost:5000/usuarios'):  # Añadiendo parámetro url
    # Realiza una petición GET al servidor
    response = requests.get(url)  
    if response.status_code == 200:  # Si la respuesta es exitosa (código 200)
        return response.json() # Retornar la lista de usuarios
    else:
        return None  # Retorna None en caso de error
        
if __name__ == '__main__':
    obtener_usuarios()  # Ejecuta la función al iniciar el script
    if usuarios:
        print ("Usuarios encontrados:")
        for usuario in usuarios:
            print(f"ID: {usuario['id']}, Nombre: {usuario['nombre']}")
    else:
        print("No se encontraron usuarios.")     