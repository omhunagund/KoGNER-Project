import hashlib

import pandas as pd
import streamlit as st

from utils.validation import validate_text
from utils.file_extractor import extract_text_from_file
from nlp.preprocessing import preprocess_text
from models.biobert.predict import predict_entities


st.set_page_config(
    page_title="Biomedical NER | KoGNER",
    page_icon="🧬",
    layout="wide"
)


# -------------------------------------------------
# Session State Initialization
# -------------------------------------------------

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

if "processed_upload_signature" not in st.session_state:
    st.session_state.processed_upload_signature = None


# -------------------------------------------------
# Page Header
# -------------------------------------------------

st.title("🧬 Biomedical Named Entity Recognition")

st.markdown("""
Extract biomedical entities such as **Diseases, Chemicals,
Genes, Proteins, DNA, RNA, Cell Lines, and Cell Types**
from biomedical text.
""")

st.divider()


# -------------------------------------------------
# Manual Text Input
# -------------------------------------------------

st.header("📝 Enter Biomedical Text")

text = st.text_area(
    "Biomedical Text",
    value=st.session_state.biomedical_text,
    height=220,
    placeholder="Paste biomedical research text here..."
)

st.session_state.biomedical_text = text


# -------------------------------------------------
# File Upload
# -------------------------------------------------

st.header("📤 Upload Biomedical File")

uploaded_file = st.file_uploader(
    "Upload a biomedical file",
    type=[
        "pdf",
        "docx",
        "txt",
        "csv",
        "xlsx",
        "jpg",
        "jpeg",
        "png"
    ],
    accept_multiple_files=False,
    help=(
        "Supported formats: PDF, DOCX, TXT, CSV, XLSX, "
        "JPG, JPEG, and PNG."
    )
)


# -------------------------------------------------
# Extract Uploaded File
# -------------------------------------------------

if uploaded_file is not None:

    file_bytes = uploaded_file.getvalue()
    file_signature = hashlib.sha256(file_bytes).hexdigest()

    if file_signature != st.session_state.processed_upload_signature:

        try:
            with st.spinner("Extracting text from uploaded file..."):

                extracted_text = extract_text_from_file(uploaded_file)

            st.session_state.biomedical_text = extracted_text
            st.session_state.processed_upload_signature = file_signature

            st.success(
                f"✅ Text extracted successfully from **{uploaded_file.name}**."
            )

            st.info(
                "The extracted text has been placed in the text box above. "
                "Review or edit it before running the analysis."
            )

            st.rerun()

        except Exception as e:
            st.error(f"❌ Could not extract text from the uploaded file: {e}")


st.divider()


# -------------------------------------------------
# Example Biomedical Text
# -------------------------------------------------

st.header("📂 Example Biomedical Text")

example_text = (
    "The patient is a 54-year-old male presenting with acute chest pain "
    "radiating to the left arm. Initial EKG shows ST-elevation in leads V1-V4. "
    "Troponin-I levels are elevated at 4.2 ng/mL. Administered aspirin 325 mg "
    "and initiated on continuous heparin infusion."
)

if st.button("📄 Load Example Text"):

    st.session_state.biomedical_text = example_text

    # Reset upload tracking so the example text is not replaced
    # by a previously uploaded file.
    st.session_state.processed_upload_signature = None

    st.rerun()


st.divider()


# -------------------------------------------------
# Analyze Biomedical Text
# -------------------------------------------------

st.header("🔎 Analyze")

analyze = st.button(
    "🚀 Analyze Biomedical Text",
    use_container_width=True
)


if analyze:

    valid, message = validate_text(
        st.session_state.biomedical_text
    )

    if not valid:

        st.error(message)

    else:

        st.success(
            "✅ Biomedical text analyzed successfully."
        )

        # ---------------------------------------------
        # NLP Processing
        # ---------------------------------------------

        preprocessed = preprocess_text(
            st.session_state.biomedical_text
        )

        st.session_state.clean_text = preprocessed["clean_text"]
        st.session_state.tokens = preprocessed["tokens"]
        st.session_state.lemmas = preprocessed["lemmas"]
        st.session_state.pos_tags = preprocessed["pos_tags"]

        st.success(
            "✅ NLP preprocessing completed."
        )

        # ---------------------------------------------
        # Biomedical NER
        # ---------------------------------------------

        with st.spinner("Running BioBERT model..."):

            entities = predict_entities(
                st.session_state.biomedical_text
            )

        st.session_state.predictions = entities
        st.session_state.biobert_entities = entities

        st.success(
            "✅ Biomedical entities extracted successfully."
        )

        st.divider()

        # ---------------------------------------------
        # Analysis Summary
        # ---------------------------------------------

        st.header("📊 Analysis Summary")

        st.metric(
            label="Entities Detected",
            value=len(entities)
        )

        st.divider()

        # ---------------------------------------------
        # Extracted Biomedical Entities
        # ---------------------------------------------

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

        st.divider()

        # ---------------------------------------------
        # Pipeline Status
        # ---------------------------------------------

        st.header("⚙ Pipeline Status")

        st.success("✔ Validation Completed")
        st.success("✔ NLP Preprocessing Completed")
        st.success("✔ BioBERT Inference Completed")
        st.success("✔ Session State Updated")


# -------------------------------------------------
# Debug Session State
# -------------------------------------------------

with st.expander("⚙ Debug Session State"):
    st.write(st.session_state)