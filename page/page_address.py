from base.base import Base
import page
class Page_address(Base):
    def __init__(self,driver):
        Base.__init__(self,driver)
        self.driver=driver

    def click_address(self):
        self.click_elm(page.el_add)

    def click_bdbc(self):
        self.click_elm(page.el_bdbc)

    def send_message(self,name,phone):
        self.sendkey_elm(page.el_xm,text=name)
        self.sendkey_elm(page.el_dh,text=phone)

    def out_address(self):
        self.click_elm(page.el_tc)

    def out_keyevent(self):
        self.driver.keyevent(4)