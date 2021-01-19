# coding:utf-8

import smtplib
from email.mime.text import MIMEText
from email.header import Header



class Mail:
    def __init__(self):
        # 第三方 SMTP 服务

        self.mail_host = "smtp.qq.com"  # 设置服务器:这个是qq邮箱服务器，直接复制就可以
        self.mail_pass = "fmlgcjkysuqadhfi"  # 刚才我们获取的授权码
        self.sender = '2675607101@qq.com'  # 你的邮箱地址
        # self.receivers = receivers # 收件人的邮箱地址，可设置为你的QQ邮箱或者其他邮箱，可多个

    def send(self,receivers,code):

        content = '您的验证码为%s' % code
        message = MIMEText(content, 'plain', 'utf-8')

        message['From'] = Header("MQZ的blog", 'utf-8')
        message['To'] = Header(receivers, 'utf-8')

        subject = '注册验证码'  # 发送的主题，可自由填写
        message['Subject'] = Header(subject, 'utf-8')
        try:
            smtpObj = smtplib.SMTP_SSL(self.mail_host, 465)
            smtpObj.login(self.sender, self.mail_pass)
            smtpObj.sendmail(self.sender, receivers, message.as_string())
            smtpObj.quit()
            return "ok"
        except smtplib.SMTPException as e:
            return "error"


