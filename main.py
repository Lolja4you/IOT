import os, threading, sys

from src.wsgi.server import Server
from src.utils.confloader import AppConfig
# from src.utils.abc import Logger

# from src.client import manage as client
from src.backend import manage as back
from src.backend.urls import urls

from src.client.GUI.main_page import StartPage
from src.client.states import ProgState


class MainApp:
    def __init__(self):
        self.BASE_DIR = os.path.abspath(os.path.dirname(__file__))
        self.is_debug = False

        # Запускаем сервер в отдельном потоке
        self.server_thread = threading.Thread(target=self.start_server)
        self.server_thread.daemon = False  # Это поток будет работать в фоне
        self.server_thread.start()

        # Запускаем tkinter в основном потоке
        self.start_tkinter()

    def start_server(self):
        server = Server(routes=urls
            # Добавьте маршруты и соответствующие функции обработчики
        )
        server.serve_forever()

    def start_tkinter(self):
        self.app = StartPage(ProgState())
        self.app.mainloop()

        # Ожидаем завершения серверного потока перед закрытием приложения
        self.server_thread.join()

    def exit_application(self):
        # Остановка сервера
        self.server.stop()
        # Ожидание завершения серверного потока
        self.server_thread.join()
        # Завершение работы приложения
        sys.exit(0)


    def on_closing(self):
        # Этот метод будет вызван при закрытии окна tkinter
        self.app.destroy()
        self.exit_application()

if __name__ == "__main__":
    app = MainApp()
    app.app.protocol("WM_DELETE_WINDOW", app.on_closing)