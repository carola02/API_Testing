#creación de un nuevo usuario
headers = {
    "Content-Type": "application/json"
}
user_body = {
    "firstName": "Andrea",
    "phone": "+11234567890",
    "address": "123 Elm Street, Hilltop"
}

#1. Lista de productos POST
headers = {
    "Content-Type": "application/json"
}
product_ids = {
    "ids": [1, 2, 3]
}
