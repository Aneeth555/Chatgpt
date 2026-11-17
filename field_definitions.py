 
# schemas/field_definitions.py

"""
Central definitions for all One-Pager fields.

Used by:
1. Questionnaire extraction
2. Web extraction

Each field explains:
- What the field means
- What information to extract
- What information NOT to extract
- Expected answer format
- Preferred source guidance

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
                "Extract the company's official business name "
                "as identified in the source."
            ),

            "what_not_to_extract": (
                "Do not extract product names, brand names, "
                "subsidiary names, or partner company names "
                "as the company name."
            ),

            "answer_format": (
                "Return only the company name."
            ),

            "source_guidance": (
                "Prefer the official company website, official "
                "company documents, or verified company profiles."
            )
        },

        "overview": {
            "description": (
                "A concise summary of the company, its primary "
                "business, technology, and value proposition."
            ),

            "what_to_extract": (
                "Identify what the company does, its main business "
                "activities, the problems it solves, and its "
                "main value proposition."
            ),

            "what_not_to_extract": (
                "Do not provide only a list of products, customers, "
                "funding details, technical specifications, or "
                "generic marketing statements without explaining "
                "the company's business."
            ),

            "answer_format": (
                "Write a concise paragraph of approximately "
                "2-4 sentences."
            ),

            "source_guidance": (
                "Prefer the official About Us page, company profile, "
                "official presentations, and company documentation."
            )
        },

        "headquarters": {
            "description": (
                "The company's primary headquarters or main "
                "corporate office location."
            ),

            "what_to_extract": (
                "Extract the address or location explicitly "
                "identified as the company's headquarters, "
                "head office, or main corporate office."
            ),

            "what_not_to_extract": (
                "Do not automatically treat a registered office, "
                "branch office, operational office, employee "
                "location, mailing address, or third-party office "
                "listing as the headquarters."
            ),

            "answer_format": (
                "Return the complete available headquarters "
                "location, including city, state, and country "
                "where available."
            ),

            "source_guidance": (
                "Prefer the official company website and official "
                "company documents. Use reliable business directories "
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
                "or company-size range."
            ),

            "what_not_to_extract": (
                "Do not extract LinkedIn profile counts, numbers "
                "in 'View all employees' links, followers, job "
                "openings, website visitors, or employee counts "
                "belonging to another company."
            ),

            "answer_format": (
                "Preserve the original number or range and its "
                "meaning. Do not convert a company-size range "
                "into an exact employee count."
            ),

            "source_guidance": (
                "Prefer official company information and the "
                "company-size information on its verified "
                "LinkedIn company profile. Secondary sources "
                "may be used when clearly attributed."
            )
        },

        "funding": {
            "description": (
                "The external capital or financial investment "
                "raised by the company."
            ),

            "what_to_extract": (
                "Extract explicitly stated funding amounts, "
                "currency, and relevant funding details when "
                "available."
            ),

            "what_not_to_extract": (
                "Do not confuse revenue, company valuation, "
                "profit, grants, projected income, or investment "
                "announcements involving another company with "
                "funding raised by this company."
            ),

            "answer_format": (
                "Return the stated monetary amount and currency. "
                "Include funding round details only when explicitly "
                "available. Do not invent missing amounts."
            ),

            "source_guidance": (
                "Prefer official funding announcements, investor "
                "announcements, company disclosures, and reliable "
                "business or financial publications."
            )
        },

        "revenue": {
            "description": (
                "The income generated by the company through "
                "its business activities."
            ),

            "what_to_extract": (
                "Extract explicitly stated company revenue, "
                "including its amount, currency, and reporting "
                "period when available."
            ),

            "what_not_to_extract": (
                "Do not confuse revenue with funding, valuation, "
                "profit, total investment, market size, or "
                "projected revenue."
            ),

            "answer_format": (
                "Preserve the original amount, scale, currency, "
                "and reporting period when provided. Do not "
                "invent a reporting period."
            ),

            "source_guidance": (
                "Prefer official financial statements, company "
                "disclosures, regulatory filings, and reliable "
                "financial publications."
            )
        },

        "gtm_partners": {
            "description": (
                "Companies or organizations that help the company "
                "sell, distribute, market, implement, or commercially "
                "deliver its products."
            ),

            "what_to_extract": (
                "Identify explicitly stated sales partners, "
                "resellers, distributors, channel partners, "
                "implementation partners, and commercial alliances."
            ),

            "what_not_to_extract": (
                "Do not treat customers, investors, suppliers, "
                "technology integrations, research collaborators, "
                "or hardware optimization partners as GTM partners "
                "unless a commercial go-to-market relationship "
                "is established."
            ),

            "answer_format": (
                "Return the names of the identified partners "
                "and briefly describe their commercial role "
                "when available."
            ),

            "source_guidance": (
                "Prefer official partnership announcements, "
                "partner directories, company announcements, "
                "and documented commercial agreements."
            )
        },

        "key_customers": {
            "description": (
                "Organizations that actually purchase, use, or "
                "have adopted the company's products or services."
            ),

            "what_to_extract": (
                "Extract named organizations explicitly identified "
                "as customers, clients, product adopters, or users."
            ),

            "what_not_to_extract": (
                "Do not extract investors, technology partners, "
                "suppliers, competitors, event participants, "
                "or organizations merely mentioned in articles."
            ),

            "answer_format": (
                "Return the names of confirmed customer organizations. "
                "Include their relationship with the company only "
                "when supported by the source."
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
                "Extract companies explicitly identified as "
                "competitors or supported by clear evidence of "
                "direct product or market competition."
            ),

            "what_not_to_extract": (
                "Do not treat companies as competitors merely "
                "because they operate in AI, technology, healthcare, "
                "or the same broad industry. Do not extract URLs, "
                "search suggestions, customers, or partners as "
                "competitors."
            ),

            "answer_format": (
                "Return company names only, optionally followed "
                "by a short explanation of their competitive "
                "relationship."
            ),

            "source_guidance": (
                "Prefer credible industry analysis, competitor "
                "comparisons, market research, and reliable "
                "business publications. Require evidence of "
                "a genuine competitive relationship."
            )
        }
    },

    # ============================================================
    # PRODUCT INFORMATION
    # ============================================================

    "product": {

        "product_name": {
            "description": (
                "The official name of the company's product "
                "or platform."
            ),

            "what_to_extract": (
                "Identify the specific product or platform "
                "belonging to the given company."
            ),

            "what_not_to_extract": (
                "Do not return the company name, partner name, "
                "technology name, or unrelated product."
            ),

            "answer_format": (
                "Return only the official product name."
            ),

            "source_guidance": (
                "Prefer the official product website, product "
                "documentation, and company materials."
            )
        },

        "description": {
            "description": (
                "A description of what the product does, how "
                "it works at a high level, and the problem it solves."
            ),

            "what_to_extract": (
                "Identify the product's purpose, main capabilities, "
                "functionality, and value to its intended users."
            ),

            "what_not_to_extract": (
                "Do not provide only the company overview, a list "
                "of technical frameworks, hardware specifications, "
                "or unsupported marketing claims."
            ),

            "answer_format": (
                "Write a concise paragraph of approximately "
                "2-4 sentences."
            ),

            "source_guidance": (
                "Prefer official product pages, product documentation, "
                "technical documentation, and company presentations."
            )
        },

        "vertical_market": {
            "description": (
                "The industries, sectors, or market segments "
                "the product is designed to serve."
            ),

            "what_to_extract": (
                "Identify the industries or business domains "
                "where the product is intended to be used."
            ),

            "what_not_to_extract": (
                "Do not confuse a product's technical capabilities, "
                "programming technologies, customer names, or "
                "general use cases with its target industry."
            ),

            "answer_format": (
                "Return a concise list of relevant industries "
                "or market segments."
            ),

            "source_guidance": (
                "Prefer official product descriptions, use cases, "
                "customer deployments, and industry-specific "
                "product documentation."
            )
        },

        "route_to_market": {
            "description": (
                "The commercial strategy through which the company "
                "sells, distributes, or delivers the product "
                "to customers."
            ),

            "what_to_extract": (
                "Identify direct sales, enterprise sales, "
                "subscription-based SaaS, resellers, distributors, "
                "channel partners, marketplaces, OEM arrangements, "
                "or other explicitly stated commercial channels."
            ),

            "what_not_to_extract": (
                "Do not confuse route-to-market with cloud, edge, "
                "or on-premises deployment. Do not automatically "
                "treat technology integrations, research partnerships, "
                "hardware optimization, or technical collaborations "
                "as commercial distribution channels."
            ),

            "answer_format": (
                "Provide a concise description of the commercial "
                "sales or distribution approach."
            ),

            "source_guidance": (
                "Prefer official sales information, pricing pages, "
                "partner programs, reseller agreements, marketplace "
                "listings, and commercial announcements."
            )
        },

        "inference_hardware": {
            "description": (
                "The hardware used to run trained AI models "
                "and perform inference."
            ),

            "what_to_extract": (
                "Identify processors, GPUs, accelerators, servers, "
                "or cloud hardware instances explicitly used "
                "for model inference."
            ),

            "what_not_to_extract": (
                "Do not confuse inference hardware with hardware "
                "used only for model training, general company "
                "infrastructure, or hardware mentioned without "
                "an inference-related connection."
            ),

            "answer_format": (
                "Return hardware names, processor or accelerator "
                "types, and cloud instance types when available."
            ),

            "source_guidance": (
                "Prefer official technical documentation, deployment "
                "architecture, engineering blogs, and product "
                "announcements."
            )
        },

        "deployment_type": {
            "description": (
                "The environment or infrastructure in which "
                "the product or AI solution is deployed."
            ),

            "what_to_extract": (
                "Identify whether the product supports cloud, "
                "on-premises, edge, hybrid, or other explicitly "
                "stated deployment environments."
            ),

            "what_not_to_extract": (
                "Do not confuse deployment type with sales strategy, "
                "hardware type, model training environment, or "
                "software framework."
            ),

            "answer_format": (
                "Return the supported deployment types and "
                "relevant details when available."
            ),

            "source_guidance": (
                "Prefer official deployment documentation, "
                "architecture documentation, and product "
                "technical specifications."
            )
        },

        "training_hardware": {
            "description": (
                "The hardware used to train or fine-tune "
                "the product's AI or machine learning models."
            ),

            "what_to_extract": (
                "Identify GPUs, CPUs, AI accelerators, servers, "
                "and cloud instances explicitly associated "
                "with model training or fine-tuning."
            ),

            "what_not_to_extract": (
                "Do not confuse inference hardware with training "
                "hardware. Do not assume that hardware used for "
                "deployment is also used for training."
            ),

            "answer_format": (
                "Return the hardware and cloud instance names "
                "with their training purpose when available."
            ),

            "source_guidance": (
                "Prefer technical papers, engineering blogs, "
                "training architecture documentation, and "
                "official technical announcements."
            )
        },

        "models": {
            "description": (
                "The AI, machine learning, or deep learning "
                "models used or developed by the product."
            ),

            "what_to_extract": (
                "Identify model architectures, pretrained models, "
                "foundation models, custom models, and model "
                "families explicitly associated with the product."
            ),

            "what_not_to_extract": (
                "Do not confuse model names with programming "
                "frameworks, serving runtimes, hardware, or "
                "general AI concepts."
            ),

            "answer_format": (
                "Return model names and relevant architecture "
                "details when available."
            ),

            "source_guidance": (
                "Prefer technical documentation, research papers, "
                "model cards, engineering publications, and "
                "official product materials."
            )
        },

        "ai_framework": {
            "description": (
                "The frameworks and libraries used to develop, "
                "train, or fine-tune AI and machine learning models."
            ),

            "what_to_extract": (
                "Identify model development and training frameworks "
                "such as PyTorch, TensorFlow, Keras, Hugging Face "
                "Transformers, and PEFT when explicitly used."
            ),

            "what_not_to_extract": (
                "Do not confuse model development frameworks "
                "with inference engines, serving runtimes, "
                "databases, cloud platforms, or hardware."
            ),

            "answer_format": (
                "Return the names of the frameworks and libraries."
            ),

            "source_guidance": (
                "Prefer technical
