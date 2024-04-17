import time, logging, threading

# from src.DataBase.usb_read import get_avalibal_ports, UsbRead, speeds
# from src.DataBase.test_data_gen import data_test_gen
from src.client.network.get_data import DataAnalyze


class ProgState:
    def __init__(self) -> None:
        self.data_storage = DataAnalyze()
        # self.avalibal_ports = get_avalibal_ports()
        # self.avalibal_speeds = speeds
        # self.is_reconect = False