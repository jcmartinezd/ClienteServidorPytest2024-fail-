import pytest   
import requests
from servidor import app # Importar la app de Flask
from cliente import obtener_usuarios

@pytest.fixture(scope="module")
def app_cliente():
    with app.test_client() as test_client:
        yield test_client
def test_servidor_responde(app_cliente):
    response = app_cliente.get('/usuarios')
    assert response.status_code == 200

def test_formato_json(app_cliente): # Prueba el formato de JSON de la respuesta 
    response = app_cliente.get('/usuarios')
    assert response.content_type == 'application/json'

def test_contendio_respuesta(app_cliente): # Prueba el contenido de la respuesta
    response = app_cliente.get('/usuarios')
    data = response.get_json()
    assert isinstance(data, list)    
    assert len(data) == 2 # verificar la cantidad de usuarios
    assert data[0]['id']==1
    assert data[0]['nombre']=="Juan"
    assert data[1]['id']==2
    assert data[1]['nombre']=="María"

def test_cliente_obtiene_usuarios(app_cliente): #prueba la función del cliente
    base_url = "http:localhost:5000"
    with app.test_request_context():
        usuarios = obtener_usuarios(f"{base_url}/usuarios")
        assert usuarios is not None
        assert len(usuarios) == 2
        assert usuarios[0]['id']==1
        assert usuarios[0]['nombre']=="Juan"
        assert usuarios[1]['id']==2
        assert usuarios[1]['nombre']=="María"

def test_cliente_error_servidor(): # Simular un error del servidor
    usuarios = obtener_usuarios('http://localhost:5001/usuarios')
    assert usuarios is None                            
                                    