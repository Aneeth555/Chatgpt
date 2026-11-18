
# ============================================================
# ONE-PAGER FIELD DEFINITIONS
# ============================================================

FIELD_DEFINITIONS = {

    # ========================================================
    # COMPANY INFORMATION
    # ========================================================

    "company": {

        "company_name": {
            "display_name": "Company Name",
            "description": "The official name of the company being profiled.",
            "what_to_extract": "The company's official and complete name.",
            "what_not_to_extract": "Product names, brand names or names of partner companies unless they are also the actual company name.",
            "answer_format": "Company name only.",
            "source_guidance": "Prefer the official company website and explicit company identification in the questionnaire."
        },

        "overview": {
            "display_name": "Company Overview",
            "description": "A concise overview of what the company does, its business, purpose, technology, products and core capabilities.",
            "what_to_extract": "The company's main business activities, problems it solves, technology, products, services and important capabilities. Combine relevant information from different parts of the questionnaire when necessary.",
            "what_not_to_extract": "An unrelated product-only description, unsupported claims, marketing slogans or speculative future capabilities.",
            "answer_format": "A concise paragraph describing the company's business and core activities.",
            "source_guidance": "Use the official company description and relevant questionnaire information."
        },

        "headquarters": {
            "display_name": "HQ",
            "description": "The actual headquarters location of the company.",
            "what_to_extract": "The city, state, region or country explicitly identified as the company's headquarters or primary headquarters.",
            "what_not_to_extract": "Registered office, branch office, regional office, mailing address, customer address or an address whose relationship to the company's headquarters is unclear.",
            "answer_format": "Location in a concise format, preserving the available city, state and country information.",
            "source_guidance": "Prefer an explicit headquarters statement from the official company website or questionnaire."
        },

        "employee_count": {
            "display_name": "Employees",
            "description": "The total number or range of employees working for the company.",
            "what_to_extract": "An explicitly stated company-wide employee count or employee-size range. Preserve the original range and any associated units.",
            "what_not_to_extract": "Number of LinkedIn profiles displayed, followers, team members listed on a webpage, job openings or employee counts belonging to another organization.",
            "answer_format": "Preserve the explicitly stated employee number or range.",
            "source_guidance": "Use explicit company-size statements, employee counts or reliable company profile information. Do not infer the count from unrelated people listings."
        },

        "funding": {
            "display_name": "Funding",
            "description": "The funding or investment capital raised by the company.",
            "what_to_extract": "Explicitly disclosed funding amounts, investment rounds, grants or total capital raised. Preserve currency, amount and funding stage when available.",
            "what_not_to_extract": "Company revenue, valuation, projected revenue, investment targets, funding requirements or unconfirmed investment discussions.",
            "answer_format": "Concise funding amount and currency, with funding round or stage when available.",
            "source_guidance": "Prefer explicit company disclosures, official announcements and credible funding reports."
        }
    },
    
    # ========================================================
    # REMAINING COMPANY FIELDS
    # ========================================================

    "company": {

        "revenue": {
            "display_name": "Revenue",
            "description": "The company's actual reported or explicitly disclosed business revenue.",
            "what_to_extract": "Explicit revenue figures, annual revenue, recurring revenue or other clearly identified revenue metrics. Preserve the amount, currency and reporting period.",
            "what_not_to_extract": "Funding, investment, valuation, profit, market size, transaction volume, projected revenue or customer spending unless explicitly identified as company revenue.",
            "answer_format": "Preserve the original amount, currency, unit and reporting period.",
            "source_guidance": "Prefer explicit financial disclosures, company statements and credible financial reporting."
        },

        "gtm_partners": {
            "display_name": "GTM Partners",
            "description": "Organizations that help the company commercialize, market, sell or distribute its products and services.",
            "what_to_extract": "Sales partners, distribution partners, reseller partners, channel partners and commercial go-to-market alliances.",
            "what_not_to_extract": "Technical integration partners, cloud infrastructure providers, research collaborators, investors or customers unless they are explicitly identified as commercial go-to-market partners.",
            "answer_format": "Partner organization names, optionally with their commercial relationship.",
            "source_guidance": "Require an explicit or clearly supported commercial relationship."
        },

        "key_customers": {
            "display_name": "Key Customers",
            "description": "Important organizations that purchase, use or are explicitly identified as customers of the company or its products.",
            "what_to_extract": "Named customers, enterprise clients, organizations using the product and publicly disclosed customer relationships.",
            "what_not_to_extract": "Partners, investors, suppliers, technology providers, research collaborators or potential customers unless they are explicitly identified as customers.",
            "answer_format": "Customer organization names, optionally with a brief description of their relationship.",
            "source_guidance": "Prefer explicit customer announcements, case studies and company disclosures."
        },

        "competitors": {
            "display_name": "Main Competitors",
            "description": "Companies offering competing products or solutions that address similar customer needs or markets.",
            "what_to_extract": "Direct competitors offering comparable products, services or technology solutions.",
            "what_not_to_extract": "Every company in the same industry, general technology providers, partners, suppliers or customers without a competitive relationship.",
            "answer_format": "Names of relevant competing companies.",
            "source_guidance": "Prefer explicit competitor identification or reliable comparisons demonstrating overlapping products and target markets."
        }
    },

    # ========================================================
    # PRODUCT INFORMATION
    # ========================================================

    "product": {

        "product_name": {
            "display_name": "Product Name",
            "description": "The name of the specific product being profiled.",
            "what_to_extract": "The official name of the product or solution provided as input or identified in the questionnaire.",
            "what_not_to_extract": "Company names, unrelated product names or generic technology names.",
            "answer_format": "Product name only.",
            "source_guidance": "Treat the explicitly supplied product name as authoritative unless the user corrects it."
        },

        "description": {
            "display_name": "Product Description",
            "description": "A description of the product's purpose, functionality, capabilities, technology and intended use cases.",
            "what_to_extract": "What the product does, the problem it solves, its main functionality, important features and intended applications. Combine relevant details from different questionnaire sections.",
            "what_not_to_extract": "The entire company overview, unrelated company activities, unsupported capabilities or future features presented as already implemented.",
            "answer_format": "A concise paragraph explaining the product and its main capabilities.",
            "source_guidance": "Use product-specific questionnaire answers and official product documentation."
        },

        "vertical_market": {
            "display_name": "Vertical Market",
            "description": "The industries, business sectors or application markets that the product serves or targets.",
            "what_to_extract": "Explicitly stated target industries, sectors and application domains. Relevant use cases may help identify a market when the questionnaire does not use the exact term vertical market.",
            "what_not_to_extract": "Programming languages, technology categories, deployment environments, customer names or broad industries that are not supported by the information.",
            "answer_format": "Concise industry or market-sector names.",
            "source_guidance": "Use explicit target-market statements and clearly supported product applications. Do not overstate the markets served."
        },

        "route_to_market": {
            "display_name": "Route to Market",
            "description": "The commercial strategy or channel through which the product is offered and reaches customers.",
            "what_to_extract": "Direct sales, indirect sales, channel partnerships, resellers, distributors, marketplaces, subscriptions or other explicitly stated commercial models.",
            "what_not_to_extract": "Cloud deployment, edge deployment, on-premises installation, technical architecture, infrastructure providers or development partnerships unless they also describe a commercial distribution channel.",
            "answer_format": "Concise description of the commercial sales or distribution model.",
            "source_guidance": "Require explicit information about how the product is sold, distributed, licensed or commercialized."
        }
    },
    
    # ========================================================
    # REMAINING PRODUCT FIELDS
    # ========================================================

    "product": {

        "inference_hardware": {
            "display_name": "Current Inference Hardware",
            "description": "The hardware currently used to execute trained AI models and perform inference.",
            "what_to_extract": "Currently used CPUs, GPUs, AI accelerators, servers and cloud compute instance types associated with model inference or production model execution.",
            "what_not_to_extract": "Hardware used only for model training, future inference hardware targets, general hardware recommendations or hardware not associated with inference.",
            "answer_format": "Concise description preserving processor names, accelerator names, instance types and specifications.",
            "source_guidance": "Prioritize explicit statements about the current inference or production environment. Distinguish currently deployed hardware from planned optimization targets."
        },

        "deployment_type": {
            "display_name": "Deployment Type",
            "description": "The environment and deployment model through which the product is made available or operated.",
            "what_to_extract": "Cloud, on-premises, edge, mobile, desktop, hybrid or other explicitly described deployment environments. Include primary deployment and supported alternatives.",
            "what_not_to_extract": "Training hardware, inference hardware, operating systems, programming languages or cloud providers unless they provide evidence of a deployment model.",
            "answer_format": "Concise deployment model, including primary and optional deployment environments when stated.",
            "source_guidance": "Distinguish the current deployment model from optional, supported or future deployment arrangements."
        },

        "training_hardware": {
            "display_name": "Current Training Hardware",
            "description": "The hardware currently used to train or fine-tune the product's AI models.",
            "what_to_extract": "Currently used CPUs, GPUs, accelerators, training servers and cloud GPU instance types explicitly associated with model training or fine-tuning.",
            "what_not_to_extract": "Inference-only hardware, general deployment hardware, future training infrastructure or hardware mentioned without a training relationship.",
            "answer_format": "Concise description preserving GPU, CPU, accelerator and instance names and specifications.",
            "source_guidance": "Prioritize explicit model-training infrastructure. Distinguish current training hardware from planned hardware."
        },

        "models": {
            "display_name": "Models",
            "description": "The AI models, model families and model architectures used by the product.",
            "what_to_extract": "Named pretrained models, foundation models, language models, computer vision models, model architectures, neural network types and relevant model variants.",
            "what_not_to_extract": "AI development frameworks, programming languages, databases, serving runtimes or general software tools unless they are themselves model names.",
            "answer_format": "Model names and architectures, with relevant versions or specifications when available.",
            "source_guidance": "Preserve exact model names, architecture names, versions and explicitly stated implementation details."
        },

        "ai_framework": {
            "display_name": "Current AI Framework",
            "description": "The AI and machine learning frameworks currently used to develop, train or fine-tune the product's models.",
            "what_to_extract": "Currently used AI development and training frameworks, machine learning libraries and model fine-tuning frameworks.",
            "what_not_to_extract": "Model names, hardware, databases, programming languages or inference runtimes unless they are explicitly being used as AI development or training frameworks.",
            "answer_format": "Framework and library names, preserving versions when available.",
            "source_guidance": "Prioritize explicitly identified frameworks currently used for model development, training or fine-tuning."
        },

        "serving_framework": {
            "display_name": "Current Serving Framework",
            "description": "The frameworks and runtimes currently used to deploy, serve, execute or optimize trained AI models for inference.",
            "what_to_extract": "Currently used model-serving frameworks, inference runtimes, model execution engines and inference optimization software.",
            "what_not_to_extract": "Training-only frameworks, model names, hardware, general-purpose cloud services or future serving targets presented as current implementations.",
            "answer_format": "Framework and runtime names. Clearly distinguish current implementations from planned or target tools.",
            "source_guidance": "Preserve implementation status. If a framework is described as a future target, do not present it as currently deployed."
        },

        "additional_ai_software_stack": {
            "display_name": "Additional AI Software Stack",
            "description": "Supporting AI, data and software technologies used alongside the main AI models and frameworks.",
            "what_to_extract": "Databases, vector databases, graph databases, data streaming platforms, message queues, data pipelines, MLOps tools, experiment tracking, model registries, CI/CD, orchestration, monitoring and observability technologies.",
            "what_not_to_extract": "Unnamed products invented from general categories, unrelated business software, hardware, model names or tools already better classified as the main AI framework or serving framework.",
            "answer_format": "Concise list of technology and tool names, optionally grouped by their purpose.",
            "source_guidance": "Preserve explicitly stated product and technology names. Generic categories may be included only when the questionnaire explicitly mentions those categories."
        }
    }
}


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def get_field_definitions():
    """
    Return all company and product field definitions.
    """
    return FIELD_DEFINITIONS


def get_section_definitions(section_name):
    """
    Return definitions belonging to a specific section.
    """
    return FIELD_DEFINITIONS.get(section_name, {})


def get_all_field_names():
    """
    Return all internal schema field names.
    """
    field_names = []

    for section in FIELD_DEFINITIONS.values():
        field_names.extend(section.keys())

    return field_names


def get_field_definition(field_name):
    """
    Find a field definition using its internal schema name.
    """
    for section in FIELD_DEFINITIONS.values():

        if field_name in section:
            return section[field_name]

    return None


def get_field_section(field_name):
    """
    Return the section containing a field.
    """
    for section_name, section in FIELD_DEFINITIONS.items():

        if field_name in section:
            return section_name

    return None
    
