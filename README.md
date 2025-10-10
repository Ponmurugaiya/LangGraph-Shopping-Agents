# LangGraph multi-agent shopping search

This project demonstrates a **multi-agent shopping search system** using **LangGraph Framework**.  
The agents can search multiple stores (Amazon, Flipkart, eBay), aggregate results, and apply filters like maximum price. It also supports **multi-turn interactions** with persistent memory.

---

## Features

- **Multi-store search**: Parallel searches across Amazon and Flipkart, with eBay as a fallback.
- **Aggregator**: Combines results from different stores and applies filters such as price limits or specific stores.
- **Persistent memory**: Stores previous queries and search results for multi-turn conversations.
- **Rule-based NLU**: Parses user intent and entities from queries (price, store selection).
- **Visualization**: Optional graph visualization using Mermaid.

---

## Project Structure

```

.
├── main.py                   # Driver script for multi-turn simulation
├── config.py                 # Configuration and paths
├── memory.py                 # Persistent memory management
├── state.py                  # GraphState model for LangGraph
├── nlu.py                    # Rule-based intent and entity extraction
├── utils.py                  # Helper functions for search and aggregation
├── products_extraction.py    # Mock product database loader
├── visualize.py              # Graph visualization helper
├── graph_builder.py          # Builds the LangGraph workflow
├── products.json             # Mock product data
└── nodes/
├── user_request.py       # Node for user query parsing
├── search.py             # Nodes for Amazon, Flipkart, eBay search
└── aggregator.py         # Node to combine and filter search results

````

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Ponmurugaiya/LangGraph-Shopping-Agents.git
cd LangGraph-Shopping-Agents
````

2. Install dependencies:

```bash
pip install -r requirements.txt
```

**Dependencies**:

* Python 3.10+
* `langgraph`
* `pydantic`
* `asyncio` (built-in)
* `mermaid` (optional, for visualization)

---

## Setup

1. Ensure `products.json` is present in the project root. Example:

```json
{
  "Amazon": [
    {"name": "Running shoes A1", "price": 50},
    {"name": "Running shoes A2", "price": 60}
  ],
  "Flipkart": [
    {"name": "Running shoes F1", "price": 55},
    {"name": "Running shoes F2", "price": 65}
  ],
  "eBay": [
    {"name": "Running shoes E1", "price": 52},
    {"name": "Running shoes E2", "price": 62}
  ]
}
```

2. The project will automatically create a memory folder:

```
./LangGraph_Memory/langgraph_memory.json
```

This file stores persistent memory across multi-turn queries.

---

## Usage

Run the simulation:

```bash
python main.py
```

Simulated user queries:

```python
simulated_user_queries = [
    "Running shoes",
    "Show cheaper than $55",
    "Only Amazon results"
]
```

* Each turn updates memory and fetches results.
* Final recommendations are printed after every turn.
* Memory ensures that repeated queries reuse cached results.

---

## Extending the Project

* **Add more stores**: Create new search nodes in `nodes/search.py` and connect them in `graph_builder.py`.
* **Improve NLU**: Extend `nlu.py` to handle multiple constraints per query.
* **Enhance aggregator**: Apply multiple filters simultaneously (e.g., store + price).
* **Visualization**: Call `visualize(app)` to generate a graph image (`langgraph_visualization.png`).

---

## Example Output

```
=== TURN 1: User Query: 'Running shoes' ===
[UserRequest] Query: 'Running shoes' | Intent: search | Entities: {}
[SearchAmazon] Result: ['Running shoes A1 - $50', 'Running shoes A2 - $60']
[SearchFlipkart] Result: ['Running shoes F1 - $55', 'Running shoes F2 - $65']
[SearchEbay] Result: ['Running shoes E1 - $52', 'Running shoes E2 - $62']
[Aggregator] Final Recommendations: ['Running shoes A1 - $50', 'Running shoes F1 - $55', 'Running shoes E1 - $52', 'Running shoes A2 - $60', 'Running shoes F2 - $65']
Final Recommendations after turn 1: ['Running shoes A1 - $50', 'Running shoes F1 - $55', 'Running shoes E1 - $52', 'Running shoes A2 - $60', 'Running shoes F2 - $65']
```

