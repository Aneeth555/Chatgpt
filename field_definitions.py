# ============================================================
# ONE-PAGER FIELD DEFINITIONS
# ============================================================
# This file defines what information belongs in each field.
#
# Both questionnaire extraction and web extraction will
# use these definitions.
#
# Important:
# - Do not guess missing information.
# - Return null if the field is not supported by evidence.
# - Distinguish similar fields carefully.
# ============================================================

FIELD_DEFINITIONS = {

    # ========================================================
    # COMPANY INFORMATION
    # ========================================================

    "company": {

        "company_name": {
            "description": (
                "The official name of the company that owns, "
                "develops, or provides the product."
            ),
            "extract": (
                "Use the company name supplied by the user. "
                "Do not replace it with another organization name."
            ),
            "example": "Assessli"
        },

        "overview": {
            "description": (
                "A brief introduction to the company, including "
                "its main business, products, services, and "
                "primary area of operation."
            ),
            "extract": (
                "Summarize what the company does, what it offers, "
                "and the problems it addresses."
            ),
            "example": (
                "An AI technology company developing personalized "
                "behavioral intelligence solutions."
            )
        },

        "headquarters": {
            "description": (
                "The official headquarters location of the company."
            ),
            "extract": (
                "Identify the city and country, or the full "
                "address if explicitly available."
            ),
            "example": "Bengaluru, India"
        },

        "employee_count": {
            "description": (
                "The total number of employees working at the company."
            ),
            "extract": (
                "Extract an explicitly stated employee count "
                "or employee range. Do not confuse followers, "
                "customers, or users with employees."
            ),
            "example": "51-200 employees"
        },

        "funding": {
            "description": (
                "The external funding raised or received by "
                "the company."
            ),
            "extract": (
                "Include disclosed funding amounts, funding rounds, "
                "grants, or investment information. Preserve the "
                "currency and funding stage when available."
            ),
            "example": "$400K USD in seed funding"
        },

        "revenue": {
            "description": (
                "The company's reported or reliably disclosed "
                "business revenue."
            ),
            "extract": (
                "Extract revenue figures only when supported by "
                "the source. Preserve currency, financial year, "
                "and reporting period when available. Do not "
                "confuse funding with revenue."
            ),
            "example": "$5.2 million annual revenue"
        },

        "gtm_partners": {
            "description": (
                "Organizations that help the company bring its "
                "products or services to customers."
            ),
            "extract": (
                "Identify named sales partners, channel partners, "
                "resellers, distributors, implementation partners, "
                "or strategic go-to-market partners."
            ),
            "example": "Partner A and Partner B"
        },

        "key_customers": {
            "description": (
                "Named companies or organizations that purchase, "
                "use, or have officially adopted the company's "
                "products or services."
            ),
            "extract": (
                "Include explicitly identified customers, client "
                "organizations, or documented deployments. Do not "
                "treat partners, investors, or general target "
                "audiences as customers."
            ),
            "example": "Customer A and Customer B"
        },

        "competitors": {
            "description": (
                "Companies or products offering competing solutions "
                "in the same or closely related market."
            ),
            "extract": (
                "Identify competitors that offer similar products "
                "or solve similar customer problems. Do not list "
                "technology providers or partners as competitors "
                "without supporting evidence."
            ),
            "example": "Company A, Company B"
        }
    },


    # ========================================================
    # PRODUCT INFORMATION
    # ========================================================

    "product": {

        "product_name": {
            "description": (
                "The official name of the specific product or "
                "platform being described."
            ),
            "extract": (
                "Use the product name supplied by the user. "
                "Do not substitute the company name unless "
                "the product genuinely has the same name."
            ),
            "example": "Dotsin"
        },

        "description": {
            "description": (
                "A concise explanation of what the product is, "
                "what it does, and which problem it solves."
            ),
            "extract": (
                "Describe the product's main functionality, "
                "purpose, and value proposition."
            ),
            "example": (
                "An AI platform that learns individual behavior "
                "and provides personalized intelligence."
            )
        },

        "vertical_market": {
            "description": (
                "The industries, business sectors, or application "
                "domains that the product serves."
            ),
            "extract": (
                "Identify the markets where the product is used, "
                "such as healthcare, finance, education, "
                "manufacturing, or retail."
            ),
            "example": "Healthcare, education and personalized learning"
        },

        "route_to_market": {
            "description": (
                "The commercial channels and selling methods "
                "through which the product reaches customers."
            ),
            "extract": (
                "Identify whether the product is sold through "
                "direct sales, SaaS subscriptions, channel partners, "
                "resellers, distributors, online marketplaces, "
                "OEM agreements, or another explicitly stated "
                "commercial channel."
            ),
            "example": (
                "Direct enterprise sales and subscription-based "
                "SaaS distribution."
            ),
            "important_distinction": (
                "Route to market describes HOW the product is sold "
                "or distributed. It does not describe WHERE the "
                "software runs. Cloud, edge and on-premises are "
                "deployment types, not route-to-market answers."
            )
        },

        "inference_hardware": {
            "description": (
                "The hardware used to execute trained AI or "
                "machine learning models during inference."
            ),
            "extract": (
                "Identify inference CPUs, GPUs, accelerators, "
                "servers, or cloud instance types explicitly "
                "used or specified for inference."
            ),
            "example": "Intel Xeon CPUs and AWS C6i instances"
        },

        "deployment_type": {
            "description": (
                "The environment or infrastructure where the "
                "product or its software components are deployed."
            ),
            "extract": (
                "Identify cloud, on-premises, edge, hybrid, "
                "or other deployment environments."
            ),
            "example": "Cloud, edge and on-premises"
        },

        "training_hardware": {
            "description": (
                "The hardware used to train or fine-tune "
                "AI or machine learning models."
            ),
            "extract": (
                "Identify training CPUs, GPUs, accelerators, "
                "servers, or cloud instance types."
            ),
            "example": "NVIDIA A100 and H100 GPUs"
        },

        "models": {
            "description": (
                "The specific AI or machine learning models, "
                "model architectures, or model families used "
                "by the product."
            ),
            "extract": (
                "Identify model names and architectures such "
                "as BERT, BioBERT, LLMs, CNNs, GNNs, or "
                "Temporal Graph Networks."
            ),
            "example": (
                "BioBERT with LoRA adapters, Graph Neural "
                "Networks and Temporal Graph Networks."
            )
        },

        "ai_framework": {
            "description": (
                "The software frameworks and libraries used "
                "to develop, train, or fine-tune AI models."
            ),
            "extract": (
                "Identify frameworks and libraries such as "
                "PyTorch, TensorFlow, Keras, JAX, PEFT, "
                "or Hugging Face Transformers."
            ),
            "example": "PyTorch, PEFT and Hugging Face Transformers"
        },

        "serving_framework": {
            "description": (
                "The software frameworks, runtimes, or engines "
                "used to deploy, serve, optimize, or execute "
                "AI models in production."
            ),
            "extract": (
                "Identify tools such as OpenVINO, vLLM, "
                "TensorRT, ONNX Runtime, Triton Inference "
                "Server, or TorchServe."
            ),
            "example": "OpenVINO and ONNX Runtime"
        },

        "additional_ai_software_stack": {
            "description": (
                "Other software and infrastructure supporting "
                "the AI product beyond its model development "
                "and model serving frameworks."
            ),
            "extract": (
                "Identify relevant databases, streaming systems, "
                "vector databases, graph databases, data pipelines, "
                "MLOps, orchestration, monitoring, and observability "
                "tools."
            ),
            "example": (
                "Kafka, Memgraph, MAGE, vector databases "
                "and MLOps tools."
            )
        }
    }
}


# ============================================================
# HELPER FUNCTION
# ============================================================

def get_field_definitions():

    """
    Returns the complete definitions of company and product fields.
    """

    return FIELD_DEFINITIONS


def get_section_definitions(section_name):

    """
    Returns definitions for a specific section.

    Valid sections:
    - company
    - product
    """

    return FIELD_DEFINITIONS.get(section_name, {})


def get_all_field_names():

    """
    Returns all one-pager field names.
    """

    return {
        section: list(fields.keys())
        for section, fields in FIELD_DEFINITIONS.items()
    }
