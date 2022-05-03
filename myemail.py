import smtplib
import email.utils
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import logging


def send_mail(**kwargs):
    SUBJECT = kwargs.pop("subject")
    SENDER = kwargs.pop("sender")
    RECIPIENT = kwargs.pop("recp")
    BODY_TEXT = kwargs.pop("body_text")
    BODY_HTML = kwargs.pop("body_html")
    HOST = kwargs.pop("smtp_host")
    PORT = kwargs.pop("smtp_port")
    USERNAME_SMTP = kwargs.pop("smtp_user")
    PASSWORD_SMTP = kwargs.pop("smtp_pass")
    tls_enable = kwargs.pop("tls_enable")
    # Create message container - the correct MIME type is multipart/alternative.
#    msg['Content-Type'] = "text/html; charset=utf-8"
    msg = MIMEMultipart("alternative")
    msg["Subject"] = SUBJECT
    msg["From"] = SENDER
    #msg["To"] = RECIPIENT
    msg["To"] = ",".join(RECIPIENT)
    part1 = MIMEText(BODY_TEXT, "plain")
    part2 = MIMEText(BODY_HTML, "html")
    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    msg.attach(part1)
    msg.attach(part2)
    try:
        print(HOST,PORT)
        server = smtplib.SMTP(HOST, PORT)
        server.ehlo()
        if tls_enable:
             server.starttls()
             # stmplib docs recommend calling ehlo() before & after starttls()
             server.ehlo()
             print("hello")
        server.login(USERNAME_SMTP, PASSWORD_SMTP)
        server.sendmail(SENDER, RECIPIENT, msg.as_string())
        server.close()
    # Display an error message if something goes wrong.
    except Exception as e:
        logging.exception("error occurred while sending mail")
    else:
        logging.info("Email sent!")


"""
send_message(
    subject="hello_test",
    sender="nikhil@gmail.com",
    recp="seeee@t.com",
    body_text="hello123",
    body_html="<html><H1>hello bhaiya</H1></html>",
    smtp_host="localhost",
    smtp_port="1025",
    smtp_user="hello",
    smtp_pass="hello",
)
"""
