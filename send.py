from format import format_text
import sys

def send(customer, company):
    msg = format_text(my_customer=customer, my_company=company)
    return msg

if __name__ == "__main__":
    if len(sys.argv) > 1:
        customer = sys.argv[1]
    if len(sys.argv) > 2:
        company = sys.argv[2]

    response = send(customer, company)
    print(response)