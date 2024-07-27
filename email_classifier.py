def classify_email(email_text):
    if "inquiry" in email_text.lower():
        return "inquiry"
    elif "review" in email_text.lower():
        return "review"
    elif "assist" in email_text.lower():
        return "assistance"
    else:
        return "general"
