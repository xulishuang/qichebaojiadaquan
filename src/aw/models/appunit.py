#coding=utf-8
'''
Created on 2017-1-17

@author: xuls
'''
import os
import unittest
from appium import webdriver
# from time import sleep
from selenium.webdriver.common.by import By

from aw.common.common import Common
from aw.common.function import ImageFunction
from aw.common import variable

from aw.models.assertResult import AssertResult
from aw.models.carContrast import CarContrast
from aw.models.friendsToHelp import FriendsToHelp
from aw.models.sendTopic import SendTopic
from aw.models.wode import Wode


# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class AppTest(unittest.TestCase):
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
#         sleep(12)
        
#         self.driver.implicitly_wait(10)
        
        self.function = ImageFunction(self.driver)
        self.common = Common(self.driver)
        self.carContrast=CarContrast(self.driver)
        self.assertResult=AssertResult(self.driver)
        self.friendsToHelp=FriendsToHelp(self.driver)
        self.sendTopic=SendTopic(self.driver)
        self.wode=Wode(self.driver)
        
        self.common.waitUntilPresent(By.NAME, "热门推荐")
    
    def tearDown(self):       
        self.driver.quit()