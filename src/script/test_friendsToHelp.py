#coding=utf-8
'''
Created on 2017-1-16

@author: xuls
'''
import unittest
from time import sleep
from aw.models import appunit

from aw.const import Text

from selenium.webdriver.common.by import By

class FriendsToHelpTest(appunit.AppTest):
    '''朋友帮选车测试'''
    def test_friendsToHelp1(self):
        '''车型投票--分享到帮买车'''
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
        #判断当前页面是否正确
        self.assertResult.assertByImage("content", "image31", 0.75)
        #发送到帮买车社区
        self.common.touchText("发给朋友帮我选车")
        self.common.touchText("帮买车社区")
        #判断当前页面是否正确
        self.common.waitUntilPresent(By.NAME, "提交",timeout=15)
        self.assertResult.assertByImage("content", "image32", 0.80) 
        #点击提交
        self.common.touchText("提交")
        
        #判断当前页面是否正确
        self.common.waitUntilPresent(By.NAME, "发起投票")
        self.assertResult.assertByImage("content", "image33", 0.70) 
        #进入话题
        self.common.back()
        self.wode.LaunchTopic()
        #判断话题是否发送成功
        self.assertResult.assertByImage("content", "image34", 0.75)
        
    def test_friendsToHelp2(self):
        '''车型投票--分享到朋友圈'''
        #进入朋友帮买车
        self.friendsToHelp.launch()
        #清空已创建的朋友帮买车
        self.friendsToHelp.setHomepageEmpty()
        #发起投票，添加车型，选择性能
        self.common.waitUntilPresent(By.NAME, "发起投票")
        self.friendsToHelp.startBranchVote()
        self.friendsToHelp.addBranch(Text.BranchName.BMW, Text.BranchName.BMW_BRANCH1)
        self.friendsToHelp.addBranch(Text.BranchName.Benz, Text.BranchName.Benz_BRANCH2)
        self.friendsToHelp.setPerformanceSelected("操控")
        self.friendsToHelp.setPerformanceSelected("油耗")
        #判断当前页面是否正确
        self.assertResult.assertByImage("content", "image35", 0.85)
        #发送到朋友圈
        self.common.touchText("发给朋友帮我选车")
        self.common.touchText("朋友圈")
        
        #判断当前页面是否正确
        self.common.waitUntilPresent(By.NAME, "WeChat")
        self.assertResult.assertByImage("content", "image36", 0.95) 
        self.common.back()
        #判断当前页面是否正确
        self.assertResult.assertByImage("content", "image37", 0.85) 
    
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
        #判断当前页面是否正确
        self.assertResult.assertByImage("content", "image38", 0.70)
        #发送到帮买车社区
        self.common.touchText("发给朋友帮我选车")
        self.common.touchText("帮买车社区")
        #判断当前页面是否正确
        self.common.waitUntilPresent(By.NAME, "提交", timeout=15)
        self.assertResult.assertByImage("content", "image39", 0.80) 
        #点击提交
        self.common.touchText("提交")
        
        #判断当前页面是否正确
        self.common.waitUntilPresent(By.NAME, "发起投票")
        self.assertResult.assertByImage("content", "image3a", 0.75) 
        #进入话题
        self.common.back()
        self.wode.LaunchTopic()
        #判断话题是否发送成功
        self.assertResult.assertByImage("content", "image3b", 0.80)
        
    def test_friendsToHelp4(self):
        '''车款投票--分享到朋友圈'''
        #进入朋友帮买车
        self.friendsToHelp.launch()
        #清空已创建的朋友帮买车
        self.friendsToHelp.setHomepageEmpty()
        #发起投票，添加车型，选择性能
        self.common.waitUntilPresent(By.NAME, "发起投票")
        self.friendsToHelp.startModelVote()
        self.friendsToHelp.addModel(Text.BranchName.BMW, Text.BranchName.BMW_BRANCH1, Text.BranchName.BMW_MODEL1)
        self.friendsToHelp.addModel(Text.BranchName.Benz, Text.BranchName.Benz_BRANCH2, Text.BranchName.Benz_MODEL2)
        self.friendsToHelp.setPerformanceSelected("操控")
        self.friendsToHelp.setPerformanceSelected("油耗")
        sleep(2)
        #判断当前页面是否正确
        self.assertResult.assertByImage("content", "image3c", 0.70)
        #发送到朋友圈
        self.common.touchText("发给朋友帮我选车")
        self.common.touchText("朋友圈")
        #判断当前页面是否正确
        self.common.waitUntilPresent(By.NAME, "WeChat")
        self.assertResult.assertByImage("content", "image3d", 0.95) 
        self.common.back()
        #判断当前页面是否正确
        self.assertResult.assertByImage("content", "image3e", 0.85) 
                
if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(FriendsToHelpTest("test_friendsToHelp1"))
    suite.addTest(FriendsToHelpTest("test_friendsToHelp2"))
    suite.addTest(FriendsToHelpTest("test_friendsToHelp3"))
    suite.addTest(FriendsToHelpTest("test_friendsToHelp4"))
    unittest.TextTestRunner().run(suite)