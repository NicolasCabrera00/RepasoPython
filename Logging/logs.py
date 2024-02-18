import logging 

logging.basicConfig(level= logging.DEBUG, filename="EjemploLog.log")  ##Python, por defecto corre a partir de warning. Con esta funcion, hago
                                            ##que ejecute desde el nivel que yo prefiero. Tambien defino un nueo archivo en
                                            ##el cual se guarden estos debugs

logging.debug("Mensaje debug. Primer nivel")
logging.info("Log of info. Second level")
logging.warning("Log of warning. 3th level")
logging.critical("Log of CRITICAL. 4th level")
logging.error("Log ERROR. 5th and the last level")

