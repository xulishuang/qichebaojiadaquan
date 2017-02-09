#coding=utf-8
'''
Created on 2017-1-17

@author: xuls
'''
from time import sleep
from aw.common.common import Common
from aw.const import Text
from aw.common import variable

class Wode(object):
    '''
    进入我的社区
    '''
    def __init__(self, driver):  
        self.driver = driver
        self.common = Common(self.driver)
    
    def Launch(self):
        self.common.touchText(Text.HomePage.WODE)
        
    def LaunchMyCommunity(self):  
        self.common.touchText(Text.HomePage.WODE)
        sleep(2)
        self.common. touchText(Text.Wode.MY_COMMUNITY)
    
    def LaunchTopic(self):
        self.common.touchText(Text.HomePage.WODE)
#         sleep(5)
        self.common. touchText(Text.Wode.MY_COMMUNITY)
#         sleep(5)
        self.common.touchText(Text.Wode.TOPIC)
    
    def checkTopicEmpty(self):
        if self.common.checkTextExist("您还没有发表过话题"):
            return True
        else:
            return False
    
    def checkTopicNotEmpty(self):
        if not self.common.checkTextExist("您还没有发表过话题"):
            return True
        else:
            return False
    
    def deleteTopics(self):
        while self.checkTopicNotEmpty():
            self.common.touchText(variable.Account.USERNAME)
            
            self.common.touchText(Text.Common.DELETE)
            self.common.touchText(Text.Common.OK) 