import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.lines import Line2D

from knowledge_graph.graph_builder import build_graph
from models.distillation.distill import distill_graph

# --------------------------------------------------------
# Page Configuration
# --------------------------------------------------------

st.set_page_config(
    page_title="Knowledge Graph Distillation | KoGNER",
    page_icon="✨",
    layout="wide"
)

st.title("✨ Knowledge Graph Distillation")

st.markdown(
    """
This module simplifies the biomedical knowledge graph by retaining
only the most important biomedical entities using graph centrality
based knowledge graph distillation.
"""
)

st.divider()

# --------------------------------------------------------
# Session Validation
# --------------------------------------------------------

if "biobert_entities" not in st.session_state:

    st.warning(
        "Please analyze biomedical text first."
    )

    st.stop()

entities = st.session_state["biobert_entities"]

if len(entities) == 0:

    st.warning(
        "No biomedical entities found."
    )

    st.stop()

# --------------------------------------------------------
# Build Knowledge Graph
# --------------------------------------------------------

graph = build_graph(entities)

# --------------------------------------------------------
# Distillation Settings
# --------------------------------------------------------

st.header("⚙️ Distillation Settings")

keep_ratio = st.slider(
    "Keep Top Percentage of Nodes",
    min_value=0.2,
    max_value=1.0,
    value=0.5,
    step=0.1
)

distilled_graph, ranked_nodes = distill_graph(
    graph,
    keep_ratio
)

st.divider()

# --------------------------------------------------------
# Statistics
# --------------------------------------------------------

st.header("📊 Distillation Statistics")

compression = (
    (
        graph.number_of_nodes()
        - distilled_graph.number_of_nodes()
    )
    / graph.number_of_nodes()
) * 100

retention = 100 - compression

col1, col2, col3 = st.columns(3)

col1.metric(
    "Original Nodes",
    graph.number_of_nodes()
)

col2.metric(
    "Distilled Nodes",
    distilled_graph.number_of_nodes()
)

col3.metric(
    "Compression",
    f"{compression:.1f}%"
)

col4, col5, col6 = st.columns(3)

col4.metric(
    "Original Edges",
    graph.number_of_edges()
)

col5.metric(
    "Distilled Edges",
    distilled_graph.number_of_edges()
)

col6.metric(
    "Retention",
    f"{retention:.1f}%"
)

st.divider()

# --------------------------------------------------------
# Graph Color Mapping
# --------------------------------------------------------

COLOR_MAP = {

    "DRUG": "#2ECC71",
    "DISEASE": "#E74C3C",
    "BIOLOGICAL_STRUCTURE": "#3498DB",
    "PROCEDURE": "#F39C12",
    "THERAPY": "#9B59B6",
    "SYMPTOM": "#F1C40F"

}

DEFAULT_COLOR = "#95A5A6"

# --------------------------------------------------------
# Shared Graph Drawing Function
# --------------------------------------------------------

def draw_graph(graph, title):

    fig, ax = plt.subplots(figsize=(8.5, 6.5))

    pos = nx.spring_layout(
        graph,
        seed=42,
        k=1.0,
        iterations=100
    )

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
        width=2.2,
        edge_color="#7F8C8D",
        alpha=0.8,
        ax=ax
    )

    nx.draw_networkx_labels(
        graph,
        pos,
        font_size=9,
        font_weight="bold",
        ax=ax
    )

    legend_elements = [

        Line2D([0],[0], marker='o', color='w',
               label='Drug',
               markerfacecolor=COLOR_MAP["DRUG"],
               markeredgecolor='black',
               markersize=8),

        Line2D([0],[0], marker='o', color='w',
               label='Disease',
               markerfacecolor=COLOR_MAP["DISEASE"],
               markeredgecolor='black',
               markersize=8),

        Line2D([0],[0], marker='o', color='w',
               label='Biological Structure',
               markerfacecolor=COLOR_MAP["BIOLOGICAL_STRUCTURE"],
               markeredgecolor='black',
               markersize=8),

        Line2D([0],[0], marker='o', color='w',
               label='Procedure',
               markerfacecolor=COLOR_MAP["PROCEDURE"],
               markeredgecolor='black',
               markersize=8),

        Line2D([0],[0], marker='o', color='w',
               label='Therapy',
               markerfacecolor=COLOR_MAP["THERAPY"],
               markeredgecolor='black',
               markersize=8),

        Line2D([0],[0], marker='o', color='w',
               label='Symptom',
               markerfacecolor=COLOR_MAP["SYMPTOM"],
               markeredgecolor='black',
               markersize=8)

    ]

    ax.legend(
        handles=legend_elements,
        fontsize=8,
        loc="upper left",
        frameon=True,
        fancybox=True,
        shadow=True
    )

    ax.set_title(
        title,
        fontsize=15,
        fontweight="bold",
        pad=12
    )

    ax.set_axis_off()

    plt.tight_layout()

    return fig

# --------------------------------------------------------
# Side-by-Side Graph Comparison
# --------------------------------------------------------

st.header("🕸️ Graph Comparison")

left, right = st.columns(2)

with left:

    st.subheader("📘 Original Knowledge Graph")

    st.pyplot(
        draw_graph(
            graph,
            "Original Graph"
        )
    )

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Nodes", graph.number_of_nodes())

    with col2:
        st.metric("Edges", graph.number_of_edges())


with right:

    st.subheader("✨ Distilled Knowledge Graph")

    st.pyplot(
        draw_graph(
            distilled_graph,
            "Distilled Graph"
        )
    )

    col3, col4 = st.columns(2)

    with col3:
        st.metric("Nodes", distilled_graph.number_of_nodes())

    with col4:
        st.metric("Edges", distilled_graph.number_of_edges())

st.divider()

# --------------------------------------------------------
# Entity Importance Ranking
# --------------------------------------------------------

st.header("🏆 Entity Importance Ranking")

ranking_df = pd.DataFrame(
    ranked_nodes,
    columns=[
        "Biomedical Entity",
        "Importance Score"
    ]
)

ranking_df.index = ranking_df.index + 1
ranking_df.index.name = "Rank"

ranking_df["Importance Score"] = ranking_df[
    "Importance Score"
].round(4)

st.dataframe(
    ranking_df,
    use_container_width=True
)

st.divider()

# --------------------------------------------------------
# Retained Biomedical Entities
# --------------------------------------------------------

st.header("✅ Retained Biomedical Entities")

retained_entities = []

for node in distilled_graph.nodes(data=True):

    retained_entities.append({

        "Biomedical Entity": node[0],

        "Entity Type": node[1].get(
            "entity_type",
            "-"
        ),

        "Confidence": node[1].get(
            "confidence",
            "-"
        )

    })

retained_df = pd.DataFrame(
    retained_entities
)

st.dataframe(
    retained_df,
    use_container_width=True,
    hide_index=True
)

st.divider()

# --------------------------------------------------------
# Distillation Performance
# --------------------------------------------------------

st.header("📈 Distillation Performance")

removed_nodes = (
    graph.number_of_nodes()
    - distilled_graph.number_of_nodes()
)

removed_edges = (
    graph.number_of_edges()
    - distilled_graph.number_of_edges()
)

col1, col2 = st.columns(2)

with col1:

    st.metric(
        "Removed Nodes",
        removed_nodes
    )

    st.metric(
        "Compression",
        f"{compression:.1f}%"
    )

with col2:

    st.metric(
        "Removed Edges",
        removed_edges
    )

    st.metric(
        "Retention",
        f"{retention:.1f}%"
    )

st.divider()

# --------------------------------------------------------
# Top Biomedical Entity
# --------------------------------------------------------

st.header("🧬 Most Important Biomedical Entity")

top_entity = ranking_df.iloc[0]["Biomedical Entity"]

top_score = ranking_df.iloc[0]["Importance Score"]

entity_type = ""

confidence = ""

for node, attrs in graph.nodes(data=True):

    if node == top_entity:

        entity_type = attrs.get(
            "entity_type",
            "-"
        )

        confidence = attrs.get(
            "confidence",
            "-"
        )

        break

card1, card2 = st.columns(2)

with card1:

    st.metric(
        "Biomedical Entity",
        top_entity
    )

    st.metric(
        "Entity Type",
        entity_type
    )

with card2:

    st.metric(
        "Importance Score",
        f"{top_score:.4f}"
    )

    st.metric(
        "Confidence",
        f"{confidence:.2f}%"
    )

st.divider()

# --------------------------------------------------------
# Distillation Insights
# --------------------------------------------------------

st.header("💡 Distillation Insights")

st.info(
    f"""
**Knowledge Graph Distillation Summary**

- Original Graph contained **{graph.number_of_nodes()} biomedical entities**
  connected by **{graph.number_of_edges()} relationships**.

- After Knowledge Graph Distillation, the graph contains
  **{distilled_graph.number_of_nodes()} important biomedical entities**
  connected by **{distilled_graph.number_of_edges()} relationships**.

- This represents a **{compression:.1f}% reduction**
  while preserving the most influential biomedical entities
  based on graph centrality measures.

- The retained entities are ranked using a weighted combination of
  Degree Centrality, Betweenness Centrality and Closeness Centrality.
"""
)