import streamlit as st
import pickle

st.set_page_config(page_title="Academic NLP Classification Prototype")

st.title("Academic NLP Classification Prototype")
st.warning(
    "This is a coursework prototype. Its labels are not clinically validated and "
    "the output must not be interpreted as a mental-health diagnosis or screening result."
)

model = pickle.load(open("models/mental_health_model.pkl", "rb"))
vectorizer = pickle.load(open("models/tfidf_vectorizer.pkl", "rb"))

user_input = st.text_area("Enter text")

if st.button("Predict"):
    if not user_input.strip():
        st.info("Please enter some text first.")
    else:
        text_vector = vectorizer.transform([user_input])
        prediction = model.predict(text_vector)
        st.success(f"Predicted class: {prediction[0]}")
        st.caption(
            "This class reflects the labels used in the original academic dataset/model only."
        )
