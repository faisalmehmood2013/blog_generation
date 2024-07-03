import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import os

# Loads environment variables from a .env file.
load_dotenv()

# Set the environment variables
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
openai_base_url = os.getenv('OPENAI_URL')

def generateresponse(input_text, no_of_words, blog_style):
    # Initialize the OpenAI model
    llm = ChatOpenAI(openai_api_base=openai_base_url, temperature=0.5, max_tokens=500)

    # Initialize the prompt template
    template="""
        Act as a professional blog writer and write a blog on {input_text} for {blog_style} job profile 
        within {no_of_words} words.
            """
    
    prompt=PromptTemplate(input_variables=["blog_style","input_text",'no_of_words'],
                          template=template)

    # Generate the response
    response = llm.predict(prompt.format(input_text=input_text, no_of_words=no_of_words, blog_style=blog_style))

    return response

# Streamlit UI
st.set_page_config(page_title="Generate Blogs", page_icon='🤖', layout='centered', initial_sidebar_state='collapsed')
st.header("Generate Blogs")

input_text=st.text_input("Enter the Blog Topic")

no_of_words, blog_style = st.columns([5,5])

with no_of_words:
    no_of_words = st.text_input('Number of Words')
with blog_style:
    blog_style = st.selectbox("Select the Blog Style", ["Data Scientist", "Researchers", "Common People"], index=0)

submit=st.button("Generate")

if submit:
    st.write((generateresponse(input_text, no_of_words, blog_style)))


