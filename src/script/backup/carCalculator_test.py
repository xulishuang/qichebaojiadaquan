#coding=utf-8
'''
Created on 2016-12-19

@author: xuls
'''

import os
import unittest
from appium import webdriver
from time import sleep

from aw.common import variable
from aw.const import Text
from aw.common.common import Common

from aw.common.function import ImageFunction

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class CarCalculatorTest(unittest.TestCase):
    '''购车计算器全款结果页'''
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
        self.common=Common(self.driver)
        
    def test_carCalculator(self):
        '''全款计算结果测试'''
        self.driver.find_element_by_name(Text.HomePage.FAXIAN).click()
        self.driver.find_element_by_name(Text.Faxian.CAR_CALCULATOR).click()
        self.driver.find_element_by_name(Text.CarCalculator.RESET).click()
        self.driver.find_element_by_name(Text.CarCalculator.SELECT_CARMODELS).click()
        sleep(5)        
        self.common.swipeUp()
        self.driver.find_element_by_name("奔驰").click()    
        sleep(5)
        self.driver.find_element_by_name("奔驰GLA级").click()
        sleep(5)
        self.driver.find_element_by_name("2016款 200 动感型").click()         
        try:
            self.assertTrue(True, self.driver.find_element_by_name("底价购车"))
        finally:
            self.function.insert_img("carCalculator.jpg")

    def tearDown(self):       
        self.driver.quit()

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(CarCalculatorTest("test_carCalculator"))
    unittest.TextTestRunner().run(suite)
    