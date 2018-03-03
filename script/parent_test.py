
from base.init_driver import Initdriver
from appium import webdriver
driver=Initdriver()
elm1 = driver.find_element_by_xpath("//*[contains(@text,'119')]/..")
elm2 = driver.find_element_by_xpath("//*[contains(@text,'#')]")
elm3 = driver.find_element_by_xpath("//*[contains(@text,'傻逼')]")


print(elm1.location)
# y1=elm1.location.get('y')
# print(elm2.location)
# y2=elm2.location.get('y')
# print(elm3.location)
# y3=elm3.location.get('y')
# print(type(y1))
# print(y1)
# print(y2)
# if y2 < y3 <y1:
#     print(True)
#
#
#
#
#
#
# num1=10
# num2=20
# if num1 < num2:
#     print(True)