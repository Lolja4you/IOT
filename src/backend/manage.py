from src.wsgi.server import Server


from src.backend.urls import urls
from src.utils.abc import logger

def init_backend():
    try:
        backend = Server(HOST='0.0.0.0', PORT=8000, routes=urls)
        
        backend.serve_forever()
    except Exception as e:
        logger.critical(e)