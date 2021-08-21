from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import mimetypes
import email.mime.application

smtp_ssl_host = 'smtp.yandex.ru'  # smtp.mail.yahoo.com
smtp_ssl_port = 465
s = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
s.login('@yandex.ru', '')


msg = MIMEMultipart()
msg['Subject'] = '100 mails'
msg['From'] = '@yandex.ru'
msg['To'] = '@yandex.ru'

txt = MIMEText('LOL')
msg.attach(txt)

filename = '123.jpg' #path to file
fo=open(filename,'rb')
attach = email.mime.application.MIMEApplication(fo.read(),_subtype="jpg")
fo.close()
attach.add_header('Content-Disposition','attachment',filename=filename)
msg.attach(attach)
for i in range(100 ):
    s.send_message(msg)
s.quit()
