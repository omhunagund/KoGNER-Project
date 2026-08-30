from knowledge_graph.graph_builder import build_graph

entities = [

    {
        "Entity": "Metformin",
        "Type": "DRUG",
        "Confidence": 99.8
    },

    {
        "Entity": "Diabetes",
        "Type": "DISEASE",
        "Confidence": 98.5
    },

    {
        "Entity": "BRCA1",
        "Type": "GENE",
        "Confidence": 97.2
    }

]

graph = build_graph(entities)

print("\nNodes\n")

for node in graph.nodes(data=True):
    print(node)

print("\nEdges\n")

for edge in graph.edges(data=True):
    print(edge)