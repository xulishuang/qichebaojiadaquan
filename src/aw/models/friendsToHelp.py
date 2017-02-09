#coding=utf-8
'''
Created on 2017-1-17

@author: xuls
'''
from aw.common.common import Common
from aw.const import Text
from aw.const import ID

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FriendsToHelp(object):
    '''
    朋友帮选车
    ''' 
    def __init__(self, driver):  
        self.driver = driver
        self.common = Common(self.driver)
        
    def launch(self):
        self.common.touchText(Text.HomePage.FAXIAN)
        WebDriverWait(self.driver, 20, 0.5).until(EC.presence_of_element_located((By.ID,"mactivity_pic")))
        self.common.swipeLeft()
        self.common.swipeLeft()
        self.common.touchText(Text.Faxian.FRIENDS_TO_HELP)
        
    def homepage_isEmpty(self):
        '''
        前提:朋友帮选车首页
        功能:判断朋友帮选车首页无已创建的帮选车
        '''
        if self.common.checkIdExist(ID.FriendsToHelp.TOTAL_CAR):
            return False
        else:
            return True
    
    def setHomepageEmpty(self):
        '''
        前提:朋友帮选车首页
        功能:清空朋友帮选车首页已创建的帮选车
        '''
        while not self.homepage_isEmpty():
            self.common.touchId(ID.FriendsToHelp.TOTAL_CAR)
            if self.common.checkTextExist(Text.FriendsToHelp.CLOSE_VOTE):
                self.common.touchText(Text.FriendsToHelp.CLOSE_VOTE)
                self.common.touchText(Text.Common.OK)
            if self.common.checkTextExist(Text.FriendsToHelp.DELETE_VOTE):
                self.common.touchText(Text.FriendsToHelp.DELETE_VOTE)
                self.common.touchText(Text.Common.OK)
    
    def startBranchVote(self):
        '''
        前提:朋友帮选车首页
        功能:发起车型投票
        '''
        self.common.touchText(Text.FriendsToHelp.START_VOTE)
        self.common.touchText(Text.FriendsToHelp.START_BRANCH_VOTE)
        
    def startModelVote(self):
        '''
        前提:朋友帮选车首页
        功能:发起车款投票
        '''
        self.common.touchText(Text.FriendsToHelp.START_VOTE)
        self.common.touchText(Text.FriendsToHelp.START_MODEL_VOTE)        
    
    def addBranch(self, brand, sub_brand):
        '''
        前提:车型投票编辑页面
        功能:选择车型
        '''
        self.common.touchText(Text.FriendsToHelp.SELECT_BRANCH)
        self.common.touchSlideText(brand)
        self.common.touchSlideText(sub_brand)
    
    def addModel(self, brand, sub_brand, model):
        '''
        前提:车型投票编辑页面
        功能:选择车型
        '''
        self.common.touchText(Text.FriendsToHelp.SELECT_MODEL)
        self.common.touchSlideText(brand)
        self.common.touchSlideText(sub_brand)
        self.common.touchSlideText(model)
        
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