import streamlit as st
import pandas as pd

from utils.validation import validate_text
from nlp.preprocessing import preprocess_text
from models.biobert.predict import predict_entities


# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Biomedical NER | KoGNER",
    page_icon="🧬",
    layout="wide"
)


# --------------------------------------------------
# Session State Initialization
# --------------------------------------------------

if "biomedical_text" not in st.session_state:
    st.session_state.biomedical_text = ""

if "predictions" not in st.session_state:
    st.session_state.predictions = []

if "clean_text" not in st.session_state:
    st.session_state.clean_text = ""

if "tokens" not in st.session_state:
    st.session_state.tokens = []

if "lemmas" not in st.session_state:
    st.session_state.lemmas = []

if "pos_tags" not in st.session_state:
    st.session_state.pos_tags = []


# --------------------------------------------------
# Header
# --------------------------------------------------

st.title("🧬 Biomedical Named Entity Recognition")

st.markdown("""
Extract biomedical entities such as **Diseases, Chemicals,
Genes, Proteins, DNA, RNA, Cell Lines, and Cell Types**
from biomedical text.
""")

st.divider()


# --------------------------------------------------
# Input Section
# --------------------------------------------------

st.header("📝 Enter Biomedical Text")

text = st.text_area(
    "Biomedical Text",
    value=st.session_state.biomedical_text,
    height=220,
    placeholder="Paste biomedical research text here..."
)

st.session_state.biomedical_text = text

st.divider()


# --------------------------------------------------
# Example Text
# --------------------------------------------------

st.header("📂 Example Biomedical Text")

example_text = (
    "The patient is a 54-year-old male presenting with acute chest pain radiating to the left arm. "
    "Initial EKG shows ST-elevation in leads V1-V4. "
    "Troponin-I levels are elevated at 4.2 ng/mL. "
    "Administered aspirin 325 mg and initiated on continuous heparin infusion."
)

if st.button("📄 Load Example Text"):
    st.session_state.biomedical_text = example_text
    st.rerun()

st.divider()


# --------------------------------------------------
# Analyze
# --------------------------------------------------

st.header("🔎 Analyze")

analyze = st.button(
    "🚀 Analyze Biomedical Text",
    use_container_width=True
)


# --------------------------------------------------
# Analysis Pipeline
# --------------------------------------------------

if analyze:

    valid, message = validate_text(
        st.session_state.biomedical_text
    )

    if not valid:

        st.error(message)

    else:

        st.success("✅ Biomedical text analyzed successfully.")

        # ----------------------------------------
        # NLP Preprocessing
        # ----------------------------------------

        preprocessed = preprocess_text(
            st.session_state.biomedical_text
        )

        st.session_state.clean_text = preprocessed["clean_text"]
        st.session_state.tokens = preprocessed["tokens"]
        st.session_state.lemmas = preprocessed["lemmas"]
        st.session_state.pos_tags = preprocessed["pos_tags"]

        st.success("✅ NLP preprocessing completed.")

        # ----------------------------------------
        # BioBERT Prediction
        # ----------------------------------------

        with st.spinner("Running BioBERT model..."):

            entities = predict_entities(
                st.session_state.biomedical_text
            )

        # Save predictions
        st.session_state.predictions = entities

        # Save specifically for the BioBERT Analysis page
        st.session_state.biobert_entities = entities

        st.success("✅ Biomedical entities extracted successfully.")

        # ----------------------------------------
        # Analysis Summary
        # ----------------------------------------

        st.divider()

        st.header("📊 Analysis Summary")

        st.metric(
            label="Entities Detected",
            value=len(entities)
        )

        # ----------------------------------------
        # Entity Table
        # ----------------------------------------

        st.divider()

        st.header("📋 Extracted Biomedical Entities")

        if len(entities) > 0:

            df = pd.DataFrame(entities)

            st.dataframe(
                df,
                use_container_width=True,
                hide_index=True
            )

        else:

            st.warning(
                "No biomedical entities detected."
            )

        # ----------------------------------------
        # Pipeline Status
        # ----------------------------------------

        st.divider()

        st.header("⚙ Pipeline Status")

        st.success("✔ Validation Completed")
        st.success("✔ NLP Preprocessing Completed")
        st.success("✔ BioBERT Inference Completed")
        st.success("✔ Session State Updated")


# --------------------------------------------------
# Debug (Temporary)
# --------------------------------------------------

with st.expander("⚙ Debug Session State"):

    st.write(st.session_state)