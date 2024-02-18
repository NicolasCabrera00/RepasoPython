import requests

response = requests.get("https://api.github.com") ##almaceno la solicitud a traves de get
print(response)  #asi solo muestra el numero de respuesta
print(response.headers) #asi muestra toda la info
##   response.status_code --> para saber el numero de estatus de la respuesta
 
"""  Para acceder a los datos de la respuesta(cuerpo o carga) hay tres maneras: 

response.content que devuelve la respuesta en bites
response.text  que convierte en texto la respuesta, da como resultado string
response.json() retorna como diccionario de python (al cuerpo)
print(response,json()["current_user_url"]) para acceder a una llave en especifico. """

""" Puedo usar query como filtros (buscar palabras clave) de la siguiente manera

responseEjemplo2 = requests.get(
    "https://api.github.com/repositories", 
    params = {"q" : "python"}   #Las llaves son los parametros de busqueda y los valores son los que vamos a usar para relaizar esa busqueda
                                #q permite buscar la palabra clave
)
print(response.status_code) ##Para ver el estatus de la respuesta (200 es ok)

Se pueden almacenar los datos retornados ya que lo pasamos a JSON

datos = response.json()
print(datos.keys())

"""

