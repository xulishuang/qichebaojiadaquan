#coding=utf-8
'''
Created on 2017-1-16

@author: xuls
'''
import unittest
from time import sleep
from aw.const import Text
from aw.models import appunit
from aw.common import variable
from selenium.webdriver.common.by import By

class SendTopicTest(appunit.AppTest):
    '''发话题测试'''
    
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
        #编辑完成后，判断当前页面是否正确
        self.assertResult.assertByImage("content", "image41", 0.75)
        #点击提交
        self.common.touchText("提交")
        #进入我的社区--话题  
        self.wode.LaunchTopic()
        #判断普通话题是否发送正确
        self.common.waitUntilPresent(By.NAME, variable.Account.USERNAME)
        self.assertResult.assertByImage("content", "image42", 0.75)
        
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
        #编辑完成后，判断当前页面是否正确
        self.assertResult.assertByImage("content", "image43", 0.80)
        #点击提交
        self.common.touchText("提交")
        #进入我的社区--话题  
        self.wode.LaunchTopic()
        #判断普通话题是否发送正确
        self.common.waitUntilPresent(By.NAME, variable.Account.USERNAME)
        self.assertResult.assertByImage("content", "image44", 0.80)
        
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
        #编辑完成后，判断当前页面是否正确
        self.assertResult.assertByImage("content", "image45", 0.80)
        #点击提交
        self.common.touchText("提交")
        #进入我的社区--话题  
        self.wode.LaunchTopic()
        #判断普通话题是否发送正确
        self.common.waitUntilPresent(By.NAME, variable.Account.USERNAME)
        self.assertResult.assertByImage("content", "image46", 0.85)
        
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
        #编辑完成后，判断当前页面是否正确
        self.assertResult.assertByImage("content", "image47", 0.68)
        #点击提交
        self.common.touchText("提交")
        #进入我的社区--话题  
        self.wode.LaunchTopic()
        #判断普通话题是否发送正确
        self.common.waitUntilPresent(By.NAME, variable.Account.USERNAME)
        self.assertResult.assertByImage("content", "image48", 0.82)
        
if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(SendTopicTest("test_sendTopic1"))
    suite.addTest(SendTopicTest("test_sendTopic2"))
    suite.addTest(SendTopicTest("test_sendTopic3"))
    suite.addTest(SendTopicTest("test_sendTopic4"))
    unittest.TextTestRunner().run(suite)