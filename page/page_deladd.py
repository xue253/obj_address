from appium.webdriver.common.touch_action import TouchAction

from base.base import Base
import page,time
class Page_deladd(Base):
    def __init__(self,driver):
        Base.__init__(self,driver)
        self.driver=driver

    def delete_address(self):
        add_list=self.find_elmlist(page.el_peo)
        for i in range (len(add_list)):
            add_list[0].click()
            self.click_elm(page.el_dd)
            self.click_elm(page.el_wz)
            self.click_elm(page.el_qd)
            time.sleep(1)