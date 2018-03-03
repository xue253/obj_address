from base.base import Base
import page
class Page_(Base):
    def __init__(self,driver):
        Base.__init__(self,driver)
        self.driver=driver


