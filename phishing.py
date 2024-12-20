import re
from urllib.parse import urlparse

# List of suspicious words commonly used in phishing attempts
suspicious_keywords = ["urgent", "verify", "click here", "bank account", "suspended"]

# Function to check for suspicious keywords
def check_keywords(message):
    for keyword in suspicious_keywords:
        if keyword.lower() in message.lower():
            return True
    return False

# Function to check if a URL looks suspicious (basic check)
def check_url(message):
    urls = re.findall(r'https?://\S+', message)  # Extract URLs starting with http(s)
    for url in urls:
        parsed_url = urlparse(url)
        suspicious_domains = ["bit.ly", "tinyurl.com", "goo.gl"]
        if parsed_url.netloc in suspicious_domains:
            return True
    return False

# Function to analyze the SMS message
def analyze_sms(message):
    if check_keywords(message):
        print("Warning: Suspicious keywords detected!")
    if check_url(message):
        print("Warning: Suspicious URL detected!")
    if not check_keywords(message) and not check_url(message):
        print("This message seems safe.")

# Take input from the user
sms_message = input("Enter the SMS message to analyze: ")

# Analyze the message
analyze_sms(sms_message)



'''
Your bank account has been suspended! Click here to verify: https://bit.ly/abc123
Please confirm your account information here: https://tinyurl.com/xyz789'''
