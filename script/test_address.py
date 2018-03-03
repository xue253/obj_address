import time,sys,os,pytest
# sys.path.append(os.path.dirname(r'C:\Users\XHY\PycharmProjects\PO_object\base'))
# sys.path.append(os.path.dirname(r'C:\Users\XHY\PycharmProjects\PO_object\page'))
sys.path.append(os.getcwd())
from base.init_driver import Initdriver
from page.page import Page
from base.read_yaml import r_ymal
def read_test_data():
    data_first=r_ymal('data_address.yaml')
    # print(data_first)
    data_secend = data_first.get('test_search')
    data_list = []
    for k in data_secend.keys():
        data_list.append((k, data_secend.get(k).get('name'), data_secend.get(k).get('phone'),data_secend.get(k).get('expect')))
    # print(data_list)
    return data_list

class Test_address(object):
    def setup_class(self):
        self.driver=Initdriver()
        self.page=Page(self.driver).page_address()
        print("开始了！！！")

    def teardown_class(self):
        time.sleep(6)
        self.driver.quit()
        print("结束了！！！")

    @pytest.fixture(scope="function")
    def start_address(self):
        self.page.click_address()

    @pytest.fixture(scope="class")
    def click_bdbc(self):
        self.page.click_bdbc()

    @pytest.mark.parametrize("expect", ["新增联系人"])
    def test_001(self,expect):
        self.page.click_address()
        self.page.click_bdbc()
        time.sleep(1)
        text_list=self.driver.page_source
        assert expect in text_list

    @pytest.mark.parametrize("expect", ["所有联系人"])
    def test_002(self,expect):
        self.page.out_address()
        time.sleep(1)
        text_list=self.driver.page_source
        assert expect in text_list

    @pytest.mark.usefixtures("start_address")
    @pytest.mark.parametrize("test_no,name,phone,expect",read_test_data())
    def test_003(self,test_no,name,phone,expect):
        print(test_no,name,phone,expect)
        self.page.send_message(name, phone)
        self.page.out_address()
        time.sleep(5)
        if name=="" and phone =="":
            pass
        else:
            self.page.out_keyevent()
        time.sleep(1)
        text_list=self.driver.page_source
        assert expect in text_list






        # if name:
        #     if phone:
        #         self.page.send_message(name,phone)
        #         self.page.out_address()
        #         time.sleep(5)
        #         self.driver.keyevent(4)
        #         time.sleep(1)
        #         text_list=self.driver.page_source
        #         assert expect in text_list
        #     else:
        #         phone=""
        #         self.page.send_message(name,phone)
        #         self.page.out_address()
        #         time.sleep(5)
        #         self.driver.keyevent(4)
        #         time.sleep(1)
        #         text_list=self.driver.page_source
        #         assert expect in text_list
        # else:
        #     name=""
        #     if phone:
        #         self.page.send_message(name,phone)
        #         self.page.out_address()
        #         time.sleep(5)
        #         self.driver.keyevent(4)
        #         time.sleep(1)
        #         text_list=self.driver.page_source
        #         assert expect in text_list
        #     else:
        #         phone=""
        #         self.page.send_message(name,phone)
        #         self.page.out_address()
        #         time.sleep(5)
        #         text_list=self.driver.page_source
        #         assert expect in text_list




