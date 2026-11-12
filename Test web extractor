
import json
from pathlib import Path

from llm.web_extractor import extract_from_web


# ============================================================
# STEP 1: PROJECT PATHS
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

OUTPUT_DIR = PROJECT_ROOT / "output"

EVIDENCE_FILE = OUTPUT_DIR / "filtered_evidence.json"

WEB_OUTPUT_FILE = OUTPUT_DIR / "web_extraction.json"


# ============================================================
# STEP 2: LOAD FILTERED EVIDENCE
# ============================================================

if not EVIDENCE_FILE.exists():

    raise FileNotFoundError(
        f"Filtered evidence not found: {EVIDENCE_FILE}"
    )

with open(
    EVIDENCE_FILE,
    "r",
    encoding="utf-8"
) as file:

    filtered_evidence = json.load(file)


# ============================================================
# STEP 3: DISPLAY INPUT SUMMARY
# ============================================================

print("=" * 60)
print("ONE-PAGER GENERATOR - WEB EXTRACTION TEST")
print("=" * 60)

print("Missing fields:", len(filtered_evidence))

for field, data in filtered_evidence.items():

    print(
        f"{field}: "
        f"{data.get('chunks_found', 0)} evidence chunks"
    )


# ============================================================
# STEP 4: EXTRACT INFORMATION USING QWEN
# ============================================================

web_results = extract_from_web(
    filtered_evidence
)


# ============================================================
# STEP 5: SAVE RESULTS
# ============================================================

with open(
    WEB_OUTPUT_FILE,
    "w",
    encoding="utf-8"
) as file:

    json.dump(
        web_results,
        file,
        indent=2,
        ensure_ascii=False
    )


# ============================================================
# STEP 6: DISPLAY FINAL RESULTS
# ============================================================

print("\n" + "=" * 60)
print("WEB EXTRACTION RESULTS")
print("=" * 60)

for field, result in web_results.items():

    print(f"\nField: {field}")
    print("Section:", result["section"])
    print("Answer:", result["answer"])
    print("Status:", result["status"])
    print("Evidence:", result.get("evidence"))
    print("Source:", result.get("source_url"))


# ============================================================
# STEP 7: SUMMARY
# ============================================================

successful = sum(
    1 for result in web_results.values()
    if result["status"] == "extracted"
)

null_fields = len(web_results) - successful

print("\n========== EXTRACTION SUMMARY ==========")

print("Total fields:", len(web_results))
print("Successfully extracted:", successful)
print("Unanswered or rejected:", null_fields)

print("\nSaved to:", WEB_OUTPUT_FILE)

print("\nWeb extraction completed.")
