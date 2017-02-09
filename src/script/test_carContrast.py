#coding=utf-8
'''
Created on 2017-1-16

@author: xuls
'''
import unittest
from aw.models import appunit
from aw.const import Text
from selenium.webdriver.common.by import By

class CarContrastTest(appunit.AppTest):
    '''车型对比测试'''
    def test_carContrast(self):
        '''开始对比'''
        #打开车型对比
        self.carContrast.launch()
        #清空已选择的车款
        self.carContrast.setHomepageEmpty()
        #添加两个对比车款
        self.carContrast.addCars(Text.BranchName.VW, Text.BranchName.VW_BRANCH1, Text.BranchName.VW_MODEL1)
        self.carContrast.addCars(Text.BranchName.Audi, Text.BranchName.Audi_BRANCH1, Text.BranchName.Audi_MODEL1)
        #判断添加车款界面是否正确
        self.assertResult.assertByImage("content", "image21", 0.80)
        #点击开始对比 
        self.carContrast.startContrast()
        self.common.waitUntilPresent(By.ID, "parameter_cartypelist")
        #判断对比结果是否正确
        self.assertResult.assertByImage("content", "image22", 0.94)
#         
if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(CarContrastTest("test_carContrast"))
    unittest.TextTestRunner().run(suite)