import socket
import threading
from urllib.parse import urlparse
from src.utils.urldispatch import RegexDispatch
from src.utils.abc import logger

class Server:
    def __init__(self,
                HOST="0.0.0.0", 
                PORT=8000, 
                BUFFER_LENGTH=2048,
                routes = None,
    ) -> None:
        # Base conf
        self.HOST:str = HOST
        self.PORT:int = PORT
        self.BUFFER_LENGTH:int = BUFFER_LENGTH
        self.is_running = True
        if routes:
            self.routes = {route: func for route, func in routes}

        # WSGI
        self.sock:socket.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.HOST, self.PORT))
        self.sock.listen(1)

        # Utils
    

        # Threading


    def serve_forever(self):
        logger.info(f'Server is running on {self.HOST}:{self.PORT}')
        logger.info(f'Available routes: {list(self.routes.keys())}')
        while self.is_running:
            try:
                client_connection, client_address = self.sock.accept()
                threading.Thread(target=self.handle_request, args=(client_connection,)).start()
            except KeyboardInterrupt:
                logger.info("Server is shutting down...")
                self.sock.close()  # Закрытие сокета для остановки сервера
                logger.info("Server has stopped.")
                break

    def handle_request(self, client_connection):
        request_data = client_connection.recv(self.BUFFER_LENGTH).decode('utf-8')
        headers, body = request_data.split('\r\n\r\n')
        method, path, version = headers.split('\n')[0].split()
        path = urlparse(path).path

        logger.info(f"Received request from {client_connection.getpeername()}")
        logger.info(f"Request method: {method}, path: {path}")

        environ = {
            'PATH_INFO': path,
            'REQUEST_METHOD': method,
            # Добавьте другие переменные окружения, если нужно
        }

        # Используйте RegexDispatch для сопоставления маршрута и вызова соответствующей функции
        dispatcher = RegexDispatch(self.routes)
        response = dispatcher(environ, self.start_response)
        # logger.debug(response)
        client_connection.sendall(response.encode())
        client_connection.close()

    def start_response(self, status, response_headers, exc_info=None):
        # Этот метод будет использоваться для отправки заголовков ответа
        server_headers = [
            # ('Date', self.helper.get_date_time_string()),
            ('Server', 'MySocket')
        ]

        self.headers_set = [status, response_headers + server_headers]
    # Остальные методы класса Server...

    def stop(self):
        self.is_running = False
        # Закрытие сокета, чтобы прервать блокировку accept
        self.sock.close()