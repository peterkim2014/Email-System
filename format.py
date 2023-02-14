msg_text = """
    Dear {customer},
        Thank you for using our service.
        New updates will be available soon.

    Best regards,
    {company}
"""

def format_text(my_customer, my_company):
    msg = msg_text.format(customer=my_customer, company=my_company)
    return msg
