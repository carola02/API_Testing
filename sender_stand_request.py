import configuration
import requests
import data

#1. Utils → Logs del servidor principal.#
def get_logs():
    return requests.get(configuration.URL_SERVICE + configuration.LOG_MAIN_PATH)
response = get_logs()
print(response.status_code)
print(response.headers)

#2.Comporbación del número de parámetros#
#def get_logs():
    #return requests.get(configuration.URL_SERVICE + configuration.LOG_MAIN_PATH,
                        #params={"count": 20})
#response = get_logs()
#print(response.status_code)
#print(response.headers)

#3. Utils → Recuperar información de la tabla de base de datos#
def get_users_table():
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)
response = get_users_table()
print(response.status_code)

#4. creación de nuevo usuario
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
            json=body,
            headers=data.headers)
response = post_new_user(data.user_body)
print(response.status_code)
print(response.json())

#5.
def post_products_kits(products_ids):     # Realiza una solicitud POST para buscar kits por productos.
    return requests.post(configuration.URL_SERVICE + configuration.PRODUCTS_KITS_PATH, # Concatenación de URL base y ruta.
                        json=products_ids, # Datos a enviar en la solicitud.
                        headers=data.headers) # Encabezados de solicitud.
response = post_products_kits(data.product_ids)
print(response.status_code)
print(response.json()) # Muestra del resultado en la consola
