import streamlit as st
import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd
from matplotlib.lines import Line2D

from knowledge_graph.graph_builder import build_graph

# -----------------------------------------
# Page Configuration
# -----------------------------------------

st.set_page_config(
    page_title="Knowledge Graph | KoGNER",
    page_icon="🕸️",
    layout="wide"
)

st.title("🕸️ Knowledge Graph")

st.markdown(
    "Visualize relationships between biomedical entities."
)

st.divider()

# -----------------------------------------
# Check Session
# -----------------------------------------

if "biobert_entities" not in st.session_state:

    st.warning(
        "Please analyze biomedical text first."
    )

    st.stop()

entities = st.session_state.biobert_entities

graph = build_graph(entities)

# -----------------------------------------
# Color Mapping
# -----------------------------------------

COLOR_MAP = {

    "DRUG": "#2ECC71",
    "DISEASE": "#E74C3C",
    "BIOLOGICAL_STRUCTURE": "#3498DB",
    "PROCEDURE": "#F39C12",
    "THERAPY": "#9B59B6",
    "SYMPTOM": "#F1C40F"

}

DEFAULT_COLOR = "#95A5A6"

node_colors = []

for node in graph.nodes():

    entity_type = graph.nodes[node].get(
        "entity_type",
        ""
    )

    node_colors.append(
        COLOR_MAP.get(
            entity_type,
            DEFAULT_COLOR
        )
    )

# -----------------------------------------
# Graph Summary
# -----------------------------------------

st.header("📊 Graph Summary")

col1, col2 = st.columns(2)

col1.metric(
    "Nodes",
    graph.number_of_nodes()
)

col2.metric(
    "Edges",
    graph.number_of_edges()
)

st.divider()

# -----------------------------------------
# Graph Visualization
# -----------------------------------------

st.header("🕸️ Biomedical Knowledge Graph")

fig, ax = plt.subplots(figsize=(10, 7))

pos = nx.spring_layout(
    graph,
    seed=42,
    k=1.2,
    iterations=100
)

nx.draw_networkx_nodes(
    graph,
    pos,
    node_size=1200,
    node_color=node_colors,
    edgecolors="black",
    linewidths=2,
    ax=ax
)

nx.draw_networkx_edges(
    graph,
    pos,
    width=2,
    edge_color="#7F8C8D",
    alpha=0.6,
    ax=ax
)

nx.draw_networkx_labels(
    graph,
    pos,
    font_size=9,
    font_weight="bold",
    font_color="black",
    ax=ax
)

ax.set_axis_off()

# -----------------------------------------
# Legend
# -----------------------------------------

legend_elements = [

    Line2D(
        [0], [0],
        marker='o',
        color='w',
        label='Drug',
        markerfacecolor=COLOR_MAP["DRUG"],
        markeredgecolor='black',
        markersize=10
    ),

    Line2D(
        [0], [0],
        marker='o',
        color='w',
        label='Disease',
        markerfacecolor=COLOR_MAP["DISEASE"],
        markeredgecolor='black',
        markersize=10
    ),

    Line2D(
        [0], [0],
        marker='o',
        color='w',
        label='Biological Structure',
        markerfacecolor=COLOR_MAP["BIOLOGICAL_STRUCTURE"],
        markeredgecolor='black',
        markersize=10
    ),

    Line2D(
        [0], [0],
        marker='o',
        color='w',
        label='Procedure',
        markerfacecolor=COLOR_MAP["PROCEDURE"],
        markeredgecolor='black',
        markersize=10
    ),

    Line2D(
        [0], [0],
        marker='o',
        color='w',
        label='Therapy',
        markerfacecolor=COLOR_MAP["THERAPY"],
        markeredgecolor='black',
        markersize=10
    ),

    Line2D(
        [0], [0],
        marker='o',
        color='w',
        label='Symptom',
        markerfacecolor=COLOR_MAP["SYMPTOM"],
        markeredgecolor='black',
        markersize=10
    )

]

ax.legend(
    handles=legend_elements,
    loc="upper left",
    fontsize=9,
    frameon=True,
    fancybox=True,
    shadow=True
)

ax.set_axis_off()

plt.tight_layout()

st.pyplot(fig)

st.divider()

# -----------------------------------------
# Graph Nodes
# -----------------------------------------

st.header("📋 Graph Nodes")

nodes = []

for node, attrs in graph.nodes(data=True):

    nodes.append({

        "Entity": node,
        "Type": attrs.get("entity_type", ""),
        "Confidence": attrs.get("confidence", "")

    })

nodes_df = pd.DataFrame(nodes)

st.dataframe(
    nodes_df,
    use_container_width=True,
    hide_index=True
)

st.divider()

# -----------------------------------------
# Graph Edges
# -----------------------------------------

st.header("🔗 Graph Edges")

edges = []

for source, target, attrs in graph.edges(data=True):

    edges.append({

        "Source": source,
        "Target": target,
        "Relation": attrs.get("relation", "")

    })

edges_df = pd.DataFrame(edges)

st.dataframe(
    edges_df,
    use_container_width=True,
    hide_index=True
)