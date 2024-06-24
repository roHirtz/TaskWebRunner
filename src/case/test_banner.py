# -*- coding: utf-8 -*-

import random
import pytest

from selenium.webdriver.common.by import By
from src.utils.pyselenium import PySelenium


# tb_system_banner
class TestBanner:
    driver = None
    new_banner_title_count = f'6657测试{random.randint(10000,99999)}'
    new_banner_title_newcount = '02'
    search = (By.XPATH, '//input[@class="el-input__inner" and @placeholder="标题"]')
    search_btn = (By.XPATH, '//*[text()="搜索"]')
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
        """每测试用例前"""
        extension_btn = (By.XPATH, '//div[@class="collapse-btn"]')
        banner_manager = (By.XPATH, '//span[text()="轮播图管理"]')
        self.driver.get('http://www.liuyanzu.tech/task/manage')
        self.driver.click(extension_btn)
        self.driver.click(banner_manager)

    def teardown_method(self):
        self.driver.force_to_wait(3)

    def teardown_class(self):
        self.driver.click(self.supermanager_manager)
        self.driver.click(self.supermanager_manager_quit)
        self.driver.force_to_wait(3)

    # @pytest.mark.skip('跳过')
    def test_add_banner(self):
        """新增轮播图"""
        new_banner = (By.XPATH, '//*[text()="新增Banner"]')
        new_banner_title = (By.XPATH, '//*[@id="app"]/div/div[3]/div[2]/div/div[4]/div/div[2]/form/div[1]/div/div/input')
        new_banner_uploadimg = (By.NAME, 'file')
        new_banner_outsidelink = (By.XPATH, '//*[@id="app"]/div/div[3]/div[2]/div/div[4]/div/div[2]/form/div[4]/div/div/input')
        new_banner_submit = (By.XPATH, '//*[@id="app"]/div/div[3]/div[2]/div/div[4]/div/div[3]/span/button[2]')
        new_banner_result = (By.XPATH, f'//div[text()="{self.new_banner_title_count}"]')

        self.driver.click(new_banner)
        self.driver.send_keys(new_banner_title, self.new_banner_title_count)
        self.driver.execute_script('document.querySelector(".el-upload__input").style.display="block"')
        self.driver.send_keys(new_banner_uploadimg, r'H:\py_home\pythonProject\Selenium-WEB自动化\cute.png')
        self.driver.send_keys(new_banner_outsidelink, 'https://www.douyu.com/6657')
        self.driver.force_to_wait(3)
        self.driver.click(new_banner_submit)

        self.driver.send_keys(self.search, self.new_banner_title_count)
        self.driver.click(self.search_btn)

        self.driver.force_to_wait(1)
        assert self.driver.exist(new_banner_result)

    # @pytest.mark.skip('跳过')
    def test_update_banner(self):
        """更新轮播图"""
        new_banner_count = self.new_banner_title_count+self.new_banner_title_newcount
        new_banner_title = (By.XPATH, '//*[@id="app"]/div/div[3]/div[2]/div/div[3]/div/div[2]/form/div[1]/div/div/input')
        new_banner_result_editor = (By.XPATH, f'//div[text()="{self.new_banner_title_count}"]/../../td[6]/div/button[1]')
        new_banner_result_editor_submit = (By.XPATH, '//*[@id="app"]/div/div[3]/div[2]/div/div[3]/div/div[3]/span/button[2]')
        new_banner_result = (By.XPATH, f'//div[text()="{new_banner_count}"]')

        self.driver.send_keys(self.search, self.new_banner_title_count)
        self.driver.click(self.search_btn)

        self.driver.click(new_banner_result_editor)
        self.driver.send_keys(new_banner_title, new_banner_count)
        self.driver.force_to_wait(1)
        self.driver.click(new_banner_result_editor_submit)

        self.driver.force_to_wait(1)
        assert self.driver.exist(new_banner_result)

    # @pytest.mark.skip('跳过')
    @pytest.mark.parametrize('data', [['禁用', '停用'], ['启用', '启用']])
    def test_disable_enable_banner(self, data):
        """禁用/启用轮播图"""
        new_banner_count = self.new_banner_title_count+self.new_banner_title_newcount
        new_banner_result_disable = (By.XPATH, f'//div[text()="{new_banner_count}"]/../../td[6]/div/button[2]/span[text()="{data[0]}"]')
        new_banner_disable_result = (By.XPATH, f'//div[text()="{new_banner_count}"]/../../td[5]/div/span')

        self.driver.send_keys(self.search, new_banner_count)
        self.driver.click(self.search_btn)
        self.driver.click(new_banner_result_disable)

        self.driver.force_to_wait(1)
        assert self.driver.text(new_banner_disable_result) == f"{data[1]}"

    # @pytest.mark.skip('跳过')
    @pytest.mark.parametrize('data', [{"启用": 2}, {"禁用": 1}])
    def test_status_select_banner(self, data):
        """状态查询"""
        search_status_manager = (By.XPATH, '//input[@placeholder="状态"]')
        rows_result_count = (By.XPATH, '//tr[@class="el-table__row"]')
        system_result_count = (By.XPATH, '//span[@class="el-pagination__total"]')
        for k, v in data.items():
            search_status = (By.XPATH, f'//li[contains(@class, "el-select-dropdown__item")]/span[text()="{k}"]')
            self.driver.click(search_status_manager)
            self.driver.force_to_wait(1)
            self.driver.click(search_status)
            self.driver.send_keys(self.search, '7244')
            self.driver.click(self.search_btn)

            self.driver.force_to_wait(3)
            assert len(self.driver.exist(rows_result_count)) == v
            assert str(v) in self.driver.text(system_result_count)
