
# schemas/field_definitions.py

"""
Shared field definitions for questionnaire and web extraction.
No company-specific example answers are provided.
"""

FIELD_DEFINITIONS = {

    # ============================================================
    # COMPANY INFORMATION
    # ============================================================

    "company": {

        "company_name": {
            "description": "The official name of the company.",
            "what_to_extract": (
                "Extract the official business name of the company "
                "identified by the user."
            ),
            "what_not_to_extract": (
                "Do not extract product names, brand names, subsidiary "
                "names, or partner company names."
            ),
            "answer_format": "Return only the company name.",
            "source_guidance": (
                "Prefer the official company website, official documents, "
                "and verified company profiles."
            )
        },

        "overview": {
            "description": (
                "A concise summary of the company's business, primary "
                "activities, technology, and value proposition."
            ),
            "what_to_extract": (
                "Identify what the company does, its main business "
                "activities, the problems it solves, and its value "
                "proposition."
            ),
            "what_not_to_extract": (
                "Do not provide only product names, customer lists, "
                "funding details, technical specifications, or generic "
                "marketing statements."
            ),
            "answer_format": (
                "Write a concise paragraph of approximately 2-4 sentences."
            ),
            "source_guidance": (
                "Prefer the official About Us page, company profile, "
                "official presentations, and company documentation."
            )
        },

        "headquarters": {
            "description": (
                "The company's primary headquarters or main corporate "
                "office location."
            ),
            "what_to_extract": (
                "Extract the address explicitly identified as the "
                "company's headquarters, head office, or main corporate "
                "office."
            ),
            "what_not_to_extract": (
                "Do not automatically treat a registered office, branch "
                "office, operational office, employee location, mailing "
                "address, or third-party office listing as headquarters. "
                "Do not select an address merely because it is the only "
                "address found."
            ),
            "answer_format": (
                "Return the available headquarters address, including "
                "city, state, and country where available."
            ),
            "source_guidance": (
                "Prefer the official company website and official "
                "company documents. Use reliable secondary sources "
                "only when the office type is clearly identified."
            )
        },

        "employee_count": {
            "description": (
                "The approximate number or declared employee-size "
                "range of the company."
            ),
            "what_to_extract": (
                "Extract an explicitly stated total employee count "
                "or company-size range belonging to the target company."
            ),
            "what_not_to_extract": (
                "Do not extract LinkedIn profile counts, numbers in "
                "'View all employees' links, followers, job openings, "
                "website visitors, or employee counts belonging to "
                "another company. A number of associated LinkedIn "
                "profiles is not necessarily the company's total "
                "employee count."
            ),
            "answer_format": (
                "Preserve the original number or range and its meaning. "
                "Do not convert a company-size range into an exact count."
            ),
            "source_guidance": (
                "Prefer official company information and the company-size "
                "information on its verified LinkedIn company profile. "
                "Secondary sources may be used when clearly attributed."
            )
        },

        "funding": {
            "description": (
                "The external capital or financial investment raised "
                "by the company."
            ),
            "what_to_extract": (
                "Extract explicitly stated funding amounts and currency. "
                "Include funding round details only when available."
            ),
            "what_not_to_extract": (
                "Do not confuse revenue, company valuation, profit, "
                "projected income, or investment announcements involving "
                "another company with funding raised by the target company."
            ),
            "answer_format": (
                "Return the stated monetary amount and currency. "
                "Do not invent missing amounts or funding rounds."
            ),
            "source_guidance": (
                "Prefer official funding announcements, investor "
                "announcements, company disclosures, and reliable "
                "financial publications."
            )
        },

        "revenue": {
            "description": (
                "The income generated by the company through its "
                "business activities."
            ),
            "what_to_extract": (
                "Extract explicitly stated company revenue, including "
                "amount, currency, scale, and reporting period when "
                "available."
            ),
            "what_not_to_extract": (
                "Do not confuse revenue with funding, valuation, profit, "
                "investment, market size, or projected revenue."
            ),
            "answer_format": (
                "Preserve the original amount, scale, currency, and "
                "reporting period when provided. Do not invent a period."
            ),
            "source_guidance": (
                "Prefer official financial statements, company disclosures, "
                "regulatory filings, and reliable financial publications."
            )
        },

        "gtm_partners": {
            "description": (
                "Organizations that help the company sell, distribute, "
                "market, implement, or commercially deliver its products."
            ),
            "what_to_extract": (
                "Identify explicitly stated sales partners, resellers, "
                "distributors, channel partners, implementation partners, "
                "and commercial alliances."
            ),
            "what_not_to_extract": (
                "Do not treat customers, investors, suppliers, technology "
                "integrations, research collaborators, or hardware "
                "optimization partners as GTM partners unless a commercial "
                "go-to-market relationship is established."
            ),
            "answer_format": (
                "Return partner names and briefly describe their "
                "commercial role when supported by evidence."
            ),
            "source_guidance": (
                "Prefer official partnership announcements, partner "
                "directories, company announcements, and documented "
                "commercial agreements."
            )
        },

        "key_customers": {
            "description": (
                "Organizations that actually purchase, use, or have "
                "adopted the company's products or services."
            ),
            "what_to_extract": (
                "Extract named organizations explicitly identified "
                "as customers, clients, product adopters, or users."
            ),
            "what_not_to_extract": (
                "Do not extract investors, technology partners, suppliers, "
                "competitors, event participants, or organizations merely "
                "mentioned in articles."
            ),
            "answer_format": (
                "Return confirmed customer organization names. Include "
                "their relationship with the company only when supported."
            ),
            "source_guidance": (
                "Prefer official customer case studies, testimonials, "
                "customer announcements, and documented deployments."
            )
        },

        "competitors": {
            "description": (
                "Companies offering competing products or services "
                "in the same or overlapping market."
            ),
            "what_to_extract": (
                "Extract companies explicitly identified as competitors "
                "or supported by clear evidence of direct product or "
                "market competition."
            ),
            "what_not_to_extract": (
                "Do not treat companies as competitors merely because "
                "they operate in AI, technology, healthcare, or the same "
                "broad industry. Do not return URLs, search suggestions, "
                "customers, or partners as competitors."
            ),
            "answer_format": (
                "Return company names only, optionally followed by "
                "a short explanation of their competitive relationship."
            ),
            "source_guidance": (
                "Prefer credible industry analysis, competitor comparisons, "
                "market research, and reliable business publications."
            )
        }
    },
    
    # ============================================================
    # PRODUCT INFORMATION
    # ============================================================

    "product": {

        "product_name": {
            "description": "The official name of the company's product.",
            "what_to_extract": (
                "Identify the specific product or platform belonging "
                "to the given company."
            ),
            "what_not_to_extract": (
                "Do not return the company name, partner name, technology "
                "name, or unrelated product."
            ),
            "answer_format": "Return only the official product name.",
            "source_guidance": (
                "Prefer the official product website, product "
                "documentation, and company materials."
            )
        },

        "description": {
            "description": (
                "A description of what the product does, how it works "
                "at a high level, and the problem it solves."
            ),
            "what_to_extract": (
                "Identify the product's purpose, main capabilities, "
                "functionality, and value to its intended users."
            ),
            "what_not_to_extract": (
                "Do not provide only the company overview, technical "
                "framework lists, hardware specifications, or unsupported "
                "marketing claims."
            ),
            "answer_format": (
                "Write a concise paragraph of approximately 2-4 sentences."
            ),
            "source_guidance": (
                "Prefer official product pages, product documentation, "
                "technical documentation, and company presentations."
            )
        },

        "vertical_market": {
            "description": (
                "The industries, sectors, or market segments the "
                "product is designed to serve."
            ),
            "what_to_extract": (
                "Identify the industries or business domains where "
                "the product is intended to be used."
            ),
            "what_not_to_extract": (
                "Do not confuse technical capabilities, programming "
                "technologies, customer names, or general use cases "
                "with the target industry."
            ),
            "answer_format": (
                "Return a concise list of relevant industries "
                "or market segments."
            ),
            "source_guidance": (
                "Prefer official product descriptions, use cases, "
                "customer deployments, and industry-specific documentation."
            )
        },

        "route_to_market": {
            "description": (
                "The commercial strategy through which the company "
                "sells, distributes, or delivers the product to customers."
            ),
            "what_to_extract": (
                "Identify direct sales, enterprise sales, subscription "
                "SaaS, resellers, distributors, channel partners, "
                "marketplaces, OEM arrangements, or other explicitly "
                "stated commercial channels."
            ),
            "what_not_to_extract": (
                "Do not confuse route-to-market with cloud, edge, or "
                "on-premises deployment. Do not automatically treat "
                "technology integrations, research partnerships, hardware "
                "optimization, or technical collaborations as commercial "
                "distribution channels."
            ),
            "answer_format": (
                "Provide a concise description of the commercial sales "
                "or distribution approach."
            ),
            "source_guidance": (
                "Prefer official sales information, pricing pages, "
                "partner programs, reseller agreements, marketplace "
                "listings, and commercial announcements."
            )
        },

        "inference_hardware": {
            "description": (
                "The hardware used to run trained AI models and "
                "perform inference."
            ),
            "what_to_extract": (
                "Identify processors, GPUs, accelerators, servers, "
                "or cloud hardware instances explicitly used for "
                "model inference."
            ),
            "what_not_to_extract": (
                "Do not confuse inference hardware with hardware used "
                "only for model training or general company infrastructure."
            ),
            "answer_format": (
                "Return hardware names, processor or accelerator types, "
                "and cloud instance types when available."
            ),
            "source_guidance": (
                "Prefer official technical documentation, deployment "
                "architecture, engineering blogs, and product announcements."
            )
        },

        "deployment_type": {
            "description": (
                "The environment or infrastructure in which the product "
                "or AI solution is deployed."
            ),
            "what_to_extract": (
                "Identify whether the product supports cloud, on-premises, "
                "edge, hybrid, or other explicitly stated deployment "
                "environments."
            ),
            "what_not_to_extract": (
                "Do not confuse deployment type with sales strategy, "
                "hardware type, model training environment, or "
                "software framework."
            ),
            "answer_format": (
                "Return supported deployment types and relevant details."
            ),
            "source_guidance": (
                "Prefer official deployment documentation, architecture "
                "documentation, and product technical specifications."
            )
        },

        "training_hardware": {
            "description": (
                "The hardware used to train or fine-tune the product's "
                "AI or machine learning models."
            ),
            "what_to_extract": (
                "Identify GPUs, CPUs, AI accelerators, servers, and "
                "cloud instances explicitly associated with model "
                "training or fine-tuning."
            ),
            "what_not_to_extract": (
                "Do not confuse inference hardware with training hardware. "
                "Do not assume that hardware used for deployment is "
                "also used for training."
            ),
            "answer_format": (
                "Return hardware and cloud instance names with their "
                "training purpose when available."
            ),
            "source_guidance": (
                "Prefer technical papers, engineering blogs, training "
                "architecture documentation, and official announcements."
            )
        },

        "models": {
            "description": (
                "The AI, machine learning, or deep learning models "
                "used or developed by the product."
            ),
            "what_to_extract": (
                "Identify model architectures, pretrained models, "
                "foundation models, custom models, and model families "
                "explicitly associated with the product."
            ),
            "what_not_to_extract": (
                "Do not confuse model names with programming frameworks, "
                "serving runtimes, hardware, or general AI concepts."
            ),
            "answer_format": (
                "Return model names and relevant architecture details."
            ),
            "source_guidance": (
                "Prefer technical documentation, research papers, "
                "model cards, engineering publications, and official "
                "product materials."
            )
        },

        "ai_framework": {
            "description": (
                "Frameworks and libraries used to develop, train, "
                "or fine-tune AI and machine learning models."
            ),
            "what_to_extract": (
                "Identify model development and training frameworks "
                "such as PyTorch, TensorFlow, Keras, Hugging Face "
                "Transformers, and PEFT when explicitly used."
            ),
            "what_not_to_extract": (
                "Do not confuse model development frameworks with "
                "inference engines, serving runtimes, databases, "
                "cloud platforms, or hardware."
            ),
            "answer_format": "Return framework and library names.",
            "source_guidance": (
                "Prefer technical documentation, source code repositories, "
                "engineering blogs, and official technical publications."
            )
        },

        "serving_framework": {
            "description": (
                "Frameworks, runtimes, or engines used to serve, deploy, "
                "or optimize trained AI models for inference."
            ),
            "what_to_extract": (
                "Identify inference serving and optimization technologies "
                "such as vLLM, TensorRT, Triton, ONNX Runtime, OpenVINO, "
                "and TorchServe when explicitly associated with serving."
            ),
            "what_not_to_extract": (
                "Do not confuse model training frameworks, programming "
                "languages, hardware, or general deployment platforms "
                "with serving frameworks."
            ),
            "answer_format": (
                "Return serving and inference optimization framework names."
            ),
            "source_guidance": (
                "Prefer official deployment documentation, engineering "
                "blogs, architecture diagrams, and technical repositories."
            )
        },

        "additional_ai_software_stack": {
            "description": (
                "Other software infrastructure and supporting technologies "
                "used in the product's AI ecosystem."
            ),
            "what_to_extract": (
                "Identify supporting technologies such as databases, "
                "vector databases, graph databases, message queues, "
                "data pipelines, MLOps platforms, monitoring systems, "
                "and orchestration tools."
            ),
            "what_not_to_extract": (
                "Do not repeat model names, training frameworks, serving "
                "frameworks, hardware, or unrelated general-purpose software."
            ),
            "answer_format": (
                "Return technology names, grouped or described by their "
                "role when available."
            ),
            "source_guidance": (
                "Prefer official technical documentation, architecture "
                "diagrams, engineering blogs, and technical repositories."
            )
        }
    }
    
# ============================================================
# HELPER FUNCTIONS
# ============================================================

def get_field_definitions():
    """Return all company and product field definitions."""
    return FIELD_DEFINITIONS


def get_section_definitions(section_name):
    """Return definitions for a specific section."""
    return FIELD_DEFINITIONS.get(section_name, {})


def get_all_field_names():
    """Return all available field names."""
    field_names = []

    for section in FIELD_DEFINITIONS.values():
        field_names.extend(section.keys())

    return field_names


def get_field_definition(field_name):
    """Return the definition of a particular field."""

    for section in FIELD_DEFINITIONS.values():
        if field_name in section:
            return section[field_name]

    return None


def get_field_section(field_name):
    """Return the section to which a field belongs."""

    for section_name, section in FIELD_DEFINITIONS.items():
        if field_name in section:
            return section_name

    return None
    
