import time
import allure
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

    def save_screen(self):
        screen_img = "./screen/%d.png" % int(time.time())
        self.driver.get_screenshot_as_file(screen_img)
        with open(screen_img,"rb") as f:
            allure.attach("截图",f.read(),allure.attach_type.PNG)





