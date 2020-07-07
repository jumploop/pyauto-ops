# coding: utf-8
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.utils import formatdate
from email.mime.application import MIMEApplication

HOST = "smtp.163.com"
SUBJECT = "官网业务服务质量周报"
TO = "827182486@qq.com"
FROM = "liming_201314521@163.com"


def addimg(src, imgid):
    fp = open(src, 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()
    msgImage.add_header('Content-ID', imgid)
    return msgImage


msg = MIMEMultipart('related')
msgtext = MIMEText("<font color=red>官网业务周平均延时图表:<br><img src=\"cid:weekly\" border=\"1\"><br>详细内容见附件。</font>", "html",
                   "utf-8")
msg.attach(msgtext)
msg.attach(addimg("img/weekly.png", "weekly"))

attach = MIMEApplication(open("doc/week_report.xlsx", "rb").read())
attach.add_header('Content-Disposition', 'attachment', filename="week_report.xlsx")
msg.attach(attach)

msg['Subject'] = SUBJECT
msg['From'] = FROM
msg['To'] = TO
msg['Date'] = formatdate()


def main():
    try:
        server = smtplib.SMTP()
        server.connect(HOST, 25)
        server.login(FROM, "XSUNGEAYHESZRGRO")
        server.sendmail(FROM, TO, msg.as_string())
        server.quit()
        print("邮件发送成功！")
    except Exception as e:
        print("失败：" + str(e))


if __name__ == '__main__':
    main()
