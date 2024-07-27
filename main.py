from email_classifier import classify_email
from inquiry_handler import handle_inquiry
from review_handler import handle_review
from assistance_handler import handle_assistance

def handle_general(email_text):
    return "Your email has been forwarded to customer service."

def main():
    # Example emails
    emails = [
        "I have an inquiry about Camera A",
        "This is a positive review of your service",
        "I need assistance with Light A"
    ]

    for email in emails:
        category = classify_email(email)
        if category == "inquiry":
            response = handle_inquiry(email)
        elif category == "review":
            response = handle_review(email)
        elif category == "assistance":
            response = handle_assistance(email)
        else:
            response = handle_general(email)
        print(f"Email: {email}\nResponse: {response}\n")

if __name__ == "__main__":
    main()
