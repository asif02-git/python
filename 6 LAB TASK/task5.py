# Task 5: Practical Applications
import re

# 5.1 Email Validator
def is_valid_email(s):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$"
    return bool(re.match(pattern, s))

emails = [
    "user@example.com", "john.doe@domain.co.uk", "a@b.c", "valid123@sub.domain.org",  # Valid
    "no-at-sign.com", "user@.com", "user@domain", "user@domain.toolongtld"          # Invalid
]
print("Task 5.1 - Email Validation Results:")
for e in emails:
    print(f"  '{e}': {is_valid_email(e)}")

# 5.2 Phone Number Extractor & Normalizer
raw_text = "Call us at 555-123-4567, (555) 123-4567, or 555.123.4567."
phone_pattern = r"\(?(\d{3})\)?[-.\s]?(\d{3})[-.\s]?(\d{4})"
normalized_text = re.sub(phone_pattern, r"\1-\2-\3", raw_text)
print("\nTask 5.2 - Normalized Phone Numbers:")
print("  ", normalized_text)

# 5.3 Date Extraction and Reformatting
dates_text = "Events are scheduled for 15/08/2024 and 01/12/2025."
extracted_dates = re.findall(r"\b(\d{2})/(\d{2})/(\d{4})\b", dates_text)
iso_dates_text = re.sub(r"\b(\d{2})/(\d{2})/(\d{4})\b", r"\3-\2-\1", dates_text)
print("\nTask 5.3 - Date Reformatting:")
print("  Extracted Tuples:", extracted_dates)
print("  ISO Format Text:", iso_dates_text)

# 5.4 Whitespace and HTML Cleanup
def clean_text(html):
    text_no_tags = re.sub(r"<[^>]+>", "", html)
    collapsed_spaces = re.sub(r"\s+", " ", text_no_tags)
    return collapsed_spaces.strip()

html_sample = "<div> <h1> Title </h1> \n <p> This is   a <b>sample</b> text. </p></div>"
print("\nTask 5.4 - Cleaned HTML Text:")
print("  ", repr(clean_text(html_sample)))

# 5.5 Password Strength Checker
def check_password(pw):
    failed_rules = []
    if len(pw) < 8:
        failed_rules.append("Must be at least 8 characters long")
    if not re.search(r"[A-Z]", pw):
        failed_rules.append("Must contain at least one uppercase letter")
    if not re.search(r"[a-z]", pw):
        failed_rules.append("Must contain at least one lowercase letter")
    if not re.search(r"\d", pw):
        failed_rules.append("Must contain at least one digit")
    if not re.search(r"[!@#$%^&*]", pw):
        failed_rules.append("Must contain at least one symbol (!@#$%^&*)")
    return failed_rules

passwords_to_test = ["Pass123!", "weak", "NoDigits!", "12345678"]
print("\nTask 5.5 - Password Checker:")
for pw in passwords_to_test:
    failures = check_password(pw)
    status = "VALID" if not failures else f"FAILED: {failures}"
    print(f"  '{pw}': {status}")