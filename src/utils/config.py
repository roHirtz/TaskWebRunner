import yaml

from src.utils.yamlloader import Yamlloader


class Config:
    def __init__(self):
        self.yaml = Yamlloader().load(r'conf/conf.yaml')

    def get_driver_path(self, browser='chrome'):
        """
            获取浏览器驱动文件地址
        """
        return self.yaml['chromedriver'][browser]

    def get_test_data(self, method):
        """
            获取数据文件地址
        """
        return f"{self.yaml['testdata']}/{method}.yaml"
