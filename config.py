import os

# ----------------------------
# Configuration
# ----------------------------
MEMORY_FOLDER = "./LangGraph_Memory"
os.makedirs(MEMORY_FOLDER, exist_ok=True)

MEMORY_FILE = f"{MEMORY_FOLDER}/langgraph_memory.json"
MOCK_PRODUCTS_EXTRACTION = "products.json"
