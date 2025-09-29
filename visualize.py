def visualize(app):
    try:
        g = app.get_graph()
        png = g.draw_mermaid_png()
        with open("langgraph_visualization.png", "wb") as f:
            f.write(png)
        print("✅ Graph visualization saved as langgraph_visualization.png")
    except Exception as e:
        print("⚠ Visualization not available:", e)
