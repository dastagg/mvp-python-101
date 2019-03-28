import logging

logging.basicConfig(filename="sample2.log", level=logging.INFO)
log = logging.getLogger("ex")

try:
    raise RuntimeError
except RuntimeError:
    log.exception("Error")
