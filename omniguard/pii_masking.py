import re

class Masker:
    """Detects and masks PII (Personally Identifiable Information)."""
    
    def __init__(self):
        self.patterns = {
            "email": r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+',
            "phone": r'\+?\d{1,4}?[-.\s]?\(?\d{1,3}?\)?[-.\s]?\d{1,4}[-.\s]?\d{1,4}[-.\s]?\d{1,9}'
        }

    def mask(self, text: str) -> str:
        masked_text = text
        for label, pattern in self.patterns.items():
            masked_text = re.sub(pattern, f"<{label.upper()}>", masked_text)
        return masked_text
