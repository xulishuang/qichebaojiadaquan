#coding=utf-8
'''
Created on 2017-1-17

@author: xuls
'''
import os
import unittest
from aw.common.function import ImageFunction
PATH2=os.path.dirname(os.getcwd())

class AssertResult(unittest.TestCase):
    def __init__(self, driver):  
        self.driver = driver
        self.function =ImageFunction(self.driver)
        
    def assertByImage(self,id_,image,percent):
        element=self.driver.find_element_by_id(id_)
        screenshot = self.function.get_screenshot_by_element(element)
        screenshot.write_to_file(PATH2+"\\aw\\image\\actual", image)
        load = self.function.load_image(PATH2+"\\aw\\image\\expected\\"+image+".png")  
        result = screenshot.same_as(load, percent)  
        try:
            self.assertTrue(result)
        except Exception:
            self.fail(image+"页面显示不正确")
        finally:
            self.function.insert_img(image+".jpg")
        