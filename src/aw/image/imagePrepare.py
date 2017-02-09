#coding=utf-8
'''
Created on 2017-1-9

@author: xuls
'''
import os
import unittest
from time import sleep

from aw.common import variable
from aw.const import Text
from aw.models import appunit
from selenium.webdriver.common.by import By

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

PATH2=os.path.dirname(os.getcwd())

class ImagePrepare(appunit.AppTest):
    
    def test_search1(self):
        '''输入关键字，搜索结果包含车型、文章、帖子'''
        element=self.driver.find_element_by_id("searchEt")
        element.send_keys(variable.SearchFor.SEARCH1)
        sleep(2)
        element=self.driver.find_element_by_id("content")       
        self.function.get_screenshot_by_element(element).write_to_file(PATH2+"\image\expected", "image01")       
        
        element=self.driver.find_element_by_id("brand_name_tv")
        element.click()
        sleep(12)
        element=self.driver.find_element_by_id("content")
        self.function.get_screenshot_by_element(element).write_to_file(PATH2+"\image\expected", "image02")
    
    def test_search2(self):
        '''输入关键字，搜索结果不包含车型，包含文章、帖子'''
        element=self.driver.find_element_by_id("searchEt")
        element.send_keys(variable.SearchFor.SEARCH2)
        sleep(2)
        element=self.driver.find_element_by_id("content")
        self.function.get_screenshot_by_element(element).write_to_file(PATH2+"\image\expected", "image03")
         
        element=self.driver.find_element_by_id("brand_name_tv")
        element.click()
        sleep(5)
        element=self.driver.find_element_by_id("indicator")
        self.function.get_screenshot_by_element(element).write_to_file(PATH2+"\image\expected", "image04") 
    
    def test_search3(self):
        '''输入关键字，搜索结果不包含车型、文章，包含帖子'''
        element=self.driver.find_element_by_id("searchEt")
        element.send_keys(variable.SearchFor.SEARCH3)
        sleep(5)
        element=self.driver.find_element_by_id("content")
        self.function.get_screenshot_by_element(element).write_to_file(PATH2+"\image\expected", "image05")
         
        element=self.driver.find_element_by_id("brand_name_tv")
        element.click()
        sleep(5)
        element=self.driver.find_element_by_id("indicator")
        self.function.get_screenshot_by_element(element).write_to_file(PATH2+"\image\expected", "image06")   
     
    def test_search4(self):
        '''输入关键字，搜索结果不包含车型、文章、帖子'''
        element=self.driver.find_element_by_id("searchEt")
        element.send_keys(variable.SearchFor.SEARCH4)
        sleep(2)
        element=self.driver.find_element_by_id("content")
        self.function.get_screenshot_by_element(element).write_to_file(PATH2+"\image\expected", "image07")
         
        element=self.driver.find_element_by_id("brand_name_tv")
        element.click()
        sleep(8)
        element=self.driver.find_element_by_id("content")
        self.function.get_screenshot_by_element(element).write_to_file(PATH2+"\image\expected", "image08")
    
    def test_enquiry(self):
        '''询价测试'''
        sleep(5)
        self.common.swipeUp()
        self.common.touchSlideText(Text.BranchName.Benz)
        self.common.touchSlideText(Text.BranchName.Benz_BRANCH1)
        sleep(5)
        self.common.touchSlideText("询底价")
        sleep(5)
        self.common.inputText(variable.Account.NAME, variable.Account.NUMBER)
        sleep(2)
        element=self.driver.find_element_by_id("content")
        self.function.get_screenshot_by_element(element).write_to_file(PATH2+"\image\expected", "image11")
           
        self.common.touchText("提交")
        sleep(5)
        l=self.common.getSize()
        self.function.get_screenshot_by_custom_size(0, l[1]*0.25, l[0], l[1]*0.75).write_to_file(PATH2+"\image\expected", "image12")  
            
        self.common.touchText("知道了")
        sleep(3)
        element=self.driver.find_element_by_id("content")
        self.function.get_screenshot_by_element(element).write_to_file(PATH2+"\image\expected", "image13")
            
        self.common.multiBack(2);
        self.common.touchText(Text.HomePage.WODE)
        self.common.touchText("询价记录")
        sleep(5)
        self.function.get_screenshot_by_custom_size(10,219,710,379).write_to_file(PATH2+"\image\expected", "image14")
    
    def test_carContrast(self): 
        '''开始对比'''        
        self.common.touchText(Text.HomePage.FAXIAN)
        self.common.touchText("车型对比")
        
        if not self.common.checkTextExist("请添加车款，进行对比"):
            self.common.touchText("编辑")
            self.common.touchText("清空")
            self.common.touchText("清空")
        self.common.touchText("添加车款")
        self.common.touchSlideText(Text.BranchName.VW)
        self.common.touchSlideText(Text.BranchName.VW_BRANCH1)
        self.common.touchSlideText(Text.BranchName.VW_MODEL1)
        
        self.common.touchText("添加车款")
        self.common.touchSlideText(Text.BranchName.Audi)
        self.common.touchSlideText(Text.BranchName.Audi_BRANCH1)
        self.common.touchSlideText(Text.BranchName.Audi_MODEL1)
        
        element=self.driver.find_element_by_id("content")
        self.function.get_screenshot_by_element(element).write_to_file(PATH2+"\image\expected", "image21")
        
        self.common.touchText("开始对比")
        sleep(10)
        
        element=self.driver.find_element_by_id("content")
        self.function.get_screenshot_by_element(element).write_to_file(PATH2+"\image\expected", "image22")
    
    def test_friendsToHelp1(self):
        '''分享到朋友帮选车'''
        #初始化环境，清空我的社区--话题
        self.wode.LaunchTopic() 
        self.common.waitUntilNotPresent(By.NAME, "加载中…",timeout=60)
        self.wode.deleteTopics()
        #返回，进入朋友帮买车
        self.common.back()
        sleep(2)
        self.common.back()
        self.friendsToHelp.launch()
        #清空已创建的朋友帮买车
        self.friendsToHelp.setHomepageEmpty()
        #发起投票，添加车型，选择性能
        self.friendsToHelp.startBranchVote()
        self.friendsToHelp.addBranch(Text.BranchName.BMW, Text.BranchName.BMW_BRANCH1)
        self.friendsToHelp.addBranch(Text.BranchName.Benz, Text.BranchName.Benz_BRANCH2)
        self.friendsToHelp.setPerformanceSelected("外观")
        self.friendsToHelp.setPerformanceSelected("安全")
        
        element=self.driver.find_element_by_id("content")
        self.function.get_screenshot_by_element(element).write_to_file(PATH2+"\image\expected", "image31")
        
        self.common.touchText("发给朋友帮我选车")
        self.common.touchText("帮买车社区")
        element=self.driver.find_element_by_id("content")
        self.function.get_screenshot_by_element(element).write_to_file(PATH2+"\image\expected", "image32")
        
        self.common.touchText("提交")
        sleep(5)
        element=self.driver.find_element_by_id("content")
        self.function.get_screenshot_by_element(element).write_to_file(PATH2+"\image\expected", "image33")
    
    def test_friendsToHelp2(self):
        '''车型投票--分享到朋友圈'''
        #进入朋友帮买车
        self.friendsToHelp.launch()
        #清空已创建的朋友帮买车
        self.friendsToHelp.setHomepageEmpty()
        #发起投票，添加车型，选择性能
        self.friendsToHelp.startBranchVote()
        self.friendsToHelp.addBranch(Text.BranchName.BMW, Text.BranchName.BMW_BRANCH1)
        self.friendsToHelp.addBranch(Text.BranchName.Benz, Text.BranchName.Benz_BRANCH2)
        self.friendsToHelp.setPerformanceSelected("操控")
        self.friendsToHelp.setPerformanceSelected("油耗")
        element=self.driver.find_element_by_id("content")
        self.function.get_screenshot_by_element(element).write_to_file(PATH2+"\image\expected", "image35")
  
        self.common.touchText("发给朋友帮我选车")
        self.common.touchText("朋友圈")
        sleep(10)
        element=self.driver.find_element_by_id("content")
        self.function.get_screenshot_by_element(element).write_to_file(PATH2+"\image\expected", "image36")
      
        self.common.back()
        element=self.driver.find_element_by_id("content")
        self.function.get_screenshot_by_element(element).write_to_file(PATH2+"\image\expected", "image37")
    
    def test_friendsToHelp3(self):
        '''车款投票--分享到帮买车'''
        #初始化环境，清空我的社区--话题
        self.wode.LaunchTopic() 
        self.common.waitUntilNotPresent(By.NAME, "加载中…",timeout=60)
        self.wode.deleteTopics()
        #返回，进入朋友帮买车
        self.common.back()
        sleep(2)
        self.common.back()
        self.friendsToHelp.launch()
        #清空已创建的朋友帮买车
        self.friendsToHelp.setHomepageEmpty()
        #发起投票，添加车型，选择性能
        self.friendsToHelp.startModelVote()
        self.friendsToHelp.addModel(Text.BranchName.BMW, Text.BranchName.BMW_BRANCH1,Text.BranchName.BMW_MODEL1)
        self.friendsToHelp.addModel(Text.BranchName.Benz, Text.BranchName.Benz_BRANCH2,Text.BranchName.Benz_MODEL2)
        self.friendsToHelp.setPerformanceSelected("外观")
        self.friendsToHelp.setPerformanceSelected("安全")
        element=self.driver.find_element_by_id("content")
        self.function.get_screenshot_by_element(element).write_to_file(PATH2+"\image\expected", "image38")
        #发送到帮买车社区
        self.common.touchText("发给朋友帮我选车")
        self.common.touchText("帮买车社区")
        sleep(3)
        element=self.driver.find_element_by_id("content")
        self.function.get_screenshot_by_element(element).write_to_file(PATH2+"\image\expected", "image39") 
        #点击提交
        self.common.touchText("提交")
        sleep(5)
        element=self.driver.find_element_by_id("content")
        self.function.get_screenshot_by_element(element).write_to_file(PATH2+"\image\expected", "image3a")
        #进入话题
        self.common.back()
        self.wode.LaunchTopic()
        element=self.driver.find_element_by_id("content")
        self.function.get_screenshot_by_element(element).write_to_file(PATH2+"\image\expected", "image3b")
        
    def test_friendsToHelp4(self):
        '''车款投票--分享到朋友圈'''
        #进入朋友帮买车
        self.friendsToHelp.launch()
        #清空已创建的朋友帮买车
        self.friendsToHelp.setHomepageEmpty()
        #发起投票，添加车型，选择性能
        self.friendsToHelp.startModelVote()
        self.friendsToHelp.addModel(Text.BranchName.BMW, Text.BranchName.BMW_BRANCH1, Text.BranchName.BMW_MODEL1)
        self.friendsToHelp.addModel(Text.BranchName.Benz, Text.BranchName.Benz_BRANCH2, Text.BranchName.Benz_MODEL2)
        self.friendsToHelp.setPerformanceSelected("操控")
        self.friendsToHelp.setPerformanceSelected("油耗")
        sleep(2)
        element=self.driver.find_element_by_id("content")
        self.function.get_screenshot_by_element(element).write_to_file(PATH2+"\image\expected", "image3c")
        #发送到朋友圈
        self.common.touchText("发给朋友帮我选车")
        self.common.touchText("朋友圈")
        sleep(6)
        element=self.driver.find_element_by_id("content")
        self.function.get_screenshot_by_element(element).write_to_file(PATH2+"\image\expected", "image3d")
        
        self.common.back()
        element=self.driver.find_element_by_id("content")
        self.function.get_screenshot_by_element(element).write_to_file(PATH2+"\image\expected", "image3e")

    def test_sendTopic1(self):
        '''普通话题'''
        #初始化环境，清空我的社区--话题
        self.wode.LaunchTopic() 
        self.common.waitUntilNotPresent(By.NAME, "加载中…",timeout=60)
        self.wode.deleteTopics()
        #返回，从帮买车进入话题
        self.common.back()
        sleep(2)
        self.common.back()
        self.sendTopic.launch()
        #编辑普通话题内容：
        self.driver.find_element_by_class_name("android.widget.EditText").send_keys("测试请勿回复")
        self.common.touchText("选择主题:")
        self.common.touchText("选车交流")
        self.common.touchText("关联车型")
        self.common.touchSlideText(Text.BranchName.Audi)
        self.common.touchSlideText(Text.BranchName.Audi_BRANCH2)
        element=self.driver.find_element_by_id("content")
        self.function.get_screenshot_by_element(element).write_to_file(PATH2+"\image\expected", "image41")
        #点击提交
        self.common.touchText("提交")
        #进入我的社区--话题  
        self.wode.LaunchTopic()
        element=self.driver.find_element_by_id("content")
        self.function.get_screenshot_by_element(element).write_to_file(PATH2+"\image\expected", "image42")
    
    def test_sendTopic2(self):
        '''发车型投票'''
        #初始化环境，清空我的社区--话题
        self.wode.LaunchTopic() 
        self.common.waitUntilNotPresent(By.NAME, "加载中…",timeout=60)
        self.wode.deleteTopics()
        #返回，从帮买车进入话题
        self.common.back()
        sleep(2)
        self.common.back()
        self.sendTopic.launch()
        #进入发布投票界面
        self.sendTopic.launchVote()
        #选择发车型投票
        self.sendTopic.selectVoteType("车型投票")
        #编辑车型投票界面
        self.driver.find_element_by_class_name("android.widget.EditText").send_keys("测试请勿回复")
        self.common.touchText("选择车型")
        self.common.touchSlideText(Text.BranchName.Audi)
        self.common.touchSlideText(Text.BranchName.Audi_BRANCH2)
        self.common.touchText("选择车型")
        self.common.touchSlideText(Text.BranchName.Benz)
        self.common.touchSlideText(Text.BranchName.Benz_BRANCH3)
        self.sendTopic.setPerformanceSelected("外观")
        self.sendTopic.setPerformanceSelected("油耗")
        self.common.touchText("选择主题:")
        self.common.touchText("选车交流")
        element=self.driver.find_element_by_id("content")
        self.function.get_screenshot_by_element(element).write_to_file(PATH2+"\image\expected", "image43")
        #点击提交
        self.common.touchText("提交")
        #进入我的社区--话题  
        self.wode.LaunchTopic()
        sleep(2)
        element=self.driver.find_element_by_id("content")
        self.function.get_screenshot_by_element(element).write_to_file(PATH2+"\image\expected", "image44")
        
    def test_sendTopic3(self):
        '''发车款投票'''
        #初始化环境，清空我的社区--话题
        self.wode.LaunchTopic() 
        self.common.waitUntilNotPresent(By.NAME, "加载中…",timeout=60)
        self.wode.deleteTopics()
        #返回，从帮买车进入话题
        self.common.back()
        sleep(2)
        self.common.back()
        self.sendTopic.launch()
        #进入发布投票界面
        self.sendTopic.launchVote()
        #选择发车型投票
        self.sendTopic.selectVoteType("车款投票")
        #编辑车型投票界面
        self.driver.find_element_by_class_name("android.widget.EditText").send_keys("测试请勿回复")
        self.common.touchText("选择车款")
        self.common.touchSlideText(Text.BranchName.Audi)
        self.common.touchSlideText(Text.BranchName.Audi_BRANCH2)
        self.common.touchSlideText(Text.BranchName.Audi_MODEL2)
        self.common.touchText("选择车款")
        self.common.touchSlideText(Text.BranchName.Benz)
        self.common.touchSlideText(Text.BranchName.Benz_BRANCH3)
        self.common.touchSlideText(Text.BranchName.Benz_MODEL3)
        self.sendTopic.setPerformanceSelected("外观")
        self.sendTopic.setPerformanceSelected("油耗")
        self.common.touchText("选择主题:")
        self.common.touchText("选车交流")
        element=self.driver.find_element_by_id("content")
        self.function.get_screenshot_by_element(element).write_to_file(PATH2+"\image\expected", "image45")
        #点击提交
        self.common.touchText("提交")
        #进入我的社区--话题  
        self.wode.LaunchTopic()
        sleep(2)
        element=self.driver.find_element_by_id("content")
        self.function.get_screenshot_by_element(element).write_to_file(PATH2+"\image\expected", "image46")
        
    def test_sendTopic4(self):
        '''发观点投票'''
        #初始化环境，清空我的社区--话题
        self.wode.LaunchTopic() 
        self.common.waitUntilNotPresent(By.NAME, "加载中…",timeout=60)
        self.wode.deleteTopics()
        #返回，从帮买车进入话题
        self.common.back()
        sleep(2)
        self.common.back()
        self.sendTopic.launch()
        #进入发布投票界面
        self.sendTopic.launchVote()
        #选择发车型投票
        self.sendTopic.selectVoteType("观点投票")
        #编辑车型投票界面
        self.driver.find_element_by_class_name("android.widget.EditText").send_keys("测试请勿回复")
        
        self.common.touchText("输入选项")
        self.driver.find_element_by_name("请输入选项内容(15字以内)").send_keys("测试请勿回复")
        self.common.touchText("输入选项")
        self.driver.find_element_by_name("请输入选项内容(15字以内)").send_keys("测试请勿回复")
       
        self.common.touchText("选择主题:")
        self.common.touchText("选车交流")
        element=self.driver.find_element_by_id("content")
        self.function.get_screenshot_by_element(element).write_to_file(PATH2+"\image\expected", "image47")
        #点击提交
        self.common.touchText("提交")
        #进入我的社区--话题  
        self.wode.LaunchTopic()
        sleep(2)
        element=self.driver.find_element_by_id("content")
        self.function.get_screenshot_by_element(element).write_to_file(PATH2+"\image\expected", "image48")
    
if __name__ == "__main__":
    suite = unittest.TestSuite()   
#     suite.addTest(ImagePrepare("test_search1"))
#     suite.addTest(ImagePrepare("test_search2"))
#     suite.addTest(ImagePrepare("test_search3"))
#     suite.addTest(ImagePrepare("test_search4")) 
#     suite.addTest(ImagePrepare("test_enquiry"))
#     suite.addTest(ImagePrepare("test_carContrast"))
    suite.addTest(ImagePrepare("test_friendsToHelp1"))
    suite.addTest(ImagePrepare("test_friendsToHelp2"))
    suite.addTest(ImagePrepare("test_friendsToHelp3"))
    suite.addTest(ImagePrepare("test_friendsToHelp4"))
#     suite.addTest(ImagePrepare("test_sendTopic1"))
#     suite.addTest(ImagePrepare("test_sendTopic2"))
#     suite.addTest(ImagePrepare("test_sendTopic3"))
#     suite.addTest(ImagePrepare("test_sendTopic4"))
    unittest.TextTestRunner().run(suite)