#coding=utf-8
'''
Created on 2016-12-16

@author: xuls
'''
from HTMLTestRunner import HTMLTestRunner
from email.mime.text import MIMEText
from email.header import Header
import unittest
import smtplib
import time
import os
from aw.common import variable

#======定义发送邮件======
def send_mail(file_new):
    f=open(file_new, 'rb')
    mail_body=f.read()
    f.close()
    
    msg=MIMEText(mail_body, 'html', 'utf-8')
    msg['Subject']=Header("自动化测试报告", 'utf-8')
    
    msg['from'] = variable.Account.SENDER
    msg['to'] = variable.Account.RECIEVER
    
    smtp=smtplib.SMTP()
    
    smtp.connect(variable.Account.SMTPADDR)
    smtp.login(variable.Account.SENDER, variable.Account.SENDDER_PASSWORD)
    smtp.sendmail(variable.Account.SENDER, variable.Account.RECIEVER, msg.as_string())
    smtp.quit()

    print('email has send out !')
    
#======查找测试报告目录，找到最新生成的测试报告文件======
def new_report(testreport):
    lists=os.listdir(testreport)
    lists.sort(key=lambda fn: os.path.getmtime(testreport+"\\"+fn))
    file_new=os.path.join(testreport,lists[-1])
    print(file_new)
    return file_new

 
if __name__ == '__main__':
    path=os.path.dirname(os.getcwd())
    now=time.strftime("%Y-%m_%d %H_%M_%S")
    filename=path+'/report/'+now+'result.html'
    fp=open(filename, 'wb')
    runner=HTMLTestRunner(stream=fp,
                          title='汽车报价大全自动化测试报告',
                          description='用例执行情况:360 N4  android版本6.0')
    
    discover=unittest.defaultTestLoader.discover(path+'/script', pattern='test_search.py')
     
    runner.run(discover)
    fp.close() #关闭生成的报告
    file_path=new_report(path+'/report/')  #查找生成的报告
    send_mail(file_path)  #调用发邮件模块        
    
    