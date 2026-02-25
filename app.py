import streamlit as st
from src.pdf_reader import extract_pdf_text
from src.cleaner import normalize_text
from src.sequence_engine import build_lookup
from src.predictor import get_prediction

st.set_page_config(page_title="Next Word Predictor from Raw Data", layout="centered")
st.title("📄 Next Word Predictor from Raw Data")

PDF_PATH = "data\Child-Development-Guide.pdf" # ✅ tumhara exact file name

if "history" not in st.session_state:
    st.session_state.history = []

raw_text = extract_pdf_text(PDF_PATH)
clean_text = normalize_text(raw_text)
words = clean_text.split()
lookup = build_lookup(words)

st.success("✅ PDF loaded successfully!")

user_sentence = st.text_input("Enter minimum 10 words from the PDF")

if st.button("Predict Next 5 Words"):
    if len(user_sentence.split()) < 10:
        st.warning("⚠ Please enter at least 10 words.")
    else:
        output = get_prediction(user_sentence, lookup)
        st.session_state.history.append({
            "input": user_sentence,
            "output": output
        })

if st.session_state.history:
    st.subheader("📜 Prediction History")
    for i, item in enumerate(reversed(st.session_state.history), 1):
        st.markdown(f"**{i}. Input:** {item['input']}")
        st.markdown(f"➡ **Prediction:** {item['output']}")
        st.markdown("---")
