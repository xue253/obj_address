import time
from base.init_driver import Initdriver
from page.page import Page
import pytest
class Test_(object):
    def setup_class(self):
        self.driver=Initdriver()
        self.page=Page(self.driver).page_改变处()
        print("开始了！！！")

    def teardown_class(self):
        time.sleep(6)
        self.driver.quit()
        print("结束了")

    # @pytest.fixture(scope="class")
    # def start_search(self):
    #     self.page.click_search()
    #
    # @pytest.mark.usefixtures("start_search")
    # @pytest.mark.parametrize("text",["fuck","fuck you","shit"])
    # def test_001(self,text):
    #     self.page.input_search(text)
if __name__ == '__main__':
    pytest.main("-s test_example.py")
    # def __init__(self):__init__在pytest里面起冲突，失效

