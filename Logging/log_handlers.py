import logging

logger = logging.getLogger(__name__)
##cuando usamos handlers no se puede usar basicConfig de la libreria loggin 
logger.setLevel(logging.DEBUG)

handlerConsola = logging.StreamHandler()
formatoLogs = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s") ##creo un formato
handlerConsola.setFormatter(formatoLogs)               ##aplico el formato creado a mi handler
logger.addHandler(handlerConsola)  #defino el logger a el cual pertenece handlerConsole

logger.info("Registro informativo")

##Para escribir los handlers en otro archivo:

handlerArchivo = logging.FileHandler("archivo.log")  #Creo el archivo   
handlerArchivo.setLevel(logging.error) #Establezco su nivel de seriedad
handlerArchivo.setFormatter(formatoLogs) #le doy el formato que cree antes
logger.addHandlerd(handlerArchivo) #añado el hanlder al logger
