import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx

from knowledge_graph.graph_builder import build_graph
from models.distillation.distill import distill_graph

st.set_page_config(
    page_title="Analytics Dashboard | KoGNER",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Analytics Dashboard")

st.markdown(
    """
This dashboard provides an overall summary of the biomedical
text analysis performed by KoGNER.
"""
)

st.divider()

# --------------------------------------------------
# Session Check
# --------------------------------------------------

if "biobert_entities" not in st.session_state:

    st.warning(
        "Please analyze biomedical text first."
    )

    st.stop()

entities = st.session_state.biobert_entities

if len(entities) == 0:

    st.warning(
        "No biomedical entities found."
    )

    st.stop()

graph = build_graph(entities)

keep_ratio = 0.5

distilled_graph, ranked_nodes = distill_graph(
    graph,
    keep_ratio
)

entity_df = pd.DataFrame(entities)

# --------------------------------------------------
# Dashboard Overview
# --------------------------------------------------

st.header("📈 Dashboard Overview")

total_entities = len(entity_df)

graph_nodes = graph.number_of_nodes()

graph_edges = graph.number_of_edges()

distilled_nodes = distilled_graph.number_of_nodes()

avg_confidence = entity_df["Confidence"].mean()

compression = (
    (
        graph_nodes
        - distilled_nodes
    )
    / graph_nodes
) * 100

c1, c2, c3 = st.columns(3)

with c1:

    st.metric(
        "Biomedical Entities",
        total_entities
    )

    st.metric(
        "Knowledge Graph Nodes",
        graph_nodes
    )

with c2:

    st.metric(
        "Knowledge Graph Edges",
        graph_edges
    )

    st.metric(
        "Distilled Nodes",
        distilled_nodes
    )

with c3:

    st.metric(
        "Average Confidence",
        f"{avg_confidence:.2f}%"
    )

    st.metric(
        "Compression",
        f"{compression:.1f}%"
    )

st.divider()

# --------------------------------------------------
# Biomedical Entity Distribution
# --------------------------------------------------

st.header("🧬 Biomedical Entity Distribution")

entity_counts = entity_df["Type"].value_counts()

# KoGNER Theme Color
EMERALD = "#2ECC71"

fig, ax = plt.subplots(figsize=(8, 4))

bars = ax.bar(
    entity_counts.index,
    entity_counts.values,
    color=EMERALD,
    edgecolor="black",
    linewidth=1.2
)

# Add count labels above each bar
for bar in bars:
    height = bar.get_height()
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        height + 0.1,
        f"{int(height)}",
        ha="center",
        va="bottom",
        fontsize=10,
        fontweight="bold"
    )

ax.set_title(
    "Biomedical Entity Distribution",
    fontsize=16,
    fontweight="bold",
    pad=15
)

ax.set_xlabel(
    "Entity Type",
    fontsize=12,
    fontweight="bold"
)

ax.set_ylabel(
    "Count",
    fontsize=12,
    fontweight="bold"
)

ax.grid(
    axis="y",
    linestyle="--",
    alpha=0.3
)

plt.xticks(rotation=45)
plt.tight_layout()

st.pyplot(fig)
plt.close(fig)

st.divider()

# --------------------------------------------------
# Confidence Distribution
# --------------------------------------------------

st.header("📊 Confidence Distribution")

# KoGNER Theme Color
CYAN = "#00BCD4"

fig2, ax2 = plt.subplots(figsize=(8, 4))

# Histogram
ax2.hist(
    entity_df["Confidence"],
    bins=10,
    color=CYAN,
    edgecolor="black",
    linewidth=1.2
)

# Average confidence line
avg_confidence = entity_df["Confidence"].mean()

ax2.axvline(
    avg_confidence,
    color="red",
    linestyle="--",
    linewidth=2,
    label=f"Average Confidence: {avg_confidence:.2f}"
)

ax2.set_title(
    "BioBERT Confidence Distribution",
    fontsize=16,
    fontweight="bold",
    pad=15
)

ax2.set_xlabel(
    "Confidence Score",
    fontsize=12,
    fontweight="bold"
)

ax2.set_ylabel(
    "Frequency",
    fontsize=12,
    fontweight="bold"
)

ax2.grid(
    axis="y",
    linestyle="--",
    alpha=0.3
)

ax2.legend()

plt.tight_layout()

st.pyplot(fig2)
plt.close(fig2)

st.divider()

# --------------------------------------------------
# Top Biomedical Entities
# --------------------------------------------------

st.header("🏆 Top Biomedical Entities")

ranking_df = pd.DataFrame(
    ranked_nodes,
    columns=[
        "Biomedical Entity",
        "Importance Score"
    ]
)

ranking_df["Importance Score"] = (
    ranking_df["Importance Score"]
    .round(3)
)

ranking_df.index = ranking_df.index + 1
ranking_df.index.name = "Rank"

st.dataframe(
    ranking_df.head(5),
    use_container_width=True
)

st.divider()

# --------------------------------------------------
# Graph Analytics
# --------------------------------------------------

st.header("🕸️ Graph Analytics")

degrees = dict(graph.degree())

central_node = max(
    degrees,
    key=degrees.get
)

density = nx.density(graph)

avg_degree = (
    sum(degrees.values())
    / graph.number_of_nodes()
)

connected_components = nx.number_connected_components(
    graph
)

c1, c2 = st.columns(2)

with c1:

    st.metric(
        "Central Biomedical Entity",
        central_node
    )

    st.metric(
        "Graph Density",
        f"{density:.3f}"
    )

with c2:

    st.metric(
        "Average Degree",
        f"{avg_degree:.2f}"
    )

    st.metric(
        "Connected Components",
        connected_components
    )

st.divider()

st.divider()

# --------------------------------------------------
# Analysis Summary
# --------------------------------------------------

st.header("📋 Analysis Highlights")

entity_types = entity_df["Type"].nunique()

st.info(f"""
✅ **Biomedical Entities Detected:** {total_entities}

✅ **Entity Categories Identified:** {entity_types}

✅ **Knowledge Graph Created:** {graph_nodes} nodes and {graph_edges} relationships

✅ **Graph Distillation:** Reduced to {distilled_nodes} important entities ({compression:.1f}% compression)

✅ **Average BioBERT Confidence:** {avg_confidence:.2f}%
""")

st.divider()

# --------------------------------------------------
# Processing Pipeline Status
# --------------------------------------------------

st.header("✅ Processing Progress")

st.progress(100)

st.caption("All processing modules completed successfully.")

col1, col2 = st.columns(2)

with col1:

    st.success("Biomedical NER")

    st.success("NLP Processing")

    st.success("BioBERT Analysis")

    st.success("Knowledge Graph")

with col2:

    st.success("GNN Analysis")

    st.success("Knowledge Graph Distillation")

    st.success("📦 Download Results Ready")

st.divider()

# --------------------------------------------------
# Export Summary
# --------------------------------------------------

st.header("📦 Export Summary")

st.success(
    """
The biomedical analysis has completed successfully.

You can now navigate to the **Download Results**
page to export:

• Biomedical Entities

• Knowledge Graph Nodes

• Knowledge Graph Edges

• GNN Statistics

• Distilled Graph Results
"""
)