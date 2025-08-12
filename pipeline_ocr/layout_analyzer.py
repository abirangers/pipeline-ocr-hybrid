"""Simple layout analysis for OCR items."""
from typing import List, Dict


def analyze_layout(ocr_items: List[Dict]) -> Dict:
    """Group OCR items into lines based on vertical proximity.

    This is a naive implementation that orders items by their y coordinate
    and groups them if they are close to each other.
    """
    if not ocr_items:
        return {"lines": [], "items": []}
    sorted_items = sorted(ocr_items, key=lambda x: x["bbox"][1])
    lines = []
    current_line = []
    current_y = sorted_items[0]["bbox"][1]
    threshold = 10

    for item in sorted_items:
        y = item["bbox"][1]
        if abs(y - current_y) <= threshold:
            current_line.append(item["text"])
        else:
            lines.append(" ".join(current_line))
            current_line = [item["text"]]
            current_y = y
    if current_line:
        lines.append(" ".join(current_line))
    return {"lines": lines, "items": ocr_items}
