#coding=utf-8
'''
Created on 2016-12-16

@author: xuls
'''

class Account(object):
    
    #汽车报价大全账号/密码/用户名/姓名/手机号码
    ACCOUNT="13466643589"
    PASSWORD="20090222"
    USERNAME="xulishuang"
    
    NAME="测试请勿回复"
    NUMBER="13466666666"
    
    #自动化测试报告发送邮件地址/密码
    SMTPADDR="SMTP.126.com"
    SENDER="xulishuang_bit@126.com"
    SENDDER_PASSWORD="20090222yq"
    RECIEVER="xuls@yiche.com"

class Device(object):
    #终端系统版本/设备名
    PLATFORM_NAME='Android'
    PLATFORM_VERSION='6.0.1'
    DEVICE_NAME='c2b5813'
    
class App(object):
    #app存放路径/包名/activity名称/
    APP_PATH='../../../autotest_baojiadaquan/apps/qichebaojiadaquan_70.apk'
    APP_PACKAGE='com.yiche.price'
    APP_ACTIVITY='.ADActivity'
    
class AppiumConfig(object): 
    #appium设置中server地址及端口号
    EXECUTOR='http://127.0.0.1:4723/wd/hub'

class SearchFor(object):
    SEARCH1="奥迪"
    SEARCH2="文章"
    SEARCH3="哦哦哦哦"
    SEARCH4="..."

    def __init__(self, params):
        '''
        Constructor
        '''
        