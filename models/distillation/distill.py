import networkx as nx


def distill_graph(graph, keep_ratio=0.5):
    """
    Distill a biomedical knowledge graph using multiple
    graph centrality measures.

    Parameters
    ----------
    graph : networkx.Graph
    keep_ratio : float

    Returns
    -------
    distilled_graph
    ranked_nodes
    """

    if graph.number_of_nodes() == 0:
        return graph.copy(), []

    degree = nx.degree_centrality(graph)
    betweenness = nx.betweenness_centrality(graph)
    closeness = nx.closeness_centrality(graph)

    scores = {}

    for node in graph.nodes():

        score = (
            0.4 * degree[node] +
            0.3 * betweenness[node] +
            0.3 * closeness[node]
        )

        scores[node] = score

    ranked_nodes = sorted(
        scores.items(),
        key=lambda x: x[1],
        reverse=True
    )

    keep_count = max(
        1,
        int(len(ranked_nodes) * keep_ratio)
    )

    selected_nodes = [
        node
        for node, score in ranked_nodes[:keep_count]
    ]

    distilled_graph = graph.subgraph(selected_nodes).copy()

    return distilled_graph, ranked_nodes