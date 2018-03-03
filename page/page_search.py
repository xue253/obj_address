from base.base import Base
import page

class Page_search(Base):
    def __init__(self, driver):
        Base.__init__(self, driver)
        self.driver = driver

    def click_search(self):
        self.click_elm(page.el_s)

    def input_search(self,text):
        self.sendkey_elm(page.el_i,text)

    def out_search(self):
        self.click_elm(page.el_r)
