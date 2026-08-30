import streamlit as st

# ----------------------------------------------------
# Page Configuration
# ----------------------------------------------------

st.set_page_config(
    page_title="About Project | KoGNER",
    page_icon="📘",
    layout="wide"
)

# ----------------------------------------------------
# Header
# ----------------------------------------------------

st.title("📘 About Project")

st.write(
    """
    This page provides a detailed overview of the KoGNER project, including its
    objectives, the problem it addresses, and the proposed biomedical text
    analysis approach.
    """
)

# ----------------------------------------------------
# Contents
# ----------------------------------------------------

st.markdown("""
### 📑 Contents

- 📖 Project Overview
- 🎯 Project Objectives
- ❗ Problem Statement
- 🔄 Proposed Solution
- 🛠️ Technologies Used
- 📂 Project Modules
- 📂 Project Structure
- 📊 Datasets Used
- 🎯 Expected Project Outcomes
""")

st.divider()

# ====================================================
# 1. PROJECT OVERVIEW
# ====================================================

st.header("📖 Project Overview")

st.write(
    """
    **KoGNER (Knowledge Graph Distillation for Biomedical Named Entity Recognition)**
    is an AI-powered biomedical text analysis framework designed to automatically
    identify important biomedical entities from unstructured biomedical literature
    and organize them into a structured knowledge graph.

    The framework combines **Natural Language Processing (NLP)**,
    **BioBERT-based Biomedical Named Entity Recognition (NER)**,
    **Knowledge Graph Construction**, **Graph Analytics**, and
    **Knowledge Graph Distillation** to simplify complex biomedical information
    while preserving the most meaningful biomedical concepts.

    By integrating multiple AI techniques into a single interactive Streamlit
    application, KoGNER enables users to visualize biomedical relationships,
    analyze graph structures, identify influential biomedical entities, and
    export processed results for further research and analysis.
    """
)

st.divider()

# ====================================================
# 2. PROJECT OBJECTIVES
# ====================================================

st.header("🎯 Project Objectives")

st.markdown("""

- ✅ Extract biomedical entities from biomedical text using BioBERT.
- ✅ Perform Natural Language Processing (NLP) for text preprocessing.
- ✅ Construct a biomedical Knowledge Graph representing entity relationships.
- ✅ Analyze graph structure using graph analytics techniques.
- ✅ Simplify complex knowledge graphs using Knowledge Graph Distillation.
- ✅ Provide interactive visualizations for biomedical analysis.
- ✅ Generate downloadable analysis results for further research.
""")

st.divider()

# ====================================================
# 3. PROBLEM STATEMENT
# ====================================================

st.header("❗ Problem Statement")

st.write(
    """
    Biomedical research publications contain a vast amount of valuable information,
    including diseases, drugs, genes, proteins, DNA, RNA, symptoms, and other
    biomedical entities. Manually identifying these entities and understanding
    their relationships is both time-consuming and challenging due to the rapidly
    increasing volume of biomedical literature.

    While traditional Named Entity Recognition (NER) techniques can identify
    biomedical entities, they often provide limited insight into how those entities
    are connected. Furthermore, large biomedical knowledge graphs may become highly
    complex and difficult to interpret.

    KoGNER addresses these challenges by combining BioBERT-based biomedical entity
    recognition with Knowledge Graph construction, graph analytics, and Knowledge
    Graph Distillation. This approach preserves the most important biomedical
    concepts while reducing graph complexity, enabling researchers to better
    understand biomedical information through an interactive and visually intuitive
    platform.
    """
)

st.divider()

# ============================
# Proposed Solution
# ============================

st.header("🔄 Proposed Solution")

st.write("""
KoGNER follows a modular biomedical text analysis pipeline that combines
Natural Language Processing (NLP), BioBERT-based Biomedical Named Entity Recognition (NER),
Knowledge Graph Construction, Graph Analytics, and Knowledge Graph Distillation
to transform unstructured biomedical text into meaningful biomedical knowledge,
interactive visualizations, and downloadable analysis results.
""")

st.markdown("### 🧬 KoGNER Processing Pipeline")

steps = [
    "📝<br><b>Biomedical Text</b>",
    "🧠<br><b>NLP Processing</b>",
    "🤖<br><b>BioBERT NER</b>",
    "🧬<br><b>Biomedical Entities</b>",
    "🕸️<br><b>Knowledge Graph</b>",
    "📊<br><b>Graph Analytics</b>",
    "✂️<br><b>Graph Distillation</b>",
    "📦<br><b>Visualization & Export</b>"
]

# Card -> Arrow -> Card -> Arrow ...
layout = []
for i in range(len(steps)):
    layout.append(2)
    if i != len(steps) - 1:
        layout.append(0.35)

cols = st.columns(layout)

col_index = 0

for i, step in enumerate(steps):

    # Pipeline Card
    with cols[col_index]:
        st.markdown(
            f"""
            <div style="
                border:2px solid #2E8B57;
                border-radius:12px;
                height:95px;
                background-color:#1c1f26;
                display:flex;
                justify-content:center;
                align-items:center;
                text-align:center;
                font-size:18px;
                font-weight:bold;
            ">
                {step}
            </div>
            """,
            unsafe_allow_html=True
        )

    col_index += 1

    # Arrow
    if i != len(steps) - 1:
        with cols[col_index]:
            st.markdown(
                """
                <div style="
                    height:95px;
                    display:flex;
                    justify-content:center;
                    align-items:center;
                    font-size:28px;
                    color:#00D084;
                    font-weight:bold;
                ">
                    ➜
                </div>
                """,
                unsafe_allow_html=True
            )
        col_index += 1

st.write("")
st.write("")

st.success("Complete Biomedical Knowledge Graph Distillation Pipeline")

st.markdown("### 📄 Workflow Description")

workflow = {
    "Pipeline Stage": [
        "Biomedical Text",
        "NLP Processing",
        "BioBERT NER",
        "Biomedical Entity Extraction",
        "Knowledge Graph Construction",
        "Graph Analytics",
        "Knowledge Graph Distillation",
        "Visualization & Export"
    ],

    "Description": [
        "Accept biomedical text input from the user.",
        "Perform text cleaning, tokenization, lemmatization and POS tagging.",
        "Detect biomedical entities using the BioBERT model.",
        "Generate structured biomedical entities with confidence scores.",
        "Construct a biomedical knowledge graph from extracted entities.",
        "Compute graph statistics and identify important biomedical concepts.",
        "Reduce graph complexity while preserving the most influential entities.",
        "Visualize results and export processed analysis files."
    ]
}

st.table(workflow)

st.divider()

# ====================================================
# 5. TECHNOLOGIES USED
# ====================================================

st.header("🛠️ Technologies Used")

technology_table = {
    "Category": [
        "Programming Language",
        "Natural Language Processing",
        "Biomedical NER",
        "Deep Learning",
        "Graph Processing",
        "Data Processing",
        "Visualization",
        "User Interface"
    ],
    "Technology": [
        "Python",
        "spaCy",
        "Clinical-AI-Apollo / Medical-NER",
        "Transformers, PyTorch",
        "NetworkX",
        "Pandas",
        "Matplotlib",
        "Streamlit"
    ]
}

st.table(technology_table)

st.divider()

# ====================================================
# 6. PROJECT MODULES
# ====================================================

st.header("📂 Project Modules")

modules = {
    "Module": [
        "Home",
        "Biomedical NER",
        "NLP Processing",
        "BioBERT Analysis",
        "Knowledge Graph",
        "GNN Analysis",
        "Knowledge Graph Distillation",
        "Analytics Dashboard",
        "Download Results"
    ],

    "Purpose": [
        "Introduces KoGNER and application overview.",
        "Extracts biomedical entities from biomedical text.",
        "Performs preprocessing, tokenization and linguistic analysis.",
        "Displays BioBERT predictions and confidence analysis.",
        "Constructs biomedical knowledge graphs.",
        "Performs graph statistics and centrality analysis.",
        "Simplifies biomedical knowledge graphs.",
        "Summarizes complete biomedical analysis.",
        "Exports analysis results into CSV files."
    ]
}

st.table(modules)

st.divider()

st.header("📂 Project Structure")

project_structure = {
    "Folder / File": [
        "app.py",
        "pages/",
        "models/",
        "knowledge_graph/",
        "nlp/",
        "utils/",
        "tests/",
        "data/",
        "outputs/",
        "assets/"
    ],

    "Purpose": [
        "Main Streamlit application entry point.",
        "Contains all Streamlit application pages.",
        "BioBERT, GNN and Knowledge Graph Distillation modules.",
        "Knowledge graph construction and processing.",
        "Natural Language Processing utilities.",
        "Helper and validation functions.",
        "Unit testing scripts for all major modules.",
        "Biomedical datasets and processed data.",
        "Generated CSV files, predictions and reports.",
        "Project images, icons and UI resources."
    ]
}

st.table(project_structure)

st.divider()

st.header("📊 Datasets Used")

datasets = {
    "Dataset": [
        "BC5CDR",
        "NCBI Disease Corpus",
        "JNLPBA"
    ],

    "Purpose": [
        "Training dataset for disease and chemical entity recognition.",
        "Benchmark dataset for disease entity recognition.",
        "Training dataset for gene, protein, DNA, RNA and cell entity recognition."
    ]
}

st.table(datasets)

st.divider()

st.header("🎯 Expected Project Outcomes")

st.success("""
The KoGNER framework is expected to provide:

✅ Accurate Biomedical Named Entity Recognition using BioBERT.

✅ Efficient biomedical Knowledge Graph construction.

✅ Graph Analytics to identify important biomedical concepts.

✅ Knowledge Graph Distillation for reducing graph complexity while preserving key information.

✅ Interactive visualization of biomedical entities and relationships.

✅ Downloadable CSV reports for further biomedical research.

✅ A simple, user-friendly Streamlit application suitable for research demonstrations and academic projects.
""")

st.success(
    "🎉 You have reached the end of the About Project section. Continue exploring the remaining KoGNER modules using the navigation panel."
)

st.write("")
st.write("")