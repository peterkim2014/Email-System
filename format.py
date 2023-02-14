msg_text = """
Dear {customer},
    Thank you for using our service.
    New updates will be available soon.

Best regards,
{company}
"""

def format_text(customer, company):
    msg_text.format(customer=customer, company=company)
    return msg_text