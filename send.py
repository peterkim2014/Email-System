from format import format_text
import sys
from send_mail import send_mail

def send(customer, company, to_email=None):
    # assert to_email != None
    my_msg = format_text(my_customer=customer, my_company=company)
    subject = "Test"
    try:
        send_mail(text=my_msg, subject=subject, to_emails=[to_email])
        print(to_email)
        sent = True
    except:
        sent = False
    return sent

if __name__ == "__main__":
    if len(sys.argv) > 1:
        customer = sys.argv[1]
    if len(sys.argv) > 2:
        company = sys.argv[2]
    if len(sys.argv) > 3:
        email = sys.argv[3]

    response = send(customer, company, email)
    print(response)