import re

def parse_intent_entities(query: str):
    query_lower = query.lower()
    intent = "search"
    entities = {}

    if "cheaper" in query_lower or "below" in query_lower or "under" in query_lower:
        intent = "filter_price"
        match = re.search(r"\$(\d+)", query)
        entities["max_price"] = int(match.group(1)) if match else 55

    if "amazon" in query_lower:
        intent = "filter_store"
        entities["store_name"] = "Amazon"
    elif "flipkart" in query_lower:
        intent = "filter_store"
        entities["store_name"] = "Flipkart"
    elif "ebay" in query_lower:
        intent = "filter_store"
        entities["store_name"] = "eBay"

    return intent, entities
