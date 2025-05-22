
import streamlit as st
import os
from utils import summarize_brief, brainstorm_ideas, generate_dalle_image, extract_text_from_file

st.set_page_config(page_title="Creative AI Agent", layout="wide")
st.title("🤖 Creative AI Agent for Campaign Ideation")

uploaded_file = st.file_uploader("Upload a campaign brief (PDF or Word)", type=["pdf", "docx"])
if uploaded_file:
    with st.spinner("Extracting text from brief..."):
        brief_text = extract_text_from_file(uploaded_file)
        st.success("Text extracted successfully!")
        st.subheader("📄 Brief Summary")
        summary = summarize_brief(brief_text)
        st.write(summary)

        st.subheader("💡 Campaign Brainstorm")
        ideas = brainstorm_ideas(summary)
        st.write(ideas)

        st.subheader("🎨 Generate Visual Direction (Optional)")
        style = st.selectbox("Select Visual Style", ["Minimalist", "Cinematic", "Collage", "Futuristic", "Lifestyle", "Retro"])
        scene = st.text_input("Scene Type or Media (e.g. 'web banner', 'billboard', 'social post')")

        if st.button("Generate Visual"):
            dalle_prompt = f"A {style.lower()} {scene} concept for a campaign about: {summary}"
            with st.spinner("Creating visual concept..."):
                image_url = generate_dalle_image(dalle_prompt)
                st.image(image_url, caption=dalle_prompt)
