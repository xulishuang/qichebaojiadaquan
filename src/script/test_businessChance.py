#coding=utf-8
'''
Created on 2017-1-11

@author: xuls
'''
import os
import unittest

from aw.common import variable
from aw.const import Text
from aw.models import appunit

from selenium.webdriver.common.by import By

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

PATH2=os.path.dirname(os.getcwd())

class BusinessChanceTest(appunit.AppTest):
    '''商机测试'''

    def test_enquiry(self):
        '''询价'''
        self.common.swipeUp()
        self.common.touchSlideText(Text.BranchName.Benz)
        self.common.touchSlideText(Text.BranchName.Benz_BRANCH1)
        
        self.common.waitUntilPresent(By.NAME, "询底价")
        
        self.common.touchSlideText("询底价")
        
        self.common.waitUntilPresent(By.CLASS_NAME, "android.widget.EditText")
        
        self.common.inputText(variable.Account.NAME, variable.Account.NUMBER)
        
        element=self.driver.find_element_by_id("content")
        image= self.function.get_screenshot_by_element(element)
        image.write_to_file(PATH2+"\\aw\\image\\actual", "image11")
        load = self.function.load_image(PATH2+"\\aw\image\expected\image11.png")  
        result = image.same_as(load, 0.85)  
        try:
            self.assertTrue(result)
        except Exception:
            self.fail("image11页面显示不正确")
        finally:
            self.function.insert_img("image11.jpg")
         
        self.common.touchText("提交")
        
        self.common.waitUntilPresent(By.NAME, "知道了")
        
        l=self.common.getSize()
        image= self.function.get_screenshot_by_custom_size(0, l[1]*0.25, l[0], l[1]*0.75)
        image.write_to_file(PATH2+"\\aw\\image\\actual", "image12")
        load = self.function.load_image(PATH2+"\\aw\image\expected\image12.png")  
        result = image.same_as(load, 0.95)  
        try:
            self.assertTrue(result)
        except Exception:
            self.fail("image12页面显示不正确")
        finally:
            self.function.insert_img("image12.jpg")
           
        self.common.touchText("知道了")
        
        self.common.waitUntilPresent(By.NAME, "询底价") 
        
        element=self.driver.find_element_by_id("content")
        image=self.function.get_screenshot_by_element(element)
        image.write_to_file(PATH2+"\\aw\\image\\actual", "image13")
        load = self.function.load_image(PATH2+"\\aw\image\expected\image13.png")  
        result = image.same_as(load, 0.95)    
        try:
            self.assertTrue(result)
        except Exception:
            self.fail("image13页面显示不正确")
        finally:
            self.function.insert_img("image13.jpg")
       
        self.common.multiBack(2);
        self.common.touchText(Text.HomePage.WODE)
        self.common.touchText("询价记录")
        
        self.common.waitUntilPresent(By.ID, "askprice_record_carname_txt")
#     
        image= self.function.get_screenshot_by_custom_size(10,219,710,379)   
        image.write_to_file(PATH2+"\\aw\\image\\actual", "image14")     
        load = self.function.load_image(PATH2+"\\aw\image\expected\image14.png")  
        result = image.same_as(load, 0.77)  
        try:
            self.assertTrue(result)
        except Exception:
            self.fail("image14页面显示不正确")
        finally:
            self.function.insert_img("image14.jpg")    
        
    def tearDown(self):       
        self.driver.quit()
        
if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(BusinessChanceTest("test_enquiry"))
    unittest.TextTestRunner().run(suite)