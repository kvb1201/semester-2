# Create a tokenizer for your own language (mother tongue you speak). The tokenizer should
# tokenize punctuations, dates, urls, emails, numbers (in all different forms such as “33.15”,

# “3,22,243”, “313/77”), social media usernames/user handles. Use regular expressions to design
# this. [Hint: Use unicode blocks for your language, check wikipedia pages]
import re

def custom_tokenizer(text):
    patterns = {
        "dates": r"\b\d{1,2}[-/]\d{1,2}[-/]\d{2,4}\b",
        "urls": r"https?://[^\s]+",
        "emails": r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
        "numbers": r"\b\d{1,3}(?:,\d{3})*(?:\.\d+)?\b",
        "usernames": r"@[a-zA-Z0-9_]+",
        "punctuation": r"[,.!?;:]"
    }
    
    tokens = []
    for category, pattern in patterns.items():
        matches = re.findall(pattern, text)
        if matches:
            tokens.extend(matches)

    return tokens

print(custom_tokenizer("www.google.com"))