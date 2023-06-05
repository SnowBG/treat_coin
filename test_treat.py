from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from dotenv import load_dotenv
import os
import pdb
from time import sleep

load_dotenv()

u = os.environ['TREAT_U']
p = os.environ['TREAT_P']
url = f"https://{u}:{p}@treatcoin.com"


def get_driver(url):
    browser = Firefox()
    browser.get(url)
    wd = WebDriverWait(browser, 10)
    wd.until(EC.title_contains('TreatCoin'),'Seu tempo acabou!')
    return browser

def do_search(driver, tag_name, question):
    search = driver.find_element(By.NAME, tag_name)
    search.send_keys(question)
    search.send_keys(Keys.ENTER)
    return driver
    
driver = get_driver(url)
sleep(5)

assert driver.find_element(By.CSS_SELECTOR,'.intro-content > span:nth-child(3) > button:nth-child(1)').text == 'Join TreatCoin'

driver.close()