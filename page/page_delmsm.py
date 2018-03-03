from appium.webdriver.common.touch_action import TouchAction

from base.base import Base
import page,time
class Page_delmsm(Base):
    def __init__(self,driver):
        Base.__init__(self,driver)
        self.driver=driver

    def delete_msm(self):
        msm_list=self.find_elmlist(page.el_dx)
        for i in range (len(msm_list)):
            TouchAction(self.driver).long_press(msm_list[0],duration=2000).perform()
            self.click_elm(page.el_del)
            self.click_elm(page.el_but)
            time.sleep(1)