"""
Company: Market Blitz
Author: Emerson Lara
Last Update: 2023-06-06

Description: This scprit was made to automate test of TreatCoin WebApp.

Libriaries/Dependencies:
- dotenv: to load the environment variables
- os: to recover the environment variables from Operation System
- time: to have a delay of the scripts' execution
- abc: to turn classes into abstract classes
- selenium: to control the browser on the automation

Credentials:
- .env: this file must be on the same folder that this script's file and must contain the environment variables.
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


"""
Loading and using the environment variabels.
This was necessary to do network login before the DOM is loaded.
"""

load_dotenv()
u = os.environ['TREAT_U']
p = os.environ['TREAT_P']

# Composing the URL with network user and password
url = f"https://{u}:{p}@treatcoin.com"


class SeleniumObject:
    """ Do the abstraction of the Selenium Objects. """
    def find_element(self, locator):
        """ Find a especific element on the DOM, according to the search conditions."""
        return self.webdriver.find_element(*locator)

    def find_elements(self, locator):
        """ Find a list of elements on the DOM, according to the search conditions."""
        return self.webdriver.find_elements(*locator)

class Page(ABC, SeleniumObject):
    """
    Abstract class to get the webdriver.
    """
    def __init__(self, webdriver,url=url):
        """ Constructor. """
        self.webdriver = webdriver
        self.url = url
        self._reflection()

    def open(self):
        """ Load and get the URL DOM as an object."""
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
    Steps to reach the Login page from start.
    Vars/DOM search:
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
    Steps to do Login.
    Vars/DOM search:
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


# Calling the methods

webdriver = Chrome()                # Calling the browser
login_elem = ReachLogin(webdriver)  # Instance of ReachLogin class passin the browser webdriver
# Open browser, call URL an reach login page
login_elem.open()
sleep(5)
login_elem.click_see_more()
sleep(3)
login_elem.click_login_link()
sleep(3)
# Fulfil user and password fields and click on Login button.
login = DoLogin(webdriver)          # Instance of DoLogin class passin the browser webdriver
login.fulfil_user()
login.fulfil_password()
sleep(3)
login.click_login()
sleep(15)
webdriver.close()
