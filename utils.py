from typing import List
from products_extraction import MOCK_PRODUCTS_EXTRACTION

def search_store(store: str, query: str):
    return [
        f"{p['name']} - ${p['price']}"
        for p in MOCK_PRODUCTS_EXTRACTION.get(store, [])
        if query.lower() in p["name"].lower()
    ]

def aggregate_results(results_list: List[List[str]], memory_filter: dict = None):
    combined = []
    for res in results_list:
        combined.extend(res)

    if memory_filter and "max_price" in memory_filter:
        combined = [
            item for item in combined if int(item.split("$")[1]) <= memory_filter["max_price"]
        ]

    return combined[:5]
