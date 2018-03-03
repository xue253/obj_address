from selenium.webdriver.common.by import By


"""
设置页搜索按钮
"""
el_s=(By.ID,"com.android.settings:id/search")
el_i=(By.ID,"android:id/search_src_text")
el_r=(By.CLASS_NAME,"android.widget.ImageButton")
"""
群删短信
"""
el_dx=(By.ID,"com.android.mms:id/from")
el_del=(By.ID,"com.android.mms:id/delete")
el_but=(By.ID,"android:id/button1")
"""
群删联系人
"""
el_peo=(By.ID,"com.android.contacts:id/cliv_name_textview")
el_dd =(By.CLASS_NAME,"android.widget.ImageButton")
el_wz =(By.XPATH,"//*[contains(@text,'删除')]")
el_qd =(By.ID,"android:id/button1")
"""
添加联系人
"""
el_add =(By.ID,'com.android.contacts:id/floating_action_button')
el_bdbc = (By.XPATH,'//*[contains(@text,"本地保存")]')
el_xm = (By.XPATH,'//*[contains(@text,"姓名")]')
el_dh = (By.XPATH,'//*[contains(@text,"电话")]')
el_tc = (By.CLASS_NAME,'android.widget.ImageButton')
