import json, os


class AppConfig:
    def __init__(self, BASE_DIR, conf_file_path: str = 'assets/conf/conf.json') -> None:
        self.error_dict_conf_loader = {}

        self.CONF_DIR:str = os.path.join(BASE_DIR, conf_file_path)
        
        self.API:str
        
        # self.ACTION_TEST_GEN 

        self.URL_PROXY:str
        
        self.FONT_FAMILY_SIZE:str

    def open_conf(self):
        # Сброс статуса перед открытием файла
        self.error_dict_conf_loader.clear()

        # Загрузка и установка конфигурации
        try:
            with open(self.CONF_FILE_PATH, 'r') as file:
                conf = json.load(file)
                for key, value in conf.items():
                    setattr(self, key, value)
                    self.error_dict_conf_loader[key] = "OK"
        except Exception as e:
            self.error_dict_conf_loader["config_load"] = str(e)


        for key, status in self.error_dict_conf_loader.items():
            color_code = '\033[32m' if status == "OK" else '\033[33m'
            reset_code = '\033[0m'
            print(f"{key}: {color_code}{status}{reset_code}")


    def save_conf(self):
        conf = {
            'API': self.API,
            # 'ACTION_TEST_GEN': self.ACTION_TEST_GEN,
            'URL_PROXY': self.URL_PROXY,
            'FONT_FAMILY_SIZE': self.FONT_FAMILY_SIZE
        }
        try:
            with open(self.CONF_FILE_PATH, 'w') as file:
                json.dump(conf, file, indent=4)
                for key in conf.keys():
                    self.error_dict_conf_loader[key] = "OK"
        except Exception as e:
            self.error_dict_conf_loader[key] = str(e)

    def update_conf(self, key: str, value: str):
        try:
            with open(self.CONF_FILE_PATH, 'r+') as file:
                conf = json.load(file)
                conf[key] = value
                file.seek(0)
                json.dump(conf, file, indent=4)
                file.truncate()
                self.error_dict_conf_loader[key] = "OK"
        except Exception as e:
            self.error_dict_conf_loader[key] = str(e)

    def is_ok_load_conf(self):
        return all(status == "OK" for status in self.error_dict_conf_loader.values())

