from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
class Base(object):
    def __init__(self,driver):
        self.driver=driver

    def find_elm(self,loc,timeout=10,poll=0.1):
        return WebDriverWait(self.driver,timeout,poll).until(lambda x:x.find_element(*loc))

    def click_elm(self,loc):
        self.find_elm(loc).click()

    def sendkey_elm(self,loc,text):
        self.find_elm(loc).clear()
        self.find_elm(loc).send_keys(text)

    def find_elmlist(self,loc,timeout=10,poll=0.1):
        return WebDriverWait(self.driver,timeout,poll).until(lambda x:x.find_elements(*loc))




