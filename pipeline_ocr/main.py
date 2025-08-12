"""Command line interface for the OCR pipeline."""
from __future__ import annotations
import argparse
from typing import List, Dict

from .pdf_utils import convert_pdf_to_images
from .ocr_engine import extract_text_from_image
from .layout_analyzer import analyze_layout
from .output_formatter import format_output


def run_pipeline(input_pdf: str, lang: str = "eng+ind", fmt: str = "json") -> str:
    """Run the OCR pipeline and return formatted output string.

    Args:
        input_pdf: Path to the PDF file to process.
        lang: Language codes for Tesseract OCR. Defaults to ``"eng+ind"``
            to recognise both English and Indonesian text.
        fmt: Output format. ``"json"`` or ``"txt"``.
    """
    images = convert_pdf_to_images(input_pdf)
    pages: List[Dict] = []
    for image in images:
        ocr_items = extract_text_from_image(image, lang=lang)
        layout = analyze_layout(ocr_items)
        pages.append(layout)
    return format_output(pages, fmt=fmt)


def main() -> None:
    parser = argparse.ArgumentParser(description="Pipeline OCR Hybrid")
    parser.add_argument("--input", required=True, help="Path to input PDF file")
    parser.add_argument("--output", required=True, help="Path to output file")
    parser.add_argument(
        "--lang",
        default="eng+ind",
        help="Tesseract language codes (e.g. 'eng+ind' for English+Indonesian)",
    )
    parser.add_argument(
        "--format",
        default="json",
        help="Output format (json or txt)",
    )
    args = parser.parse_args()

    result = run_pipeline(args.input, lang=args.lang, fmt=args.format)
    with open(args.output, "w", encoding="utf-8") as f:
        f.write(result)


if __name__ == "__main__":
    main()
