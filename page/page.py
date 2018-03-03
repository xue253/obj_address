from page.page_search import Page_search
from page.page_delmsm import Page_delmsm
from page.page_deladd import Page_deladd
from page.page_address import Page_address
class Page(object):
    def __init__(self,driver):
        self.driver=driver

    def page_search(self):
        return Page_search(self.driver)

    def page_delmsm(self):
        return Page_delmsm(self.driver)

    def page_deladd(self):
        return Page_deladd(self.driver)

    def page_address(self):
        return Page_address(self.driver)
