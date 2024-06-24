# -*- coding: utf-8 -*-

import random
import pytest

from selenium.webdriver.common.by import By
from src.utils.pyselenium import PySelenium


# tb_user
class TestUser:
    driver = None
    new_user_count = f'6657测试{random.randint(10000,99999)}'
    new_user_phone = f'159{random.randint(10000000,99999999)}'
    new_user_newphone = new_user_count+'02'
    status_search = (By.XPATH, '//input[@placeholder="状态"]')
    username_search = (By.XPATH, '//input[@placeholder="用户名"]')
    phone_search = (By.XPATH, '//input[@placeholder="手机号"]')
    search_btn = (By.XPATH, '//span[text()="搜索"]')
    supermanager_manager = (By.XPATH, '//span[contains(text(), "汉堡")]')
    supermanager_manager_quit = (By.XPATH, '//li[contains(text(), "退出登录")]')

    def setup_class(self):
        self.driver = PySelenium()
        self.driver.get('http://www.liuyanzu.tech/task/manage')
        username = (By.XPATH, '//input[@class="el-input__inner" and @placeholder="username"]')
        password = (By.XPATH, '//input[@class="el-input__inner" and @placeholder="password"]')
        login_btn = (By.XPATH, '//*[text()="登录"]')
        login_res = (By.XPATH, '//p[text()="登录成功"]')

        self.driver.send_keys(username, 'hanbao')
        self.driver.send_keys(password, '123456')
        self.driver.click(login_btn)
        assert self.driver.exist(login_res)

    def setup_method(self):
        extension_btn = (By.XPATH, '//div[@class="collapse-btn"]')
        user_manager = (By.XPATH, '//span[text()="会员管理"]')
        self.driver.get('http://www.liuyanzu.tech/task/manage')
        self.driver.click(extension_btn)
        self.driver.click(user_manager)

    def teardown_method(self):
        self.driver.force_to_wait(3)

    def teardown_class(self):
        self.driver.click(self.supermanager_manager)
        self.driver.click(self.supermanager_manager_quit)
        self.driver.force_to_wait(3)

    # @pytest.mark.skip('跳过')
    def test_add_user(self):
        add_user_manager = (By.XPATH, '//span[text()="新增用户"]')
        add_user_name = (By.XPATH, '//label[text()="昵称"]/../div/div/input')
        add_user_phone = (By.XPATH, '//label[text()="手机"]/../div/div/input')
        add_user_img = (By.NAME, 'file')
        add_user_btn = (By.XPATH, '//div[@aria-label="新增"]/div[3]/span/button[2]/span')
        new_user_result = (By.XPATH, f'//div[text()="{self.new_user_count}"]')

        self.driver.click(add_user_manager)
        self.driver.send_keys(add_user_name, self.new_user_count)
        self.driver.send_keys(add_user_phone, self.new_user_phone)
        self.driver.execute_script('document.querySelector(".el-upload__input").style.display="block"')
        self.driver.send_keys(add_user_img, r'H:\py_home\pythonProject\Selenium-WEB自动化\cute.png')
        self.driver.force_to_wait(3)
        self.driver.click(add_user_btn)

        self.driver.send_keys(self.username_search, self.new_user_count)
        self.driver.click(self.search_btn)
        self.driver.force_to_wait(1)
        assert self.driver.exist(new_user_result)

    @pytest.mark.skip('跳过')
    def test_update_user(self):
        edit_btn = (By.XPATH, f'//div[text()="{self.new_user_count}"]/../../td[8]/div/button[2]/span')
        update_user_count = (By.XPATH, f'//div[text()="{self.new_user_newphone}"]')
        update_user_name = (By.XPATH, '//label[text()="昵称"]/../div/div/input')
        update_user_img = (By.NAME, 'file')
        update_user_btn = (By.XPATH, '//div[@aria-label="编辑"]/div[3]/span/button[2]/span')

        self.driver.send_keys(self.username_search, self.new_user_count)
        self.driver.click(self.search_btn)

        self.driver.click(edit_btn)
        self.driver.send_keys(update_user_name, self.new_user_newphone)
        self.driver.execute_script('document.querySelector(".el-upload__input").style.display="block"')
        self.driver.send_keys(update_user_img, r'H:\py_home\pythonProject\Selenium-WEB自动化\cute.png')
        self.driver.force_to_wait(1)
        self.driver.click(update_user_btn)

        self.driver.force_to_wait(1)
        assert self.driver.exist(update_user_count)

    @pytest.mark.parametrize('data', [['已冻结', 2], ['正常', 2], ['禁止发布任务', 1]])
    def test_search_user(self, data):
        status_manager = (By.XPATH, '//input[@placeholder="状态"]')
        status_manager_pick_status = (By.XPATH, f'//div[@class="el-scrollbar"]//span[contains(text(), "{data[0]}")]')
        user_result = (By.XPATH, '//tr[@class="el-table__row"]')

        self.driver.click(status_manager)
        self.driver.force_to_wait(1)
        self.driver.click(status_manager_pick_status)
        self.driver.send_keys(self.username_search, '7244测试')
        self.driver.click(self.search_btn)

        self.driver.force_to_wait(1)
        assert len(self.driver.exist(user_result)) == data[1]

    # @pytest.mark.skip('跳过')
    @pytest.mark.parametrize('data', [['冻结', '冻结'], ['禁止发布任务', '禁止发布任务'], ['恢复', '正常']])
    def test_change_status(self, data):
        user_name = (By.XPATH, f'//div[text()="{self.new_user_count}"]')
        user_change_status_btn = (By.XPATH, user_name[1]+f'/../../td[8]/div/button/span[text()="{data[0]}"]')
        user_status = (By.XPATH, user_name[1]+f'/../../td[7]/div/span[text()="{data[1]}"]')

        self.driver.send_keys(self.username_search, self.new_user_count)
        self.driver.click(self.search_btn)

        self.driver.click(user_change_status_btn)

        self.driver.force_to_wait(1)
        assert self.driver.text(user_status) == data[1]

