#coding=utf-8
'''
Created on 2017-1-17

@author: xuls
'''
from aw.common.common import Common
from aw.const import Text
from time import sleep
from selenium.webdriver.common.by import By

class CarContrast(object):
    '''
    车型对比
    '''
    def __init__(self, driver):  
        self.driver = driver
        self.common = Common(self.driver)
    
    def launch(self):
        self.common.touchText(Text.HomePage.FAXIAN)
        self.common.touchText(Text.Faxian.CAR_CONTRAST)
        
    def homepage_isEmpty(self):
        #判断车型对比首页无已选车型
        if self.common.checkTextExist(Text.CarContrast.HOMEPAGE_EMPTY):
            return True
        else:
            return False
    
    def setHomepageEmpty(self):
        #清空车型对比首页已选车型
        if not self.homepage_isEmpty():
            sleep(2)
            self.common.touchText(Text.Common.EDIT)
            self.common.touchText(Text.Common.EMPTY)
            self.common.touchText(Text.Common.EMPTY)
            
    def addCars(self, brand, sub_brand, model):
        #添加车款
        self.common.touchText(Text.CarContrast.ADD_CAR)
        self.common.waitUntilPresent(By.ID, "brandname")
        self.common.touchSlideText(brand)
        self.common.waitUntilPresent(By.ID, "brandname")
        self.common.touchSlideText(sub_brand)
        self.common.waitUntilPresent(By.ID, "brandname")
        self.common.touchSlideText(model)
    
    def startContrast(self):
        self.common.touchText(Text.CarContrast.START_CONTRAST)
        
        