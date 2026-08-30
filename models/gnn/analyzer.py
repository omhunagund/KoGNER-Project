import networkx as nx


def analyze_graph(G):
    """
    Analyze a NetworkX graph and return useful statistics.
    """

    if G.number_of_nodes() == 0:
        return None

    # Number of nodes and edges
    num_nodes = G.number_of_nodes()
    num_edges = G.number_of_edges()

    # Density
    density = nx.density(G)

    # Degree of every node
    degrees = dict(G.degree())

    # Average degree
    avg_degree = sum(degrees.values()) / num_nodes

    # Centrality
    centrality = nx.degree_centrality(G)

    # Most important node
    central_node = max(centrality, key=centrality.get)

    # Connected components
    components = list(nx.connected_components(G))

    return {

        "nodes": num_nodes,

        "edges": num_edges,

        "density": density,

        "average_degree": avg_degree,

        "central_node": central_node,

        "connected_components": len(components),

        "degrees": degrees,

        "centrality": centrality

    }