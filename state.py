from pydantic import BaseModel
from typing import List, Optional

class GraphState(BaseModel):
    request: Optional[str] = None
    amazon: Optional[List[str]] = None
    flipkart: Optional[List[str]] = None
    ebay: Optional[List[str]] = None
    final: Optional[List[str]] = None
