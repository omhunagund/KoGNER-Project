import streamlit as st

# -------------------------------------------------------
# Page Configuration
# -------------------------------------------------------
st.set_page_config(
    page_title="KoGNER",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -------------------------------------------------------
# Title
# -------------------------------------------------------
st.title("🧭 Project Guide")

st.markdown("""
Welcome to **KoGNER**, an AI-powered biomedical text analysis platform for biomedical
named entity recognition, knowledge graph construction, graph neural network analysis,
and knowledge graph distillation.

This page serves as a quick guide to help you navigate the application and follow the
recommended processing workflow. For the best experience, complete each module in the
recommended order shown below.
""")

st.divider()

# -------------------------------------------------------
# Recommended Workflow
# -------------------------------------------------------
st.header("🔄 Recommended Workflow")

st.markdown("""
### Follow the modules in this order:

1. 🧬 Biomedical Named Entity Recognition

2. 📝 NLP Processing

3. 🤖 BioBERT Analysis

4. 🕸️ Knowledge Graph Generation

5. 🧠 GNN Analysis

6. ✨ Knowledge Graph Distillation

7. 📊 Analytics Dashboard

8. ⬇️ Download Results
""")

st.divider()

# -------------------------------------------------------
# Usage Guidelines
# -------------------------------------------------------
st.header("📌 Usage Guidelines")

st.info("""
• Begin with the **Biomedical NER** module.

• Complete each processing stage before moving to the next.

• Follow the modules in the recommended workflow.

• Review the **Analytics Dashboard** after processing.

• Export the generated outputs using **Download Results**.
""")

st.divider()

# -------------------------------------------------------
# Footer
# -------------------------------------------------------
st.caption(
    "KoGNER • Final Year Project • Computer Science & Engineering (Data Science)"
)