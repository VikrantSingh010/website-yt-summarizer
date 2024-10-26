import validators
import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain.chains.summarize import load_summarize_chain
from langchain_community.document_loaders import YoutubeLoader, UnstructuredURLLoader

# Set up page configuration
st.set_page_config(page_title="Langchain: Summarize Text from YT or Website", page_icon="")
st.title("Langchain: Summarize Text from YT or Website")
st.subheader("Summarize URL")

# Sidebar for API key
with st.sidebar:
    groq_api_key = st.text_input("Groq API Key", value="", type="password")

# URL input field
generic_url = st.text_input("URL", label_visibility="collapsed")

# Initialize language model
llm = ChatGroq(model="Gemma-7b-It", groq_api_key=groq_api_key)

# Prompt template for summary
prompt_template = """
Provide a summary of the following content in about 300 words:
Content: {text}
"""
prompt = PromptTemplate(template=prompt_template, input_variables=["text"])

# Button to trigger summarization
if st.button("Summarize the content from YouTube or Website"):
    if not groq_api_key.strip() or not generic_url.strip():  # Use 'generic_url' instead of 'url'
        st.error("Please provide correct information.")
    elif not validators.url(generic_url):
        st.error("Please enter a valid URL")
    else:
        try:
            with st.spinner("Waiting..."):
                # Choose loader based on URL type
                if "youtube.com" in generic_url:
                    loader = YoutubeLoader.from_youtube_url(generic_url, add_video_info=True)
                else:
                    loader = UnstructuredURLLoader(
                        urls=[generic_url],
                        ssl_verify=False,
                        headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"}
                    )

                # Load documents and summarize
                docs = loader.load()
                chain = load_summarize_chain(llm, chain_type="stuff", prompt=prompt)
                output_summary = chain.run(docs)
                st.success(output_summary)
        except Exception as e:
            st.error(f"Exception: {e}")
