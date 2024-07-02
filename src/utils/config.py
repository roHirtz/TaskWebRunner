# -*- coding: utf-8 -*-

import os
import sys
from src.utils.yamlloader import Yamlloader


class Config:
    def __init__(self):
        self.yaml = Yamlloader().load(r'conf/conf.yaml')

    def get_driver_path(self, browser='chrome') -> str:
        """
            获取浏览器驱动文件地址
        """

        return self.yaml['selenium']['chromedriver'][sys.platform][browser]

    def get_test_data(self, method):
        """
            获取数据文件地址
        """
        return f"{self.yaml['testdata']}/{method}.yaml"

    def get_selenium_options(self, browser='chrome') -> list:
        """
            获取浏览器options配置
        """
        return self.yaml['selenium']['options'][browser]

    def get_images_path(self, img):
        return os.getcwd() + r'/data/img/' + img

    def get_jenkins_conf(self):
        return self.yaml['jenkins']

    def get_dingtalk_conf(self):
        return self.yaml['Dingtalk']
