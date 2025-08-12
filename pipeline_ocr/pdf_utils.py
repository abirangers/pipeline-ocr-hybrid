"""Utilities for working with PDF files."""
from typing import List
from PIL import Image
from pdf2image import convert_from_path
import os


def convert_pdf_to_images(pdf_path: str) -> List[Image.Image]:
    """Convert a PDF file into a list of PIL Image objects.

    Args:
        pdf_path: Path to the PDF file.

    Returns:
        List of images, one per page of the PDF.

    Raises:
        FileNotFoundError: If the file does not exist.
        RuntimeError: If conversion fails.
    """
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"PDF file {pdf_path} not found")
    try:
        images = convert_from_path(pdf_path)
    except Exception as exc:  # pragma: no cover - external dependency errors
        raise RuntimeError(f"Failed to convert PDF to images: {exc}") from exc
    return images
