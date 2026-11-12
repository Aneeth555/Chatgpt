 
from schemas.one_pager_schema import OnePagerExtraction

# Generate the JSON schema that will be sent to Ollama
schema = OnePagerExtraction.model_json_schema()

print("Schema generated successfully.")
print("\nTop-level fields:")
print(list(schema["properties"].keys()))

print("\nCompany fields:")
print(list(schema["$defs"]["CompanyInformation"]["properties"].keys()))

print("\nProduct fields:")
print(list(schema["$defs"]["ProductInformation"]["properties"].keys()))

print("\nRoute to market definition:")
print(
    schema["$defs"]["ProductInformation"]
    ["properties"]["route_to_market"]["description"]
)
