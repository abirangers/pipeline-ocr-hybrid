"""OCR extraction utilities."""
from typing import List, Dict, Tuple
from PIL import Image
import pytesseract


def extract_text_from_image(image: Image.Image, lang: str = "eng+ind") -> List[Dict]:
    """Extract text and bounding boxes from an image.

    Args:
        image: PIL Image to process.
        lang: Tesseract language(s) specification. Defaults to ``"eng+ind"``
            which enables combined English and Indonesian OCR.

    Returns:
        A list of dicts containing ``text``, ``bbox`` and ``confidence``.
    """
    data = pytesseract.image_to_data(
        image, lang=lang, output_type=pytesseract.Output.DICT
    )
    items: List[Dict] = []
    n = len(data["text"])
    for i in range(n):
        text = data["text"][i].strip()
        if not text:
            continue
        bbox: Tuple[int, int, int, int] = (
            data["left"][i],
            data["top"][i],
            data["width"][i],
            data["height"][i],
        )
        conf = float(data["conf"][i])
        items.append({"text": text, "bbox": bbox, "confidence": conf})
    return items
