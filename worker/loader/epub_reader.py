from pathlib import Path
from typing import List

from ebooklib import epub, ITEM_DOCUMENT
from bs4 import BeautifulSoup


def extract_paragraphs_from_epub(epub_path: str | Path) -> List[str]:
    epub_path = Path(epub_path)

    if not epub_path.exists():
        raise FileNotFoundError(f"EPUB file not found: {epub_path}")

    book = epub.read_epub(epub_path)
    paragraphs: List[str] = []

    for item in book.get_items():
        if item.get_type() == ITEM_DOCUMENT:
            soup = BeautifulSoup(item.get_content(), "html.parser")

            for p in soup.find_all("p"):
                text = p.get_text(separator=" ", strip=True)
                if text:
                    paragraphs.append(text)

    return paragraphs
