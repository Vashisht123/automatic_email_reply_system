def handle_review(email_text):
    if "positive" in email_text.lower():
        return "Thank you for your positive review! Please share your experience on social media."
    elif "negative" in email_text.lower():
        return "We're sorry for your experience. A customer service representative will follow up with you soon and you will receive a gift voucher."
    else:
        return "Thank you for your feedback."
