#!/usr/bin/env python3
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options 
import subprocess
import os

class Auther:

    CHROMEDRIVER_PATH = "/usr/bin/chromedriver"
    AUTH_URL = 'https://gauth.apps.gbraad.nl/'
    USERNAME = "username"
    SECRET = "your secret key"

    def __init__(self):
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')  # Last I checked this was necessary.
        self.driver = webdriver.Chrome(self.CHROMEDRIVER_PATH, chrome_options=options)

    def process(self):
        self.driver.get(self.AUTH_URL)
        self.prepare()
        self.add_account()
        self.get_code()
        return self.vng_code

    def prepare(self):
        editbtn = self.driver.find_element_by_id("edit")
        editbtn.click()
        addbtn = self.driver.find_element_by_id("addButton")
        addbtn.click()


    def add_account(self):
        name = self.driver.find_element_by_name('keyAccount')
        pawd = self.driver.find_element_by_name('keySecret')
        button = self.driver.find_element_by_id('addKeyButton')
        name.send_keys(self.USERNAME)
        pawd.send_keys(self.SECRET)
        button.click()

    def get_code(self):
        codes = self.driver.find_elements_by_tag_name("h3")
        vng_code = codes[-1]
        self.vng_code = vng_code.text


class Main:

    CURRENT_PATH = "/full/path/contain/this/code/" 
    LOGIN_PATH = "./login.sh"

    def __init__(self):
        key = Auther().process()
        print(key)
        os.chdir(self.CURRENT_PATH)
        subprocess.call(["sudo", '-b', self.LOGIN_PATH, key])
        print(os.getcwd())
        time.sleep(20)

Main()

# html = driver.page_source
# f = open("myhtml", "wt")
# f.write(html)
# f.close()

# search_box.send_keys("ChromeDriver")
# search_box.submit()
# time.sleep(5)
# driver.quit()
