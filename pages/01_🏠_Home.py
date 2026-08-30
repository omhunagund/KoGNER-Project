import streamlit as st

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------
st.set_page_config(
    page_title="Home | KoGNER",
    page_icon="🏠",
    layout="wide"
)

# --------------------------------------------------
# Hero Section
# --------------------------------------------------

st.title("🧬 KoGNER")

st.markdown(
    """
    ### Knowledge Graph Distillation for Biomedical Named Entity Recognition
    """
)

st.markdown(
    """
    Welcome to **KoGNER**, an AI-powered biomedical text analysis platform that
    combines **Natural Language Processing (NLP)**, **BioBERT**, **Knowledge Graphs**,
    and **Graph Neural Networks (GNN)** to identify biomedical entities and
    discover meaningful relationships from biomedical literature.
    """
)

st.divider()

# --------------------------------------------------
# About KoGNER
# --------------------------------------------------

st.header("📖 About KoGNER")

st.write(
    """
KoGNER is a biomedical named entity recognition platform developed to
extract important biomedical entities such as diseases, chemicals,
genes, proteins, DNA, RNA, cell lines, and cell types from biomedical
text.

The application integrates Natural Language Processing (NLP),
BioBERT-based deep learning, Knowledge Graph construction, and Graph
Neural Networks (GNN) to provide an interactive biomedical text analysis
environment.
"""
)

st.divider()

# --------------------------------------------------
# Objectives
# --------------------------------------------------

st.header("🎯 Project Objectives")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.info("🧬\n\n**Biomedical\nEntity Recognition**")

with col2:
    st.info("🕸️\n\n**Knowledge\nGraph Construction**")

with col3:
    st.info("🤖\n\n**Relationship\nAnalysis using GNN**")

with col4:
    st.info("📊\n\n**Interactive\nVisualization**")

st.divider()

# --------------------------------------------------
# Technologies & Frameworks
# --------------------------------------------------

st.header("🛠 Technologies & Frameworks")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Core Frameworks")
    st.markdown("""
- 🧹 Natural Language Processing (NLP)
- 🧠 BioBERT
- 🕸️ Knowledge Graph
- 🤖 Graph Neural Network (GNN)
""")

with col2:
    st.subheader("Development Tools")
    st.markdown("""
- 🐍 Python
- 🌐 Streamlit
- 📚 spaCy
- 🤗 Transformers
- 🔥 PyTorch
- 📈 NetworkX
""")

st.divider()

# --------------------------------------------------
# Datasets
# --------------------------------------------------

st.header("📂 Datasets Used")

col1, col2, col3 = st.columns(3)

with col1:
    st.success("""
### BC5CDR

✔ Diseases

✔ Chemicals

**Primary Dataset**
""")

with col2:
    st.info("""
### NCBI Disease Corpus

✔ Disease Recognition

**Evaluation Dataset**
""")

with col3:
    st.warning("""
### JNLPBA

✔ Genes

✔ Proteins

✔ DNA

✔ RNA

**Extended Biomedical Entities**
""")

st.divider()

# --------------------------------------------------
# Project Statistics
# --------------------------------------------------

st.header("📈 Project Overview")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Datasets", "3")
col2.metric("Frameworks", "4")
col3.metric("Entity Types", "9")
col4.metric("Modules", "8")

st.divider()

# --------------------------------------------------
# Workflow
# --------------------------------------------------

st.header("🏗 System Workflow")

st.code("""
📝 Biomedical Text
       │
       ▼
🧹 NLP Processing
       │
       ▼
🤖 BioBERT Analysis
       │
       ▼
🧬 Biomedical Entity Recognition
       │
       ▼
🕸️ Knowledge Graph Construction
       │
       ▼
🧠 Graph Neural Network Analysis
       │
       ▼
✨ Knowledge Graph Distillation 
       │
       ▼
📊 Analytics Dashboard
       │
       ▼
⬇️ Download Results
""", language="text")

st.divider()

# --------------------------------------------------
# Get Started
# --------------------------------------------------

st.header("🚀 Get Started")

st.markdown("""
Use the navigation panel on the left to explore each module of **KoGNER**.

### Available Modules

- 🏠 Home
- 📘 About Project
- 🧬 Biomedical NER
- 📝 NLP Processing
- 🤖 BioBERT Analysis
- 🕸️ Knowledge Graph
- 🧠 GNN Analysis
- ✨ Knowledge Graph Distillation
- 📊 Analytics Dashboard
- ⬇️ Download Results
""")

st.success("✅ KoGNER is ready for biomedical text analysis.")