 
import re


# ============================================================
# Chunking configuration
# ============================================================

CHUNK_SIZE = 2500
CHUNK_OVERLAP = 250


# ============================================================
# Text cleaning
# ============================================================

def clean_text(text):
    """
    Remove excessive whitespace from webpage content.
    """

    if not text:
        return ""

    text = str(text)
    text = text.replace("\r", "\n")

    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)

    return text.strip()


# ============================================================
# Split text into chunks
# ============================================================

def split_into_chunks(
    text,
    chunk_size=CHUNK_SIZE,
    overlap=CHUNK_OVERLAP
):
    """
    Split text into chunks while preferring paragraph
    and sentence boundaries.
    """

    if chunk_size <= 0:
        raise ValueError(
            "chunk_size must be greater than zero."
        )

    if overlap < 0 or overlap >= chunk_size:
        raise ValueError(
            "overlap must be non-negative and smaller "
            "than chunk_size."
        )

    text = clean_text(text)

    if not text:
        return []

    if len(text) <= chunk_size:
        return [text]

    chunks = []
    start = 0
    text_length = len(text)

    while start < text_length:

        end = min(start + chunk_size, text_length)

        if end < text_length:

            # Prefer paragraph boundary
            boundary = text.rfind(
                "\n\n",
                start,
                end
            )

            # Otherwise prefer sentence boundary
            if boundary <= start + chunk_size // 2:

                boundary = text.rfind(
                    ". ",
                    start,
                    end
                )

            # Otherwise prefer word boundary
            if boundary <= start + chunk_size // 2:

                boundary = text.rfind(
                    " ",
                    start,
                    end
                )

            if boundary > start:
                end = boundary + 1

        chunk = text[start:end].strip()

        if chunk:
            chunks.append(chunk)

        if end >= text_length:
            break

        next_start = max(
            0,
            end - overlap
        )

        # Ensure progress
        if next_start <= start:
            next_start = start + chunk_size

        start = next_start

    return chunks


# ============================================================
# Preserve source metadata
# ============================================================

def get_page_metadata(page):
    """
    Extract metadata from the original crawled page.

    Identity verification must happen before chunking.
    Unverified pages remain unverified.
    """

    return {
        "title": page.get("title", ""),
        "url": (
            page.get("final_url")
            or page.get("url", "")
        ),
        "domain": page.get("domain", ""),

        "identity_verified": (
            page.get("identity_verified") is True
        ),

        "identity_reason": page.get(
            "identity_reason", ""
        ),

        "source_type": page.get(
            "source_type", "other"
        ),

        "source_priority": page.get(
            "source_priority", 4
        ),

        "related_fields": page.get(
            "related_fields", []
        )
    }


# ============================================================
# Chunk crawled webpages
# ============================================================

def chunk_crawled_pages(crawled_pages):
    """
    Convert crawled webpages into structured chunks.

    Every chunk inherits:
        - Source title
        - Source URL
        - Domain
        - Identity verification status
        - Identity verification reason
        - Source type and priority
        - Related fields

    Unverified pages are retained as unverified.
    The relevance filter will reject them.
    """

    all_chunks = []

    for page in crawled_pages:

        if not page.get("success"):
            continue

        content = clean_text(
            page.get("content", "")
        )

        if not content:
            continue

        # Extract original webpage metadata
        metadata = get_page_metadata(page)

        chunks = split_into_chunks(content)

        for index, chunk_text in enumerate(chunks):

            chunk_id = (
                f"{metadata['domain'] or 'unknown'}_"
                f"{len(all_chunks) + 1}"
            )

            all_chunks.append({

                # Chunk identification
                "chunk_id": chunk_id,

                # Original webpage information
                "title": metadata["title"],
                "url": metadata["url"],
                "domain": metadata["domain"],

                # Identity verification
                "identity_verified": (
                    metadata["identity_verified"]
                ),

                "identity_reason": (
                    metadata["identity_reason"]
                ),

                # Source classification
                "source_type": metadata["source_type"],
                "source_priority": metadata["source_priority"],

                # Field association
                "related_fields": metadata["related_fields"],

                # Chunk information
                "chunk_index": index,
                "total_chunks": len(chunks),

                # Actual webpage text
                "text": chunk_text
            })

    return all_chunks
