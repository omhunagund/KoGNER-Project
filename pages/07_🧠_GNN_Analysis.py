import streamlit as st
import matplotlib.pyplot as plt

from knowledge_graph.graph_builder import build_graph
from models.gnn.analyzer import analyze_graph

st.set_page_config(
    page_title="GNN Analysis | KoGNER",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 Graph Neural Network Analysis")

st.markdown(
    "Analyze the biomedical knowledge graph using graph-based statistics."
)

st.divider()

# -------------------------------------------------
# Check Session
# -------------------------------------------------

if "biobert_entities" not in st.session_state:

    st.warning(
        "Please run Biomedical NER first."
    )

    st.stop()

entities = st.session_state.biobert_entities

if len(entities) == 0:

    st.warning("No biomedical entities found.")

    st.stop()

# -------------------------------------------------
# Build Graph
# -------------------------------------------------

graph = build_graph(entities)

results = analyze_graph(graph)

# -------------------------------------------------
# Summary
# -------------------------------------------------

st.header("📊 Graph Statistics")

c1, c2, c3 = st.columns(3)

c1.metric("Nodes", results["nodes"])
c2.metric("Edges", results["edges"])
c3.metric("Connected Components", results["connected_components"])

c4, c5, c6 = st.columns(3)

c4.metric("Density", f"{results['density']:.2f}")
c5.metric("Average Degree", f"{results['average_degree']:.2f}")
c6.metric("Central Node", results["central_node"])

st.divider()

# -------------------------------------------------
# Degree Distribution
# -------------------------------------------------

st.header("📈 Node Degree Distribution")

degrees = results["degrees"]

PURPLE = "#9B59B6"

fig, ax = plt.subplots(figsize=(8, 4))

bars = ax.bar(
    degrees.keys(),
    degrees.values(),
    color=PURPLE,
    edgecolor="black",
    linewidth=1.2
)

# Display degree values above each bar
for bar in bars:
    height = bar.get_height()
    ax.text(
        bar.get_x() + bar.get_width()/2,
        height + 0.05,
        f"{int(height)}",
        ha="center",
        va="bottom",
        fontsize=10,
        fontweight="bold"
    )

ax.set_title(
    "Node Degree Distribution",
    fontsize=16,
    fontweight="bold",
    pad=15
)

ax.set_xlabel(
    "Nodes",
    fontsize=12,
    fontweight="bold"
)

ax.set_ylabel(
    "Degree",
    fontsize=12,
    fontweight="bold"
)

ax.grid(
    axis="y",
    linestyle="--",
    alpha=0.3
)

plt.xticks(rotation=30)

plt.tight_layout()

st.pyplot(fig)
plt.close(fig)

st.divider()

# -------------------------------------------------
# Centrality
# -------------------------------------------------

st.header("⭐ Node Centrality")

centrality = results["centrality"]

PURPLE = "#9B59B6"

fig2, ax2 = plt.subplots(figsize=(8, 4))

bars = ax2.bar(
    centrality.keys(),
    centrality.values(),
    color=PURPLE,
    edgecolor="black",
    linewidth=1.2
)

# Display centrality values above each bar
for bar in bars:
    height = bar.get_height()
    ax2.text(
        bar.get_x() + bar.get_width()/2,
        height + 0.002,
        f"{height:.2f}",
        ha="center",
        va="bottom",
        fontsize=9,
        fontweight="bold"
    )

ax2.set_title(
    "Node Centrality Analysis",
    fontsize=16,
    fontweight="bold",
    pad=15
)

ax2.set_xlabel(
    "Nodes",
    fontsize=12,
    fontweight="bold"
)

ax2.set_ylabel(
    "Centrality Score",
    fontsize=12,
    fontweight="bold"
)

ax2.grid(
    axis="y",
    linestyle="--",
    alpha=0.3
)

plt.xticks(rotation=30)

plt.tight_layout()

st.pyplot(fig2)
plt.close(fig2)

st.divider()

# -------------------------------------------------
# Degree Table
# -------------------------------------------------

st.header("📋 Node Degrees")

st.dataframe(
    {
        "Node": list(degrees.keys()),
        "Degree": list(degrees.values())
    },
    hide_index=True,
    use_container_width=True
)

st.divider()

# -------------------------------------------------
# Central Node
# -------------------------------------------------

st.success(
    f"⭐ Most Important Node: **{results['central_node']}**"
)