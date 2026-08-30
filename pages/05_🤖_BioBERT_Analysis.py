import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="BioBERT Analysis | KoGNER",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 BioBERT Analysis")

st.markdown(
    "Explore the biomedical entities predicted by the BioBERT model."
)

st.divider()

# -------------------------------------------------
# Check Session
# -------------------------------------------------

if "biobert_entities" not in st.session_state:

    st.warning(
        "Please analyze biomedical text first from the Biomedical NER page."
    )

    st.stop()

entities = st.session_state["biobert_entities"]

if len(entities) == 0:

    st.warning("No biomedical entities were detected.")

    st.stop()

df = pd.DataFrame(entities)

st.header("📋 Model Information")

col1, col2, col3 = st.columns(3)

col1.info("Model\n\nBioBERT")
col2.info("Framework\n\nTransformers")
col3.info("Task\n\nBiomedical NER")

st.divider()

st.header("📊 Prediction Summary")

total = len(df)
avg_conf = df["Confidence"].mean()
max_conf = df["Confidence"].max()
min_conf = df["Confidence"].min()

c1, c2, c3, c4 = st.columns(4)

c1.metric("Entities", total)
c2.metric("Average Confidence", f"{avg_conf:.2f}%")
c3.metric("Highest", f"{max_conf:.2f}%")
c4.metric("Lowest", f"{min_conf:.2f}%")

st.divider()

st.header("🧬 Detected Biomedical Entities")

st.dataframe(
    df,
    use_container_width=True,
    hide_index=True
)

st.divider()

st.header("📈 Entity Type Distribution")

type_counts = df["Type"].value_counts()

EMERALD = "#2ECC71"

fig, ax = plt.subplots(figsize=(8, 4))

bars = ax.bar(
    type_counts.index,
    type_counts.values,
    color=EMERALD,
    edgecolor="black",
    linewidth=1.2
)

# Display count above each bar
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

plt.xticks(rotation=30)

plt.tight_layout()

st.pyplot(fig)
plt.close(fig)

st.divider()

st.header("🎯 Confidence Scores")

CYAN = "#00BCD4"

fig2, ax2 = plt.subplots(figsize=(8, 4))

# Histogram
ax2.hist(
    df["Confidence"],
    bins=10,
    color=CYAN,
    edgecolor="black",
    linewidth=1.2
)

# Average confidence line
avg_confidence = df["Confidence"].mean()

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

st.header("🏆 Highest Confidence Entity")

best = df.loc[df["Confidence"].idxmax()]

st.success(
    f"{best['Entity']} ({best['Type']}) - {best['Confidence']:.2f}%"
)

st.header("⚠ Lowest Confidence Entity")

worst = df.loc[df["Confidence"].idxmin()]

st.warning(
    f"{worst['Entity']} ({worst['Type']}) - {worst['Confidence']:.2f}%"
)

st.divider()

st.header("📝 Raw BioBERT Output")

st.json(entities)