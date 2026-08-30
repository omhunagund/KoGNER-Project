import networkx as nx


def build_graph(entities):
    """
    Build a biomedical knowledge graph from extracted entities.
    """

    graph = nx.Graph()

    # ------------------------
    # Add Nodes
    # ------------------------

    for entity in entities:

        graph.add_node(
            entity["Entity"],
            entity_type=entity["Type"],
            confidence=entity["Confidence"]
        )

    # ------------------------
    # Add Relationships
    # ------------------------

    for i in range(len(entities) - 1):

        source = entities[i]["Entity"]
        target = entities[i + 1]["Entity"]

        graph.add_edge(
            source,
            target,
            relation="related_to"
        )

    return graph