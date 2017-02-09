#coding=utf-8
'''
Created on 2016-12-19

@author: xuls
'''
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Common(object):
    def __init__(self, driver):  
        self.driver = driver
        
    #获得屏幕大小宽和高
    def getSize(self):
        x=self.driver.get_window_size()['width']
        y=self.driver.get_window_size()['height']
        return(x,y)
        
    #屏幕向下滑动
    def swipeDown(self,t=1000):
        l=Common.getSize(self)
        x1=int(l[0]*0.5) #x坐标
        y1=int(l[1]*0.25) #起始y坐标
        y2=int(l[1]*0.75) #终点y坐标
        self.driver.swipe(x1,y1,x1,y2,t)
     
    #屏幕向上滑动   
    def swipeUp(self,t=1000):
        l=Common.getSize(self)
        x1=int(l[0]*0.5) #x坐标
        y1=int(l[1]*0.75) #起始y坐标
        y2=int(l[1]*0.25) #终点y坐标
        self.driver.swipe(x1,y1,x1,y2,t)
        
    #屏幕向左滑动
    def swipeLeft(self,t=1000):
        l=Common.getSize(self)
        x1=int(l[0]*0.75) #起始x坐标
        y1=int(l[1]*0.5) #y坐标
        x2=int(l[1]*0.05) #终点x坐标
        self.driver.swipe(x1,y1,x2,y1,t)
        
    #屏幕向右滑动
    def swipeRight(self,t=1000):
        l=Common.getSize(self)
        x1=int(l[0]*0.05) #起始x坐标
        y1=int(l[1]*0.5) #y坐标
        x2=int(l[1]*0.75) #终点x坐标
        self.driver.swipe(x1,y1,x2,y1,t)
    #点击text   
    def touchText(self,text):
        element=WebDriverWait(self.driver, 15, 0.5).until(EC.presence_of_element_located((By.NAME,text)))
#         element=self.driver.find_element_by_name(text)
        element.click()
    
    #滑动点击text
    def touchSlideText(self,text):
        while not Common.checkTextExist(self, text):
            Common.swipeUp(self)
        element=self.driver.find_element_by_name(text)
        element.click()
        
    #点击id   
    def touchId(self,id_):
        element=WebDriverWait(self.driver, 15, 0.5).until(EC.presence_of_element_located((By.ID,id_)))
#         element=self.driver.find_element_by_id(id_)
        element.click()
    
    #滑动点击id
    def touchSlideId(self,id_):
        while not Common.checkIdExist(self, id_):
            Common.swipeUp(self)
        element=self.driver.find_element_by_id(id_)
        element.click()
    
    #判断text是否存在
    def checkTextExist(self,text):
        if self.driver.find_elements_by_name(text):
            return True
        else:
            return False
    
    #判断id是否存在
    def checkIdExist(self,id_):
        if self.driver.find_elements_by_id(id_):
            return True
        else:
            return False
        
    #页面包含两个文本编辑框，输入文本
    def inputText(self, param1,param2):
        textfields = self.driver.find_elements_by_class_name("android.widget.EditText")
        textfields[0].send_keys(param1)
        textfields[1].send_keys(param2)
        
    #返回
    def back(self):
        self.driver.keyevent('4')
        
    #多次返回
    def multiBack(self, times):
        while not times==0:
            Common.back(self)
            times=times-1;
            
    #等待元素出现
    def waitUntilPresent(self, by, value,timeout=30, poll_frequency=0.5):
        WebDriverWait(self.driver, timeout, poll_frequency).until(EC.presence_of_element_located((by,value)))
        
    #等待元素不再出现
    def waitUntilNotPresent(self,by, value,timeout=30, poll_frequency=0.5):
        WebDriverWait(self.driver, timeout, poll_frequency).until_not(EC.presence_of_element_located((by,value)))
