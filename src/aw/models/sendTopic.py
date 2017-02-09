#coding=utf-8
'''
Created on 2017-1-18

@author: xuls
'''
from aw.common.common import Common
from aw.const import Text
from aw.const import ID
# from time import sleep

class SendTopic(object):
    '''
    发话题
    '''
    def __init__(self, driver):  
        self.driver = driver
        self.common = Common(self.driver)
    
    def launch(self):
        self.common.touchText(Text.HomePage.BANGMAICHE)
        self.common.touchId(ID.HelpToBuyCar.OPEN_TOPIC)
    
    def launchVote(self):
        self.common.touchText("发投票")

    def selectVoteType(self, text):
        '''
        前提:发投票界面
        功能:选择投票类型
        '''
        self.common.touchText("投票类型:")
        self.common.touchText(text)
    
    def performance_isSelected(self,text): 
        '''
        前提:车型/车款投票编辑页面
        功能:判断某性能方面被选中
        '''
        element=self.driver.find_element_by_name(text)
        if element.is_selected():
            return True
        else:
            return False
        
    def performance_isNotSelected(self,text): 
        '''
        前提:车型/车款投票编辑页面
        功能:判断某性能方面没有被选中
        '''
        element=self.driver.find_element_by_name(text)
        if element.is_selected():
            return False
        else:
            return True
        
    def setPerformanceSelected(self,text): 
        '''
        前提:车型/车款投票编辑页面
        功能:选中某性能方面
        '''
        if self.performance_isNotSelected(text):
            self.common.touchText(text)
        
    def setPerformanceNotSelected(self,text):
        '''
        前提:车型/车款投票编辑页面
        功能:取消选中某性能方面
        '''
        if self.performance_isSelected(text):
            self.common.touchText(text)

    
        