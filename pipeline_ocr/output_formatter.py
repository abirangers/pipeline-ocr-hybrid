"""Format pipeline output into various representations."""
from typing import List, Dict
import json


def format_output(pages_data: List[Dict], fmt: str = "json") -> str:
    """Format pages data into a string representation.

    Args:
        pages_data: List containing layout information for each page.
        fmt: Output format. Supports ``json`` and ``txt``.
    """
    if fmt == "json":
        return json.dumps(pages_data, ensure_ascii=False, indent=2)
    if fmt == "txt":
        pages = []
        for page in pages_data:
            lines = page.get("lines", [])
            pages.append("\n".join(lines))
        return "\n\n".join(pages)
    raise ValueError(f"Unsupported format: {fmt}")
