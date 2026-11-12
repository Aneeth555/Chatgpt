
import json
from pathlib import Path

from processing.merge_results import merge_extractions


# ============================================================
# STEP 1: PROJECT PATHS
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

OUTPUT_DIR = PROJECT_ROOT / "output"

QUESTIONNAIRE_FILE = (
    OUTPUT_DIR / "questionnaire_extraction.json"
)

WEB_FILE = OUTPUT_DIR / "web_extraction.json"

FINAL_FILE = OUTPUT_DIR / "final_one_pager.json"

PROVENANCE_FILE = OUTPUT_DIR / "extraction_sources.json"


# ============================================================
# STEP 2: LOAD INPUT FILES
# ============================================================

for file_path in [QUESTIONNAIRE_FILE, WEB_FILE]:

    if not file_path.exists():
        raise FileNotFoundError(
            f"Required file not found: {file_path}"
        )

with open(
    QUESTIONNAIRE_FILE,
    "r",
    encoding="utf-8"
) as file:

    questionnaire_data = json.load(file)

with open(
    WEB_FILE,
    "r",
    encoding="utf-8"
) as file:

    web_results = json.load(file)


# ============================================================
# STEP 3: MERGE RESULTS
# ============================================================

print("=" * 60)
print("ONE-PAGER GENERATOR - DATA MERGING")
print("=" * 60)

final_data, provenance = merge_extractions(
    questionnaire_data=questionnaire_data,
    web_results=web_results
)


# ============================================================
# STEP 4: SAVE FINAL JSON
# ============================================================

with open(
    FINAL_FILE,
    "w",
    encoding="utf-8"
) as file:

    json.dump(
        final_data,
        file,
        indent=2,
        ensure_ascii=False
    )


# ============================================================
# STEP 5: SAVE SOURCE INFORMATION SEPARATELY
# ============================================================

with open(
    PROVENANCE_FILE,
    "w",
    encoding="utf-8"
) as file:

    json.dump(
        provenance,
        file,
        indent=2,
        ensure_ascii=False
    )


# ============================================================
# STEP 6: DISPLAY FINAL RESULTS
# ============================================================

print("\nPydantic validation successful.")

print("\n========== FINAL ONE-PAGER JSON ==========")

print(
    json.dumps(
        final_data,
        indent=2,
        ensure_ascii=False
    )
)


# ============================================================
# STEP 7: SUMMARY
# ============================================================

questionnaire_count = sum(
    1 for item in provenance.values()
    if item["selected_source"] == "questionnaire"
)

web_count = sum(
    1 for item in provenance.values()
    if item["selected_source"] == "web"
)

missing_count = sum(
    1 for item in provenance.values()
    if item["selected_source"] is None
)

print("\n========== MERGE SUMMARY ==========")

print("Questionnaire answers:", questionnaire_count)
print("Web answers:", web_count)
print("Unanswered fields:", missing_count)

print("\nFinal JSON saved:", FINAL_FILE)
print("Source information saved:", PROVENANCE_FILE)

print("\nMerging completed successfully.")
