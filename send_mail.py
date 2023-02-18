import smtplib

username="program.python.test@gmail.com"
password = "hfzuhitpywagszzg"

def send_mail(text, subject, to_emails=None):
    assert isinstance(to_emails, list)

    # login smtp server
    server = smtplib.SMTP(host="smtp.gmail.com", port=587)
    server.ehlo()
    server.starttls()
    server.login(username, password)

    server.quit()