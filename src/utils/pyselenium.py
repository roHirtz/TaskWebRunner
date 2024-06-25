# -*- coding: utf-8 -*-

import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from src.utils.config import Config
from src.utils.logger import log


class PySelenium:
    __instance = None
    __driver = None
    __timeout = None

    def __new__(cls, browser='chrome', timeout=30):
        if not cls.__instance:
            cls.__timeout = timeout
            cls.__instance = super().__new__(cls)

            driver_path = Config().get_driver_path()
            options = cls.__get_options(browser)
            services = cls.__get_services(browser, driver_path)
            cls.__driver = getattr(cls, browser.lower())(options, services)

        return cls.__instance

    def __init__(self):
        pass

    @classmethod
    def __get_options(cls, browser):
        if browser == 'chrome':
            from selenium.webdriver import ChromeOptions as Options
        if browser == 'edge':
            from selenium.webdriver import FirefoxOptions as Options
        if browser == 'firefox':
            from selenium.webdriver import EdgeOptions as Options
        else:
            from selenium.webdriver import ChromeOptions as Options

        # 参数配置
        options = Options()
        for option in Config().get_selenium_options(browser)['add_argument']:
            options.add_argument(option)

        return options

    @classmethod
    def __get_services(cls, browser, driver_path):
        if browser == 'chrome':
            from selenium.webdriver import ChromeService as Services
        if browser == 'edge':
            from selenium.webdriver import FirefoxService as Services
        if browser == 'firefox':
            from selenium.webdriver import EdgeService as Services
        else:
            from selenium.webdriver import ChromeService as Services

        return Services(executable_path=driver_path)

    @classmethod
    def chrome(cls, options, services):
        return webdriver.Chrome(options=options, service=services)

    @classmethod
    def edge(cls, options, services):
        return webdriver.Edge(options=options, service=services)

    @classmethod
    def firefox(cls, options, services):
        return webdriver.Firefox(options=options, service=services)

    @log
    def get_origin_driver(self):
        return self.__driver

    @log
    def get(self, url):
        self.__driver.get(url)

    def __find_element(self, Locator) -> WebElement:
        if not isinstance(Locator, tuple):
            raise Exception('输入的格式必须为(By.xx, value)')
        return WebDriverWait(self.__driver, self.__timeout).until(lambda s: s.find_element(*Locator))

    def __find_elements(self, Locator) -> WebElement:
        if not isinstance(Locator, tuple):
            raise Exception('输入的格式必须为(By.xx, value)')
        return WebDriverWait(self.__driver, self.__timeout).until(lambda s: s.find_elements(*Locator))

    @log
    def click(self, Locator):
        self.__find_element(Locator).click()

    @log
    def send_keys(self, Locator, content):
        self.clear(Locator)
        self.__find_element(Locator).send_keys(content)

    @log
    def exist(self, Locator):
        """
            判断元素是否存在, list
        """
        return self.__find_elements(Locator)

    @log
    def clear(self, Locator):
        self.__find_element(Locator).clear()

    @log
    def switch_to_alert(self):
        return self.__driver.switch_to.alert

    @log
    def switch_to_frame(self, Locator):
        frame = self.__find_element(Locator)
        self.__driver.switch_to.frame(frame)

    @log
    def switch_to_default_frame(self):
        self.__driver.switch_to.default_content()

    @log
    def switch_to_new_window(self):
        windows = self.__driver.window_handles
        self.__driver.switch_to.window(windows[-1])

    @log
    def move_to_element(self, Locator):
        from selenium.webdriver.common.action_chains import ActionChains
        ActionChains(self.__driver).move_to_element(self.__find_element(Locator)).perform()

    @log
    def double_click(self, Locator):
        from selenium.webdriver.common.action_chains import ActionChains
        ActionChains(self.__driver).double_click(self.__find_element(Locator)).perform()

    @log
    def get_attribute(self, Locator, attribute):
        return self.__find_element(Locator).get_attribute(attribute)

    @log
    def text(self, Locator):
        return self.__find_element(Locator).text

    @log
    def execute_script(self, script, *args):
        self.__driver.execute_script(script, *args)

    @log
    def scroll_to_element(self, Locator):
        """
            页面滑动到某个元素使可用
        """
        self.__driver.execute_script("arguments[0].scrollIntoView()", self.__find_element(Locator))

    @log
    def add_cookie(self, cookie):
        self.__driver.add_cookie(cookie)

    @log
    def delete_all_cookies(self):
        self.__driver.delete_all_cookies()

    @log
    def refresh(self):
        self.__driver.refresh()

    @log
    def max_window(self):
        self.__driver.maximize_window()

    @log
    def save_screenshot(self, file_path):
        """
            屏幕截图png
        """
        self.__driver.save_screenshot(file_path)

    @log
    def wait(self, timeout=10):
        """
            隐式等待
        """
        self.__driver.implicitly_wait(timeout)

    @log
    def force_to_wait(self, timeout=10):
        """time.sleep"""
        time.sleep(timeout)

    @log
    def close(self):
        self.__driver.close()

    @log
    def quit(self):
        self.__driver.quit()
