import time,sys,os
sys.path.append(os.path.dirname(r'C:\Users\XHY\PycharmProjects\PO_object\base'))
sys.path.append(os.path.dirname(r'C:\Users\XHY\PycharmProjects\PO_object\page'))
from base.read_yaml import r_ymal
from base.init_driver import Initdriver
from page.page import Page
import pytest
def read_test_data():
    data_first=r_ymal('data_search.yaml')
    data_secend = data_first.get('test_search')
    data_list = []
    for k in data_secend.keys():
        data_list.append((k, data_secend.get(k).get('text'), data_secend.get(k).get('expect')))
    return data_list
class Test_search(object):
    def setup_class(self):
        self.driver=Initdriver()
        self.page=Page(self.driver).page_search()
        print("开始了！！！")

    def teardown_class(self):
        self.page.out_search()
        time.sleep(6)
        self.driver.quit()
        print("结束了")

    @pytest.fixture(scope="class")
    def start_search(self):
        self.page.click_search()

    @pytest.mark.usefixtures("start_search")
    @pytest.mark.parametrize("test_no,text,expect",read_test_data())
    def test_001(self,test_no,text,expect):
        self.page.input_search(text)
        self.driver.get_screenshot_as_file('../picture/%s.png'%test_no)
        time.sleep(1)
        text_ml=self.driver.page_source
        assert expect in text_ml
