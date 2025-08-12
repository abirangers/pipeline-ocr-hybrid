import json
from pathlib import Path
import sys

# Ensure the package can be imported when tests run from a different cwd
sys.path.append(str(Path(__file__).resolve().parents[1]))

from fpdf import FPDF

from pipeline_ocr.main import run_pipeline


def _create_sample_pdf(path: Path) -> Path:
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(0, 10, txt="Hello World", ln=True)
    pdf.output(str(path))
    return path


def test_pipeline_extracts_text(tmp_path: Path):
    pdf_path = _create_sample_pdf(tmp_path / "sample.pdf")
    result = run_pipeline(str(pdf_path), lang="eng", fmt="json")
    data = json.loads(result)
    combined = json.dumps(data)
    assert "Hello World" in combined
