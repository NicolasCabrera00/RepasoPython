import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(message)s", ##con format doy formato a los logs
    datefmt="%H:%M:%S"  #FORMATO DE HORA
)

logging.warning("Mensaje de w")
logging.error("Mensaje de error")
logging.critical("Mensaje de critical")

#Ejemplo muy basico de como usar los log

try:
    division =  2/0
except:
    logging.error("Division por cero")