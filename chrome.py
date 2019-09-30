# -*- coding: utf-8 -*-
# @Time    : 2019/9/29 16:06
# @Author  : Coderfly
# @Email   : coderflying@163.com
# @File    : chrome.py
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from constants import *

class Chrome(object):

    def __init__(self,chrome_driver,mitm_proxy="127.0.0.1:8080"):
        self.timer = 0
        self.driver = self.init_driver(chrome_driver,mitm_proxy)

    def init_driver(self,chrome_driver,mitm_proxy):
        chrome_options = Options()
        chrome_options.add_argument("--disable-gpu")  # 禁用gpu
        chrome_options.add_argument("--headless")  # 无界面
        chrome_options.add_argument(f"--proxy-server={mitm_proxy}")
        chrome_options.add_argument(
            '--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36')
        driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)
        driver.get("https://www.iesdouyin.com/share/user/58958068057")
        return driver

    def reload(self):
        self.timer = 0
        self.driver.refresh()


    def watch(self):
        while True:
            if self.timer >= reload_times:
                self.reload()
            self.timer += 1
            time.sleep(1)

    def __del__(self):
        self.driver.close()
        self.driver.quit()
        del self



if __name__ == '__main__':
    chrome = Chrome("chromedriver.exe",mitm_proxy=f'{mitmproxy_host}:{mitmproxy_port}')
    chrome.watch()
