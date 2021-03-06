#coding=utf-8
'''
Created on 2017-1-9

@author: xuls
'''
import os
import unittest

from aw.common import variable
from aw.models import appunit

from selenium.webdriver.common.by import By

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

PATH2=os.path.dirname(os.getcwd())

class SearchTest(appunit.AppTest):
    '''搜索测试'''
    
    def test_search1(self):
        '''搜索键盘功能：输入关键字，搜索结果包含车型、文章、帖子'''
        element=self.driver.find_element_by_id("searchEt")
        element.send_keys(variable.SearchFor.SEARCH1)
        
        self.common.waitUntilPresent(By.ID, "brand_name_tv")
        
        element=self.driver.find_element_by_id("content")
        image=self.function.get_screenshot_by_element(element)
        image.write_to_file(PATH2+"\\aw\\image\\actual", "image01")
        load = self.function.load_image(PATH2+"\\aw\image\expected\image01.png")  
        result = image.same_as(load, 0.90)  
        try:
            self.assertTrue(result)
        except Exception:
            self.fail("image01页面显示不正确")
        finally:
            self.function.insert_img("image01.jpg")
        
        element=self.driver.find_element_by_id("brand_name_tv")
        element.click()
        
        self.common.waitUntilPresent(By.ID, "brand_name_tv")
        
        element=self.driver.find_element_by_id("content") 
        image=self.function.get_screenshot_by_element(element)
        image.write_to_file(PATH2+"\\aw\\image\\actual", "image02")
        load = self.function.load_image(PATH2+"\\aw\image\expected\image02.png")  
        result = image.same_as(load, 0.85) 
        try:
            self.assertTrue(result)
        except Exception:
            self.fail("image02页面显示不正确")
        finally:
            self.function.insert_img("image02.jpg")
        
    def test_search2(self):
        '''搜索键盘功能：输入关键字，搜索结果不包含车型，包含文章、帖子'''
        element=self.driver.find_element_by_id("searchEt")
        element.send_keys(variable.SearchFor.SEARCH2)
        
        self.common.waitUntilPresent(By.ID, "brand_name_tv")
        element=self.driver.find_element_by_id("content")
        image=self.function.get_screenshot_by_element(element)
        image.write_to_file(PATH2+"\\aw\\image\\actual", "image03")
        load = self.function.load_image(PATH2+"\\aw\image\expected\image03.png")  
        result = image.same_as(load, 0.95)  
        try:
            self.assertTrue(result)
        except Exception:
            self.fail("image03页面显示不正确")
        finally:
            self.function.insert_img("image03.jpg")
         
        element=self.driver.find_element_by_id("brand_name_tv")
        element.click()
        
        self.common.waitUntilPresent(By.ID, "news_title")
        
        element=self.driver.find_element_by_id("indicator")
        image=self.function.get_screenshot_by_element(element)
        image.write_to_file(PATH2+"\\aw\\image\\actual", "image04")
        load = self.function.load_image(PATH2+"\\aw\image\expected\image04.png")  
        result = image.same_as(load, 1.0)  
        try:
            self.assertTrue(result)
        except Exception:
            self.fail("image04页面显示不正确")
        finally:
            self.function.insert_img("image04.jpg")
    
    def test_search3(self):
        '''搜索键盘功能：输入关键字，搜索结果不包含车型、文章，包含帖子'''
        element=self.driver.find_element_by_id("searchEt")
        element.send_keys(variable.SearchFor.SEARCH3)
        
        self.common.waitUntilPresent(By.ID, "brand_name_tv")
        element=self.driver.find_element_by_id("content")
        image=self.function.get_screenshot_by_element(element)
        image.write_to_file(PATH2+"\\aw\\image\\actual", "image05")
        load = self.function.load_image(PATH2+"\\aw\image\expected\image05.png")  
        result = image.same_as(load, 0.95)  
        try:
            self.assertTrue(result)
        except Exception:
            self.fail("image05页面显示不正确")
        finally:
            self.function.insert_img("image05.jpg")
          
        element=self.driver.find_element_by_id("brand_name_tv")
        element.click()
        
        self.common.waitUntilPresent(By.ID, "news_comment_count")
        
        element=self.driver.find_element_by_id("indicator")
        image=self.function.get_screenshot_by_element(element)
        image.write_to_file(PATH2+"\\aw\\image\\actual", "image06")
        load = self.function.load_image(PATH2+"\\aw\image\expected\image06.png")  
        result = image.same_as(load, 1.0)  
        try:
            self.assertTrue(result)
        except Exception:
            self.fail("image06页面显示不正确")
        finally:
            self.function.insert_img("image06.jpg")
            
    def test_search4(self):
        '''搜索键盘功能：输入关键字，搜索结果不包含车型、文章、帖子'''
        element=self.driver.find_element_by_id("searchEt")
        element.send_keys(variable.SearchFor.SEARCH4)
        
        self.common.waitUntilPresent(By.ID, "brand_name_tv")
        element=self.driver.find_element_by_id("content")
        image=self.function.get_screenshot_by_element(element)
        image.write_to_file(PATH2+"\\aw\\image\\actual", "image07")
        image.write_to_file(PATH2+"\\aw\\image\\actual", "image07")
        load = self.function.load_image(PATH2+"\\aw\image\expected\image07.png")  
        result = image.same_as(load, 0.95)  
        try:
            self.assertTrue(result)
        except Exception:
            self.fail("image07页面显示不正确")
        finally:
            self.function.insert_img("image07.jpg")
          
        element=self.driver.find_element_by_id("brand_name_tv")
        element.click()
        
        self.common.waitUntilPresent(By.NAME, "暂无数据")
        
        element=self.driver.find_element_by_id("content")
        image=self.function.get_screenshot_by_element(element)
        image.write_to_file(PATH2+"\\aw\\image\\actual", "image08")
        load = self.function.load_image(PATH2+"\\aw\image\expected\image08.png")  
        result = image.same_as(load, 0.95)  
        try:
            self.assertTrue(result)
        except Exception:
            self.fail("image08页面显示不正确")
        finally:
            self.function.insert_img("image08.jpg")
            
    def test_search5(self):
        '''搜索框下的联想词跳转'''
        self.common.touchId("searchEt")
        if self.common.checkTextExist("清空"):
            self.common.touchText("清空")
        self.common.inputTextById("searchEt", "奥迪")
        self.common.waitUntilPresent(By.ID, "brand_name_tv")
        self.assertResult.assertByImage("content", "image09", 0.90)
        
        self.common.touchText("奥迪A4L")
        self.common.waitUntilPresent(By.NAME, "询底价")
        self.assertResult.assertByImage("content", "image0a", 0.85)
        
        self.common.back()
        self.common.touchText("取消")
        self.common.touchId("searchEt")
        self.assertTrue(self.common.checkTextExist("奥迪A4L"))
        self.assertResult.assertByImage("content", "image0b", 0.85)
        
    def test_search6(self):
        '''搜索页热门车型'''
        self.common.touchId("searchEt")
        if self.common.checkTextExist("清空"):
            self.common.touchText("清空")
        self.assertResult.assertByImage("content", "image0c", 0.90)
        
        self.common.touchText("哈弗H6")
        self.common.waitUntilPresent(By.NAME, "询底价")
        self.assertResult.assertByImage("content", "image0d", 0.85)
        
        self.common.back()
        self.common.touchText("清空")
        self.assertResult.assertByImage("content", "image0e", 0.90)
        
        self.common.touchText("取消")
        self.assertResult.assertByImage("homepage_quick_entrance_gridview", "image0f", 0.90)        
        
if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(SearchTest("test_search1"))   
    suite.addTest(SearchTest("test_search2")) 
    suite.addTest(SearchTest("test_search3"))
    suite.addTest(SearchTest("test_search4"))   
    suite.addTest(SearchTest("test_search5"))
    suite.addTest(SearchTest("test_search6"))
    unittest.TextTestRunner().run(suite)