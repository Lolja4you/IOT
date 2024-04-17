import datetime, threading

import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


from src.client.GUI.base_page import BaseWindow
from src.client.GUI.layouts import LogText, PlotHelper

import tkinter as tk
from tkinter import filedialog, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# from src.UI.pages import settings_page

class StartPage(BaseWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.process_running = False
        self.settings = False

        self.tool_frame = tk.Frame(self, bd=2)
        self.tool_frame.pack(side=tk.RIGHT, fill=tk.Y)

        self.button_frame = tk.Frame(self)
        self.button_frame.pack(side=tk.TOP, fill=tk.X)
        # 
        self.create_buttons()
        self.create_checkboxes()

        # Создаем график
        self.fig = plt.figure(figsize=(6, 4))
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

    def create_buttons(self):
        # Создаем кнопку "Открыть файл"
        self.open_file_button = tk.Button(self.button_frame, text="Открыть файл", command=self.open_file)
        self.open_file_button.pack(side=tk.LEFT, padx=5)

        # Создаем кнопку "Отобразить"
        self.display_button = tk.Button(self.button_frame, text="Отобразить", command=self.display_plot)
        self.display_button.pack(side=tk.LEFT, padx=5)

    def create_checkboxes(self):
        # Создаем фрейм для чекбоксов акций
        self.stocks_frame = tk.LabelFrame(self.button_frame, text="Акции")
        self.stocks_frame.pack(side=tk.RIGHT, padx=5)

        # Создаем чекбоксы для акций
        self.stocks_var = tk.StringVar()
        self.stocks = ["CHMF", "GAZP", "YNDX"]
        for stock in self.stocks:
            tk.Radiobutton(self.stocks_frame, text=stock, variable=self.stocks_var, value=stock).pack(anchor=tk.W)

        # Создаем фрейм для чекбоксов типа графика
        self.plot_type_frame = tk.LabelFrame(self.button_frame, text="Тип графика")
        self.plot_type_frame.pack(side=tk.RIGHT, padx=5)

        # Создаем чекбоксы для типа графика
        self.plot_type_var = tk.StringVar()
        self.plot_types = ["Линейный", "Свечной"]
        for plot_type in self.plot_types:
            tk.Radiobutton(self.plot_type_frame, text=plot_type, variable=self.plot_type_var, value=plot_type).pack(anchor=tk.W)

    def open_file(self):
        # Открываем диалог выбора файла
        file_path = filedialog.askopenfilename()
        if file_path:
            # Здесь вы можете добавить логику для обработки выбранного файла
            messagebox.showinfo("Файл открыт", f"Выбран файл: {file_path}")
        with open(file_path, 'r') as data:
            self.prog_state.data_storage.update_data(str(data))


    # ПОДУМАТЬ НАД ЭТИМ ПОЛУЧШЕ
    def display_plot(self):
        # Получаем выбранную акцию и тип графика
        selected_stock = self.stocks_var.get()
        selected_plot_type = self.plot_type_var.get()

        if not selected_stock or not selected_plot_type:
            messagebox.showerror("Ошибка", "Не выбрана акция или тип графика.")
            return

        # Запрашиваем данные с сервера
        data = self.get_data_from_server(selected_stock)
        # data pars

        # Отрисовываем график
        if data:
            self.plot_data = PlotHelper(data, 
                                        type_plot=selected_plot_type, 
                                        canvas = self.canvas, fig = self.fig
                                       )
            self.plot_data.update_plot()


    # ОТДЕЛИТЬ ЕМУ ТУТ НЕ МЕСТО!
    def get_data_from_server(self, stock):
        import socket
        # Количество попыток подключения
        max_attempts = 2
        for attempt in range(max_attempts):
            try:
                # Создаем сокет
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

                # Подключаемся к серверу
                s.connect(('127.0.0.1', 8000))

                # Формируем HTTP-запрос
                http_request = f'GET /{stock.upper()} HTTP/1.1\r\nHost: 127.0.0.1:8000\r\n\r\n'

                # Отправляем запрос
                s.sendall(http_request.encode('utf-8'))

                # Получаем данные из сокета
                data = b''
                while True:
                    part = s.recv(1024)
                    data += part
                    if len(part) < 1024:
                        break

                # Декодируем данные и выводим их
                print(data.decode('utf-8'))

                # Закрываем соединение
                s.close()

                # Если данные получены, возвращаем их
                return data.decode('utf-8')

            except socket.error as e:
                print(f'Ошибка при подключении к серверу: {e}')
                # Если это последняя попытка, вызываем окно с ошибкой
                if attempt == max_attempts - 1:
                    messagebox.showerror("Ошибка", "Не удалось получить данные с сервера.")

        # Если данные не были получены, возвращаем None
        return None


    # НАСЛЕДОВАНО ОТ ПРЕДКА
    def on_close(self, event=None):
        plt.close(self.fig) 
        return super().on_close(event)
