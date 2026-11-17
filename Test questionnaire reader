
from pathlib import Path

from document_processing.questionnaire_reader import (
    extract_pptx
)


PROJECT_ROOT = Path(__file__).resolve().parent.parent

QUESTIONNAIRE_PATH = PROJECT_ROOT / "questionnaire.pptx"

with open(QUESTIONNAIRE_PATH, "rb") as file:

    file_bytes = file.read()

extracted_text = extract_pptx(file_bytes)

print("\n========== EXTRACTED POWERPOINT TEXT ==========\n")

print(extracted_text)

output_path = (
    PROJECT_ROOT / "output" / "questionnaire_text.txt"
)

output_path.parent.mkdir(
    parents=True,
    exist_ok=True
)

output_path.write_text(
    extracted_text,
    encoding="utf-8"
)

print("\nExtracted text saved to:", output_path)
