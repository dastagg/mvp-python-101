import logging

logging.basicConfig(filename="sample.log", level=logging.INFO)

logging.debug("This is a debug message")
logging.info("Informational message")
logging.error("An error has happened")
logging.warning("This is a warning")
logging.critical("CRITICAL MESSAGE")
