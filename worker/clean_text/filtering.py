# worker/text_cleaning/filtering.py

from typing import List
from .paragraphs import clean_paragraph_text, is_noise, is_arabic

def filter_and_clean_paragraphs(paragraphs: List[str]) -> List[str]:
    """
    Apply the cleaning pipeline to raw EPUB paragraphs:
    - Remove noise (page numbers, decorative lines, empty lines)
    - Remove Arabic text (English-only ingestion v1)
    - Clean and normalize remaining English paragraphs
    """
    cleaned: List[str] = []

    for p in paragraphs:
        if p is None:
            continue

        # Drop noise chunks entirely
        if is_noise(p):
            continue

        # Drop Arabic paragraphs (for English-only ingestion)
        if is_arabic(p):
            continue

        # Clean the remaining English paragraph
        content = clean_paragraph_text(p)

        if content:  # only keep if something remains after cleaning
            cleaned.append(content)

    return cleaned