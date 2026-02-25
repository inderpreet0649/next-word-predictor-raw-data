import re
import string

def normalize_text(text):
    text = text.lower()
    text = re.sub(f"[{string.punctuation}]", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()
