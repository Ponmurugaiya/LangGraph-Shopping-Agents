from memory import memory, save_memory
from utils import aggregate_results

def aggregator(state):
    intent = memory.get("current_intent", "search")
    entities = memory.get("current_entities", {})
    all_results = [memory.get("amazon", []), memory.get("flipkart", []), memory.get("ebay", [])]

    if intent == "filter_store" and "store_name" in entities:
        store = entities["store_name"]
        all_results = [memory.get(store.lower(), []) if store.lower() in memory else []]

    memory_filter = {}
    if intent == "filter_price" and "max_price" in entities:
        memory_filter["max_price"] = entities["max_price"]

    final = aggregate_results(all_results, memory_filter)
    print("[Aggregator] Final Recommendations:", final)
    memory["final"] = final
    save_memory()
    return {"final": final}
