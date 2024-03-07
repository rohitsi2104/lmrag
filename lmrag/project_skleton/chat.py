from langchain_community.llms import OpenAI
from dotenv import load_dotenv
import streamlit as st
import os

load_dotenv()

def get_openai_response(question):
    llm = OpenAI(openai_api_key=os.getenv('OPENAI_API_KEY'),  temperature=0.6)
    try:
        response = llm(question)
        return response
    except Exception as e:
        st.error(f"Error from OpenAI API: {e}")
        return None

st.set_page_config(page_title="Q&A Application")
st.header('Welcome to your personal AI you can promt below. ')
input_text = st.text_input("Input: ", key="Input")
response = get_openai_response(input_text)

submit = st.button('Generate')

if submit:
    if response is not None:
        st.subheader('Response is')
        st.write(response)

