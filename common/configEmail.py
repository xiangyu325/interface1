import smtplib
import time
from email.mime.text import  MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import os
import readConfig
import getpathInfo
from common.Log import logger
read_conf = readConfig.ReadConfig()
HOST = read_conf.get_email('HOST')#从配置文件中读取，邮件主题
FROM = read_conf.get_email('FROM')#从配置文件中读取，邮件发送人
TO = read_conf.get_email('TO')#从配置文件中读取，邮件收件人
mailpass = read_conf.get_email('mailpass')#从配置文件中读取，邮箱密码
mail_path = os.path.join(getpathInfo.get_Path(), 'result', 'report.html')#获取测试报告路径
logger = logger
class send_email():
    def outlook(self):
        now = time.strftime('%Y-%m-%d_%H_%M_%S')
        SUBJECT = now+'的测试报告'
        message =MIMEMultipart()
        message['Subject'] = SUBJECT
        message['From'] = FROM
        message['To'] = TO
        #--邮件内容部分--
        mail_msg = """
        <p>python接口测试zhunbei</p>
        """
        part = MIMEText(mail_msg,'html','utf-8')
        message.attach(part)
        # --这是附件部分--
        part = MIMEApplication(open(mail_path,'rb').read())
        part.add_header('Content-Disposition','attachment',filename ='report.html')
        message.attach(part)
        #--连接服务器，发送邮件
        server =smtplib.SMTP_SSL(HOST,timeout=300)
        server.login(FROM,mailpass)
        server.sendmail(FROM,TO,message.as_string())
        server.close()
if __name__ == '__main__':
    send_email().outlook()