from langgraph.graph import StateGraph, START, END
from state import GraphState
from nodes.user_request import get_request
from nodes.search import search_amazon_flipkart_parallel, search_ebay
from nodes.aggregator import aggregator

def build_graph():
    graph = StateGraph(GraphState)
    graph.add_node("UserRequest", get_request)
    graph.add_node("SearchAmazonFlipkartParallel", search_amazon_flipkart_parallel)
    graph.add_node("SearchEbay", search_ebay)
    graph.add_node("Aggregate", aggregator)

    graph.add_edge(START, "UserRequest")
    graph.add_edge("UserRequest", "SearchAmazonFlipkartParallel")
    graph.add_edge("SearchAmazonFlipkartParallel", "SearchEbay")
    graph.add_edge("SearchEbay", "Aggregate")
    graph.add_edge("Aggregate", END)

    return graph.compile()
