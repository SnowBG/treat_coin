"""
This scprit was made to automate test of TreatCoin webapp.


"""


from dotenv import load_dotenv
import os
from time import sleep
from abc import ABC

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


load_dotenv()
u = os.environ['TREAT_U']
p = os.environ['TREAT_P']

url = f"https://{u}:{p}@treatcoin.com"


class SeleniumObject:
    def find_element(self, locator):
        return self.webdriver.find_element(*locator)

    def find_elements(self, locator):
        return self.webdriver.find_elements(*locator)

class Page(ABC, SeleniumObject):
    """
    Abstract class to get the webdriver.
    """
    def __init__(self, webdriver,url=url):
        self.webdriver = webdriver
        self.url = url
        self._reflection()

    def open(self):
        self.webdriver.get(url)

    def _reflection(self):
        for atribute in dir(self):
            real_atribute = getaatr(self, atribute)
            if isinstance(real_atribute, PageElement):
                real_atribute.webdriver = self.webdriver

class PageElement(Page, ABC, SeleniumObject):
    def __init__(self, webdriver=None):
        self.webdriver = webdriver

class ReachLogin(PageElement):
    """
    See More = CLASS_NAME, "see-more-link"
    Sidebar menu button = ID, "menu-bar"
    Log in = CLASS_NAME, "login-logout-button"
    """
    selenium_object = SeleniumObject()
    see_more = (By.CLASS_NAME, "see-more-link")
    sidebar_btn = (By.ID, "menu-bar")
    login_lnk = (By.CLASS_NAME, "login-button-styled")
    def click_see_more(self):
        self.find_element(self.see_more).click()
    
    def click_sidebar_btn(self):
        self.find_element(self.sidebar_btn).click()

    def click_login_link(self):
        self.find_element(self.login_lnk).click()

class DoLogin(PageElement):
    """
    Username = ID, "username"
    Password = ID, "password"
    Log in button = CLASS_NAME, "login-button"
    """
    user = (By.ID, "username")
    pwd = (By.ID, "password")
    login_btn = (By.CLASS_NAME, "login-button")
    
    def fulfil_user(self):
        self.find_element(self.user).send_keys('admin')

    def fulfil_password(self):
        self.find_element(self.pwd).send_keys('admin')
    
    def click_login(self):
        self.find_element(self.login_btn).click()

webdriver = Chrome()
login_elem = ReachLogin(webdriver)
login_elem.open()
sleep(5)
login_elem.click_see_more()
sleep(3)
login_elem.click_login_link()
sleep(3)
login = DoLogin(webdriver)
login.fulfil_user()
login.fulfil_password()
sleep(3)
login.click_login()
sleep(15)
# webdriver.close()
