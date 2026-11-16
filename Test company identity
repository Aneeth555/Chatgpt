
from processing.company_identity import (
    verify_company_identity,
    filter_search_results_by_identity
)


company_name = "Assessli"
official_domain = "assessli.com"


# ============================================================
# Sample search results
# ============================================================

sample_results = [
    {
        "title": "Assessli - Official Website",
        "url": "https://www.assessli.com/",
        "snippet": "Assessli provides AI-powered solutions.",
        "domain": "assessli.com"
    },
    {
        "title": "Assessli Company Profile",
        "url": "https://www.linkedin.com/company/assessli/",
        "snippet": "Assessli company information.",
        "domain": "linkedin.com"
    },
    {
        "title": "Assessio Alternatives and Competitors",
        "url": "https://example.com/assessio-alternatives",
        "snippet": "Assessio provides talent assessment solutions.",
        "domain": "example.com"
    },
    {
        "title": "Assessli Competitors",
        "url": "https://example.com/assessli-competitors",
        "snippet": "Competitors of Assessli in its market.",
        "domain": "example.com"
    },
    {
        "title": "General AI Company Information",
        "url": "https://example.com/ai-companies",
        "snippet": "Information about several AI companies.",
        "domain": "example.com"
    }
]


# ============================================================
# Individual verification test
# ============================================================

print("\n========== INDIVIDUAL TEST ==========")

for result in sample_results:

    verification = verify_company_identity(
        company_name=company_name,
        result=result,
        official_domain=official_domain
    )

    print("\nTitle:", result["title"])
    print("Verified:", verification["verified"])
    print("Reason:", verification["reason"])


# ============================================================
# Grouped search-output test
# ============================================================

print("\n========== GROUPED OUTPUT TEST ==========")

search_output = {
    "competitors": {
        "section": "company",
        "query": "Assessli competitors",
        "results": sample_results
    }
}

filtered_output = filter_search_results_by_identity(
    search_output=search_output,
    company_name=company_name,
    official_domain=official_domain
)

print("\nAccepted result count:",
      len(filtered_output["competitors"]["results"]))

print("Rejected result count:",
      len(filtered_output["competitors"]["rejected_results"]))
