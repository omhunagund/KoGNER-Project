import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="NLP Processing | KoGNER",
    page_icon="📝",
    layout="wide"
)

st.title("📝 NLP Processing")

st.markdown(
    "View the preprocessing results generated from the biomedical text."
)

st.divider()

# --------------------------------------------------
# Check Session State
# --------------------------------------------------

if "clean_text" not in st.session_state:

    st.warning(
        "Please analyze biomedical text first from the Biomedical NER page."
    )

    st.stop()

# --------------------------------------------------
# Clean Text
# --------------------------------------------------

st.header("🧹 Clean Text")

st.code(st.session_state["clean_text"])

st.divider()

# --------------------------------------------------
# Statistics
# --------------------------------------------------

tokens = st.session_state["tokens"]
lemmas = st.session_state["lemmas"]
pos_tags = st.session_state["pos_tags"]

token_count = len(tokens)
unique_tokens = len(set(tokens))
sentence_count = st.session_state["clean_text"].count(".")
word_count = len(st.session_state["clean_text"].split())

st.header("📊 NLP Statistics")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Words", word_count)
col2.metric("Tokens", token_count)
col3.metric("Sentences", sentence_count)
col4.metric("Unique Tokens", unique_tokens)

st.divider()

# --------------------------------------------------
# Tokens
# --------------------------------------------------

st.header("🔤 Tokens")

token_df = pd.DataFrame({
    "Token": tokens
})

st.dataframe(
    token_df,
    use_container_width=True,
    hide_index=True
)

st.divider()

# --------------------------------------------------
# Lemmatization
# --------------------------------------------------

st.header("📚 Lemmatization")

lemma_df = pd.DataFrame({
    "Token": tokens,
    "Lemma": lemmas
})

st.dataframe(
    lemma_df,
    use_container_width=True,
    hide_index=True
)

st.divider()

# --------------------------------------------------
# POS Tags
# --------------------------------------------------

st.header("🏷 Part of Speech Tags")

pos_df = pd.DataFrame(pos_tags)

st.dataframe(
    pos_df,
    use_container_width=True,
    hide_index=True
)

st.divider()

# --------------------------------------------------
# POS Distribution
# --------------------------------------------------

st.header("📈 POS Distribution")

pos_counts = pos_df["POS"].value_counts()

TEAL = "#009688"

fig, ax = plt.subplots(figsize=(8, 4))

bars = ax.bar(
    pos_counts.index,
    pos_counts.values,
    color=TEAL,
    edgecolor="black",
    linewidth=1.2
)

# Display values above each bar
for bar in bars:
    height = bar.get_height()
    ax.text(
        bar.get_x() + bar.get_width()/2,
        height + 0.1,
        f"{int(height)}",
        ha="center",
        va="bottom",
        fontsize=10,
        fontweight="bold"
    )

ax.set_title(
    "Part-of-Speech (POS) Distribution",
    fontsize=16,
    fontweight="bold",
    pad=15
)

ax.set_xlabel(
    "POS Tags",
    fontsize=12,
    fontweight="bold"
)

ax.set_ylabel(
    "Frequency",
    fontsize=12,
    fontweight="bold"
)

ax.grid(
    axis="y",
    linestyle="--",
    alpha=0.3
)

plt.tight_layout()

st.pyplot(fig)
plt.close(fig)