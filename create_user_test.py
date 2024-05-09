import configuration
import requests
import sender_stand_request
import data


# Se cambia el valor del parámetro firstName
# Se devuelve un nuevo diccionario con el valor firstName requerido
def get_user_body(first_name): # esta función cambia los valores en el parámetro "firstName"
    current_body = data.user_body.copy()# el diccionario que contiene el cuerpo de solicitud se copia del archivo "data" (datos) para conservar los datos del diccionario de origen
    current_body["firstName"] = first_name
    return current_body

#Prueba 1. Creación de un nuevo usuario o usuaria. Cuando el parámetro "firstName" contiene dos caracteres
def test_create_user_2_letter_in_first_name_get_success_response(): # El parámetro "firstName" contiene dos caracteres
    user_body = get_user_body("Aa") # La versión actualizada del cuerpo de solicitud con el nombre "Aa" se guarda en la variable "user_body"
    user_response = sender_stand_request.post_new_user(user_body) # El resultado de la solicitud relevante se guarda en la variable "user_response"
    assert user_response.status_code == 201 # Comprueba si el código de estado es 201
    assert user_response.json()["authToken"] != "" # Comprueba que el campo authToken está en la respuesta y contiene un valor
    users_table_response = sender_stand_request.get_users_table()         # El resultado de la solicitud de recepción de datos de la tabla "user_model" se guarda en la variable "users_table_response"#
    str_user = user_body ["firstName"] + "," + user_body["phone"] + "," \
               + user_body["address"] + ",,," + user_response.json()["authToken"] # El string que debe estar en el cuerpo de la respuesta para recibir datos de la tabla "users" se ve así#
    assert users_table_response.text.count(str_user) == 1         # Comprueba si el usuario o usuaria existe y es único/a


# Función de prueba positiva. Comprobar si hay un registro de creación de un nuevo usuario o usuaria guardado en la tabla users
def positive_assert(first_name):
    user_body = get_user_body(first_name)  # El cuerpo de la solicitud actualizada se guarda en la variable user_body
    user_response = sender_stand_request.post_new_user(user_body) # El resultado de la solicitud para crear un/a nuevo/a usuario/a se guarda en la variable user_response
    assert user_response.status_code == 201 # Comprueba si el código de estado es 201
    assert user_response.json()["authToken"] != ""
    users_table_response = sender_stand_request.get_users_table()
    str_user = user_body["firstName"] + "," + user_body["phone"] + "," \
               + user_body["address"] + ",,," + user_response.json()["authToken"]
    assert users_table_response.text.count(str_user) == 1

# Prueba 1. Nombre de usuario de 2 caracteres.
def test_create_user_2_letter_in_first_name_get_success_response():# El parámetro "firstName" contiene dos caracteres
    positive_assert("Aa")

# Prueba 2. Nombre de usuario de 15 caracteres
def test_create_user_15_letter_in_first_name_get_success_response():# El parámetro "firstName" contiene 15 caracteres
    positive_assert("Aaaaaaaaaaaaaaa")

# Preparación Función de prueba negativa
def negative_assert_symbol(first_name):
    user_body = get_user_body(first_name)  # El cuerpo de la solicitud actualizada se guarda en la variable user_body
    response = sender_stand_request.post_new_user(user_body) # Comprueba si la variable "response" almacena el resultado de la solicitud.
    assert response.status_code == 400 #Comprueba si el atributo "code" en el cuerpo de respuesta es 400
    assert response.json()["code"] == 400    # Comprueba si el atributo "code" en el cuerpo de respuesta es 400.
    assert response.json()["message"] == "Has introducido un nombre de usuario no válido. " \
                                         "El nombre solo puede contener letras del alfabeto latino, "\
                                         "la longitud debe ser de 2 a 15 caracteres."

#Prueba 3: Nombre de un solo caracter
def test_create_user_1_letter_in_first_name_get_error_response(): # El parámetro "firstName" contiene 1 caracter
        negative_assert_symbol("A")

#Prueba 4: Nombre con 16 caracteres
def test_create_user_16_letter_in_first_name_get_error_response(): ## El parámetro "firstName" contiene 16 caracters
    negative_assert_symbol("Aaaaaaaaaaaaaaaa")

#Prueba 5: user has space in first name
def test_create_user_has_space_in_first_name_get_error_response():
    negative_assert_symbol("A Aaa")

#Prueba 6:
def test_create_user_has_special_symbol_in_first_name_get_error_response():
    negative_assert_symbol("\"№%@\",")

#Prueba 7:
def test_create_user_has_number_in_first_name_get_error_response():
    negative_assert_symbol("123")

#Preparación pruebas 8 y 9 para el user body:
def negative_assert_no_first_name(user_body):
    response = sender_stand_request.post_new_user(user_body)  # Guarda el resultado de llamar a la función a la variable "response"
    assert response.status_code == 400 #Comprueba si el atributo "code" en el cuerpo de respuesta es 400
    assert response.json()["code"] == 400    # Comprueba si el atributo "code" en el cuerpo de respuesta es 400.
    assert response.json()["message"] == "No se han aprobado todos los parámetros requeridos"

#Prueba 8.  El parámetro no se pasa en la solicitud
def test_create_user_no_first_name_get_error_response(): #La solicitud no contiene el parámetro "firstName"
    user_body = data.user_body.copy()    # El diccionario con el cuerpo de la solicitud se copia del archivo "data" a la variable "user_body. De lo contrario, se podrían perder los datos del diccionario de origen
    user_body.pop("firstName") # El parámetro "firstName" se elimina de la solicitud
    negative_assert_no_first_name (user_body)  # Comprueba la respuesta

#Prueba 9.  Se ha pasado un valor de parámetro vacío
def test_create_user_empty_first_name_get_error_response():
    user_body = get_user_body(" ")  # El cuerpo de la solicitud actualizada se guarda en la variable user_body
    negative_assert_no_first_name(user_body)

#Prueba 10. Se ha pasado otro tipo de parámetro "firstName": número
def test_create_user_number_type_first_name_get_error_response():
    user_body = get_user_body(12)  # El cuerpo de la solicitud actualizada se guarda en la variable user_body
    response = sender_stand_request.post_new_user(user_body)  # Guarda el resultado de llamar a la función a la variable "response"
    assert response.status_code == 400 #Comprueba si el atributo "code" en el cuerpo de respuesta es 400
