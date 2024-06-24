# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By
from src.utils.pyselenium import PySelenium


def login(request):
    pyselenium = PySelenium()
    pyselenium.get('http://www.liuyanzu.tech/shopxo')
    go_login = (By.XPATH, '//a[text()="登录"]')
    user_name = (By.NAME, 'accounts')
    user_pawd = (By.NAME, 'pwd')
    user_verf = (By.NAME, 'verify')
    login_btn = (By.XPATH, '//button[text()="登录"]')
    verfy_ele = (By.XPATH, '//em[text()="hotshot0"]')

    pyselenium.click(go_login)
    pyselenium.send_keys(user_name, request.param[0])
    pyselenium.send_keys(user_pawd, request.param[1])
    pyselenium.send_keys(user_verf, request.param[2])
    pyselenium.click(login_btn)

    assert pyselenium.exist(verfy_ele)

