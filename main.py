# Phishing Email analyzer

import email
import re

def print_email_headers(eml_file):
  # Parse the email file
  with open(eml_file, "rb") as f:
    msg = email.message_from_binary_file(f)

  # Print the email's headers
  print("Email Header Info -")
  print("From:", msg["From"])
  print("To:", msg["To"])
  print("Subject:", msg["Subject"])
  print("Date:", msg["Date"])
  print("Message-ID:", msg["Message-ID"])

  
  
# Analyzing email headers
def get_domain_from_email(email):
    # Use a regular expression to extract the domain from the email
    domain = re.search("@([^@]+)", email).group(1)
    return domain
    
def analyze_email_headers(eml_file):
    # Parse the email file
    with open(eml_file, "rb") as f:
        msg = email.message_from_binary_file(f)

    # Extract the domain name of the sender's email address
    sender = msg["From"]
    sender_domain = get_domain_from_email(sender[:-1])
    # Check the "To" header for multiple recipients
    recipients = msg["To"]
    if "," in recipients:
        print("Warning: Email was sent to multiple recipients")

    # Check for suspicious "Subject" and "Date" values
    subject = msg["Subject"]
    date = msg["Date"]
    if "urgent" in subject.lower():
        print("Warning: Subject line contains the word 'urgent'")
    if "suspicious_date" in date:
        print("Warning: Email was sent from a suspicious date")

    # Check for suspicious "Message-ID" values
    message_id = msg["Message-ID"]
    if "fake_id" in message_id:
        print("Warning: Email has a fake message ID")

# Example usage:
eml_file = "test.eml"
print_email_headers(eml_file)
analyze_email_headers(eml_file)

