import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

username="program.python.test@gmail.com"
password = "hfzuhitpywagszzg"

def send_mail(text, subject, to_emails=None, from_email="Python Test <program.python.test@gmail.com>"):
    assert isinstance(to_emails, list)

    msg = MIMEMultipart("alternative")
    msg["From"] = from_email
    msg["To"] = " ,".join(to_emails)
    msg["Subject"] = subject

    text_body = MIMEText(text, "plain")
    msg.attach(text_body)

    msg_str = msg.as_string()
    # login smtp server
    server = smtplib.SMTP(host="smtp.gmail.com", port=587)
    server.ehlo()
    server.starttls()
    server.login(username, password)
    server.sendmail(from_email, to_emails, msg_str)

    server.quit()