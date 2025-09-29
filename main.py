from memory import memory
from graph_builder import build_graph
from visualize import visualize

# Build graph
app = build_graph()
visualize(app)

# Simulate multi-turn interaction
simulated_user_queries = [
    "Running shoes",
    "Show cheaper than $55",
    "Only Amazon results"
]

for turn, query in enumerate(simulated_user_queries, 1):
    print(f"\n=== TURN {turn}: User Query: '{query}' ===")
    memory["current_turn_query"] = query
    final_state = app.invoke({})
    print(f"Final Recommendations after turn {turn}: {memory.get('final')}")
