import pandas as pd


class DataAnalyze:
    def __init__(self):
        # self.res_name_conf = self.load_res_name_conf()
        self.data = pd.DataFrame({})
    
    def update_data(self, data):
        self.data = pd.DataFrame(data)

        # Exclude empty or all-NA columns before concatenating

    def get_format(self):
        return self.data