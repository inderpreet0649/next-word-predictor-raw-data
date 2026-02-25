import re
import string

def clean_seed(text, input_len):
    text = text.lower()
    text = re.sub(f"[{string.punctuation}]", "", text)
    text = re.sub(r"\s+", " ", text)
    words = text.split()
    return " ".join(words[-input_len:])

def get_prediction(seed, lookup_dict, input_len=10):
    processed = clean_seed(seed, input_len)

    if processed in lookup_dict:
        return lookup_dict[processed]
    else:
        return "❌ No matching sequence found in PDF."
