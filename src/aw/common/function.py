#coding=utf-8
'''
Created on 2017-1-5

@author: xuls
'''
import os    
import tempfile  
import shutil   
from PIL import Image
# from functools import reduce

import time 

PATH2=os.path.dirname(os.getcwd())  
PATH = lambda p: os.path.abspath(p)  
TEMP_FILE = PATH(tempfile.gettempdir() + "/temp_screen.png")  
  
class ImageFunction(object):  
    def __init__(self, driver):  
        self.driver = driver
    
    def insert_img(self, file_name):
        #截图整个屏幕,用于记录结果，存放于report/image路径下
        base_dir=os.path.dirname(os.path.dirname(__file__))
        base_dir=str(base_dir)
        base_dir=base_dir.replace('\\', '/')
        base=base_dir.split('/aw')[0]
        now=time.strftime("%Y-%m_%d %H_%M_%S")
        file_path=base+"/report/image/"+now+file_name
        self.driver.get_screenshot_as_file(file_path)  
  
    def get_screenshot_by_element(self, element):  
        #先截取整个屏幕，存储至系统临时目录下  
        self.driver.get_screenshot_as_file(TEMP_FILE)  
  
        #获取元素bounds  
        location = element.location  
        size = element.size  
        box = (location["x"], location["y"], location["x"] + size["width"], location["y"] + size["height"])  
  
        #截取图片  
        image = Image.open(TEMP_FILE)  
        newImage = image.crop(box)  
        newImage.save(TEMP_FILE)  
  
        return self  
  
    def get_screenshot_by_custom_size(self, start_x, start_y, end_x, end_y):  
        #自定义截取范围  
        self.driver.get_screenshot_as_file(TEMP_FILE)  
        box = (start_x, start_y, end_x, end_y)  
  
        image = Image.open(TEMP_FILE)  
        newImage = image.crop(box)  
        newImage.save(TEMP_FILE)  
  
        return self  
  
    def write_to_file( self, dirPath, imageName, form = "png"):  
        #将截屏文件复制到指定目录下  
        if not os.path.isdir(dirPath):  
            os.makedirs(dirPath)  
        shutil.copyfile(TEMP_FILE, PATH(dirPath + "/" + imageName + "." + form))  
  
    def load_image(self, image_path):  
        #加载目标图片供对比用  
        if os.path.isfile(image_path):  
            load = Image.open(image_path)  
            return load  
        else:  
            raise Exception("%s is not exist" %image_path)
  
#     def same_as(self, load_image, percent):  
#         #方法一  求图片相似度
#         #对比图片，percent值设为0，则100%相似时返回True，设置的值越大，相差越大  
#         import math  
#         import operator  
#       
#         image1 = Image.open(TEMP_FILE)  
#         image2 = load_image  
#       
#         histogram1 = image1.histogram()  
#         histogram2 = image2.histogram()  
#       
#         differ = math.sqrt(reduce(operator.add, list(map(lambda a,b: (a-b)**2, histogram1, histogram2)))/len(histogram1))
#             
#         if differ <= percent:  
#             return True  
#         else:  
#             return False 
    
    def same_as(self,load_image,percent,size = (256,256)):
        #方法二 求图片相似度
        image1 = Image.open(TEMP_FILE)  
        image2 = load_image
             
        image1 = image1.resize(size).convert("RGB")   
        g = image1.histogram()     
        image2 = image2.resize(size).convert("RGB")   
        s = image2.histogram()     
        assert len(g) == len(s),"error"     
        data = []    
        for index in range(0,len(g)):        
            if g[index] != s[index]:            
                data.append(1 - abs(g[index] - s[index])/max(g[index],s[index]) )       
            else:            
                data.append(1)    
        similar=sum(data)/len(g) 
#         print(str(similar))
        if similar<percent:
            return False
        else:
            return True

    def equal(self, image1, image2):
        #判断两张图片全等
        img1=open(image1,'rb')
        img2=open(image2,'rb')
        if img1.read()==img2.read():
            return True
        else:
            return False
        