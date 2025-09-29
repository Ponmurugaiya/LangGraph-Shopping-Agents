import json
from config import MOCK_PRODUCTS_EXTRACTION

with open(MOCK_PRODUCTS_EXTRACTION, "r") as f:
    MOCK_PRODUCTS_EXTRACTION = json.load(f)

