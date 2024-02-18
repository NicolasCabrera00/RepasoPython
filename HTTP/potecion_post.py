import requests

url = "https://webhook.site/e3a0a12a-e615-4e5f-b534-e14b95eb3901"

##voy a crear una orden en forma de diccionario para que se pueda pasar JSON luego


payload = {"plato" : "pasta",
           "cantidad" : 2
           }
response = requests.post(url, data=payload)
print(response.status_code)
print(response.text)