import asyncio
from memory import memory
from utils import search_store

def search_amazon_flipkart_parallel(state):
    async def search_both():
        async def search_amazon_fn():
            if not memory.get("amazon"):
                result = search_store("Amazon", state.request)
                memory["amazon"] = result
            else:
                result = memory["amazon"]
            print("[SearchAmazon] Result:", result)
            return result

        async def search_flipkart_fn():
            if not memory.get("flipkart"):
                result = search_store("Flipkart", state.request)
                memory["flipkart"] = result
            else:
                result = memory["flipkart"]
            print("[SearchFlipkart] Result:", result)
            return result

        return await asyncio.gather(search_amazon_fn(), search_flipkart_fn())

    amazon_result, flipkart_result = asyncio.run(search_both())
    return {"amazon": amazon_result, "flipkart": flipkart_result}


def search_ebay(state):
    if not memory.get("ebay"):
        if len(memory.get("amazon", [])) + len(memory.get("flipkart", [])) < 4:
            result = search_store("eBay", state.request)
            memory["ebay"] = result
        else:
            result = []
            memory["ebay"] = []
    else:
        result = memory["ebay"]

    print("[SearchEbay] Result:", result)
    return {"ebay": result}
