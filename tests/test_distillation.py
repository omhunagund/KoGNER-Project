from knowledge_graph.graph_builder import build_graph
from models.distillation.distill import distill_graph


entities = [
    {"Entity": "Diabetes", "Type": "DISEASE", "Confidence": 98.5},
    {"Entity": "Metformin", "Type": "DRUG", "Confidence": 97.8},
    {"Entity": "Insulin", "Type": "DRUG", "Confidence": 96.2},
    {"Entity": "Kidney", "Type": "BIOLOGICAL_STRUCTURE", "Confidence": 95.4},
    {"Entity": "Heart", "Type": "BIOLOGICAL_STRUCTURE", "Confidence": 94.7}
]

graph = build_graph(entities)

distilled_graph, ranked = distill_graph(
    graph,
    keep_ratio=0.6
)

print("Original Nodes :", graph.number_of_nodes())
print("Distilled Nodes:", distilled_graph.number_of_nodes())

print()

print("Ranked Nodes")

for node, score in ranked:
    print(node, round(score, 3))