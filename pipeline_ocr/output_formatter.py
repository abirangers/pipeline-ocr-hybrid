"""Format pipeline output into various representations."""
from typing import List, Dict
import json


def format_output(pages_data: List[Dict], fmt: str = "json") -> str:
    """Format pages data into a string representation.

    Args:
        pages_data: List containing layout information for each page.
        fmt: Output format, currently only ``json`` is supported.
    """
    if fmt != "json":
        raise ValueError(f"Unsupported format: {fmt}")
    return json.dumps(pages_data, ensure_ascii=False, indent=2)
