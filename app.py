import streamlit as st
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from utils import extract_text_from_pdf
from prompts import get_prompt_template

load_dotenv()

st.set_page_config(page_title="AI Resume Optimizer", page_icon="🚀", layout="wide")

with st.sidebar:
    st.header("⚙️ Configuration")
    st.info("Powered by Groq Llama3")

    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        st.error("API Key missing in .env")
        st.stop()

st.title("🚀 AI-Powered Resume Optimizer")

col1, col2 = st.columns(2)

with col1:
    uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

with col2:
    job_description = st.text_area("Paste Job Description", height=300)

if st.button("Analyze & Optimize", type="primary"):
    if not uploaded_file or not job_description:
        st.warning("Upload a resume and enter job description.")
    else:
        with st.spinner("Processing..."):

            resume_text = extract_text_from_pdf(uploaded_file)

            if len(resume_text) < 50:
                st.error("Unable to extract text. PDF may be scanned.")
                st.stop()

            llm = ChatGroq(
                temperature=0.0,
                groq_api_key=api_key,
                model_name="llama-3.1-8b-instant"
            )

            prompt = get_prompt_template()
            parser = StrOutputParser()
            chain = prompt | llm | parser

            response = chain.invoke({
                "job_description": job_description,
                "resume_text": resume_text
            })

            st.success("Done!")
            st.markdown(response)
