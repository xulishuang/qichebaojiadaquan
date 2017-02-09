#coding=utf-8
import os
import unittest
from appium import webdriver
from time import sleep

from aw.const import Text
from aw.const import ID
from aw.common import variable
from aw.common.function import ImageFunction

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class UserLoginTest(unittest.TestCase):
    '''汽车报价大全用户登录测试'''
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = variable.Device.PLATFORM_NAME
        desired_caps['platformVersion'] = variable.Device.PLATFORM_VERSION
        desired_caps['deviceName'] = variable.Device.DEVICE_NAME
#         desired_caps['app'] = PATH(variable.App.APP_PATH)
        desired_caps['appPackage'] = variable.App.APP_PACKAGE
        desired_caps['appActivity'] = variable.App.APP_ACTIVITY
        desired_caps['unicodeKeyboard'] = "True"
        desired_caps['resetKeyboard'] = "True"
#         desired_caps['automationName'] = "Selendroid"
        self.driver = webdriver.Remote(variable.AppiumConfig.EXECUTOR, desired_caps)
        sleep(10)
        
        self.function = ImageFunction(self.driver)

    def test_login_account(self):
        '''正常登录账户测试'''
        self.driver.find_element_by_name(Text.HomePage.WODE).click()
        if not "登录"==self.driver.find_element_by_id("com.yiche.price:id/title").get_attribute("text"):
            self.driver.find_element_by_id(ID.Wode.SETTINGS).click()
            self.driver.find_element_by_name(Text.Wode.LOGOUT).click()
        self.driver.find_element_by_name(Text.Wode.LOGIN).click()
        textfields = self.driver.find_elements_by_class_name("android.widget.EditText")
        textfields[0].send_keys(variable.Account.ACCOUNT)
        textfields[1].send_keys(variable.Account.PASSWORD)
        self.driver.find_element_by_class_name("android.widget.Button").click()
        sleep(10)
        
        try:
            self.assertTrue(True, self.driver.find_element_by_name(variable.Account.USERNAME))
        except Exception:
            print("程序出现异常了")
            self.fail("程序出现异常")
        finally:
            self.function.insert_img("user_login.jpg")
    
    def test_logout_account(self):
        '''正常退出账户测试'''
        self.driver.find_element_by_name(Text.HomePage.WODE).click()
        
        if "登录"==self.driver.find_element_by_id("com.yiche.price:id/title").get_attribute("text"):
            self.driver.find_element_by_name(Text.Wode.LOGIN).click()            
            textfields = self.driver.find_elements_by_class_name("android.widget.EditText")
            textfields[0].send_keys(variable.Account.ACCOUNT)
            textfields[1].send_keys(variable.Account.PASSWORD)
            self.driver.find_element_by_class_name("android.widget.Button").click()
            sleep(10)
        self.driver.find_element_by_id(ID.Wode.SETTINGS).click()
        self.driver.find_element_by_name(Text.Wode.LOGOUT).click()
        
        try:
            self.assertTrue(True, self.driver.find_element_by_name(Text.Wode.LOGIN))
        finally:
            self.function.insert_img("user_logout.jpg")

    def tearDown(self):       
        self.driver.quit()

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(UserLoginTest("test_login_account"))  
#     suite.addTest(UserLoginTest("test_logout_account")) 
    unittest.TextTestRunner().run(suite)