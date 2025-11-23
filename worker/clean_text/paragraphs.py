import re

def clean_paragraph_text(text: str) -> str:
    """
    Basic cleanup for a single paragraph of text:
    - Strip leading/trailing whitespace
    - Normalize internal whitespace (multiple spaces -> one space)
    - Remove stray spaces before punctuation
    """
    if text is None:
        return ""

    # Strip leading/trailing whitespace
    cleaned = text.strip()

    # Replace any sequence of whitespace (spaces, tabs, newlines) with a single space
    cleaned = re.sub(r"\s+", " ", cleaned)

    # Remove spaces before common punctuation marks (e.g. 'word , word' -> 'word, word')
    cleaned = re.sub(r"\s+([.,;:!?])", r"\1", cleaned)

    return cleaned

def is_noise(text: str) -> bool:
    """
    Decide if a paragraph is 'noise' that we want to drop entirely.
    Examples of noise:
    - Empty strings or only whitespace
    - Just numbers (page numbers)
    - Decorative lines like '***', '-----', '*****'
    """
    if text is None:
        return True

    stripped = text.strip()

    # Empty or only whitespace
    if stripped == "":
        return True

    # Purely numeric (likely a page number)
    if stripped.isdigit():
        return True

    # Decorative line like '***', '----', '_____'
    if re.fullmatch(r"[\*\-\_=~\.]{3,}", stripped):
        return True

    return False

def is_arabic(text: str) -> bool:
    """
    Detect whether a paragraph contains Arabic script characters.
    Returns True if the text is primarily Arabic, False otherwise.
    """
    if text is None:
        return False

    # Arabic Unicode blocks
    arabic_pattern = r"[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDFF\uFE70-\uFEFF]"

    return bool(re.search(arabic_pattern, text))