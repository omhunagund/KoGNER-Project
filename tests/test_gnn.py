from knowledge_graph.graph_builder import build_graph
from models.gnn.analyzer import analyze_graph


entities = [

    {
        "Entity": "Metformin",
        "Type": "DRUG",
        "Confidence": 99.8
    },

    {
        "Entity": "Diabetes",
        "Type": "DISEASE",
        "Confidence": 98.4
    },

    {
        "Entity": "BRCA1",
        "Type": "GENE",
        "Confidence": 97.2
    }

]

graph = build_graph(entities)

results = analyze_graph(graph)

print("\nGraph Statistics\n")

for key, value in results.items():

    print(f"{key} : {value}")