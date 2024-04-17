import logging

class Logger:
    def __init__(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)

        # Создание обработчика для вывода в консоль
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)

        # Формат лога
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        console_handler.setFormatter(formatter)

        # Добавление обработчика в логгер
        self.logger.addHandler(console_handler)

        self.info('Logger is ready')

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)


logger = Logger()