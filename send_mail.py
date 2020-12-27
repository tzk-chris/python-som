# -*- coding: utf-8 -*-
"""
@File  : send_mail.py
@Author: Chris_kun
@Date  : 2020/7/17 2020/07/17
"""
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

msg_from = 'xxx'  # 发送方邮箱
passwd = 'xxx'  # 填入发送方邮箱的授权码
msg_to = 'xxx'  # 收件人邮箱

def sendmail():
    subject = "python邮件测试"  # 主题
    content = "这是我使用python smtplib及email模块发送的邮件"   # 正文
    msg = MIMEText(content)
    msg['Subject'] = subject
    msg['From'] = formataddr(["Ekko", msg_from])
    msg['To'] = formataddr(["chris", msg_to])

    ret = True

    try:
        smtp = smtplib.SMTP_SSL("smtp.qq.com",465)
        smtp.login(msg_from,passwd)
        smtp.sendmail(msg_from,[msg_to,],msg.as_string())
    except Exception:
        ret = False
    return ret

ret = sendmail()
if ret:
    print("邮件发送成功")
else:
    print("邮件发送失败")
