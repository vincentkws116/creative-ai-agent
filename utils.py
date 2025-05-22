
import os
import fitz  # PyMuPDF
import docx
import openai

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def extract_text_from_file(uploaded_file):
    if uploaded_file.name.endswith(".pdf"):
        doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
        text = "".join([page.get_text() for page in doc])
        return text.strip()
    elif uploaded_file.name.endswith(".docx"):
        doc = docx.Document(uploaded_file)
        return "\n".join([para.text for para in doc.paragraphs])
    else:
        return ""

def summarize_brief(text):
    prompt = f"Summarize this campaign brief in a few key points:\n{text}"
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

def brainstorm_ideas(summary):
    prompt = f"Based on this brief summary, brainstorm campaign ideas with headlines, visual directions, and taglines:\n{summary}"
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.9
    )
    return response.choices[0].message.content.strip()

def generate_dalle_image(prompt):
    response = client.images.generate(
        prompt=prompt,
        n=1,
        size="1024x1024"
    )
    return response.data[0].url
