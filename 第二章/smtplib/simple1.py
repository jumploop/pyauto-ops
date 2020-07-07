import smtplib

HOST = "smtp.163.com"
SUBJECT = "Test email from Python"
TO = "test@qq.com"
FROM = "test@163.com"
text = "Python rules them all!"
BODY = "\r\n".join((
    "From: %s" % FROM,
    "To: %s" % TO,
    "Subject: %s" % SUBJECT,
    "",
    text
))


def main():
    try:
        server = smtplib.SMTP()
        server.connect(HOST, 25)
        server.login(FROM, "123456")
        server.sendmail(FROM, [TO], BODY)
        server.quit()
        print("邮件发送成功！")
    except Exception as e:
        print("失败：" + str(e))


if __name__ == '__main__':
    main()
