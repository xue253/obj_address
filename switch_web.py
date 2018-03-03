from appium import webdriver
import os
def Initdriver():
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5.1'
    desired_caps['deviceName'] = 'os.popen("adb devices").read().split()[4]'
    desired_caps['appPackage'] = 'com.android.contacts'
    desired_caps['appActivity'] = '.activities.PeopleActivity'
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
    return driver
