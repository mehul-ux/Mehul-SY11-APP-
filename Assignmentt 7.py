"""Find and validate email addresses using regex."""
 
import re
 
EMAIL_PATTERN = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9.-]+'
 
 
def find_emails(text: str) -> list[str]:
    """Return all email addresses found anywhere in the text."""
    return re.findall(EMAIL_PATTERN, text)
 
 
def is_valid_email(email: str) -> bool:
    """Return True if the entire string is a valid email address."""
    return re.fullmatch(EMAIL_PATTERN, email) is not None
 
 
if __name__ == "__main__":
    text = """
    Contact us: support@example.com or sales.team@business.co.in
    Not valid: plain.text@, @missing-local.com
    """
 
    print("Emails found:")
    for email in find_emails(text):
        print(f"  {email}")
 
    print("\nValidation:")
    for candidate in ["john@example.com", "invalid-email", "user@site.com"]:
        status = "VALID" if is_valid_email(candidate) else "INVALID"
        print(f"  {candidate:20s} -> {status}")
 