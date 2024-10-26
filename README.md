
Langchain: Summarize Text from YouTube or Website

A Streamlit app that allows you to summarize content from YouTube videos or websites. This tool utilizes the Langchain library and Groq's language model, providing concise summaries with ease. Just input a valid URL, and the app will retrieve and summarize the content.
Features

    Supports YouTube and web URLs: Automatically detects YouTube URLs and extracts transcript data.
    Customizable summary: Summarizes content in approximately 300 words.
    User-friendly: Built with Streamlit for an interactive experience.

Installation
1. Clone the repository
    git clone <repository_url>
    cd <repository_directory>

2.Set up a virtual environment:
   python3 -m venv env
   source env/bin/activate

3. Install dependencies

Install all required libraries with:

     pip install -r requirements.txt
Contents of requirements.txt

    chromadb
    sentence_transformers
    langchain_huggingface
    faiss_cpu
    langchain_chroma
    duckdb
    pandas
    openai
    langchain-groq
    duckduckgo-search
    pymupdf
    arxiv
    wikipedia
    validators==0.28.1
    youtube_transcript_api
    langchain_community
    pytube
4. Set up API keys

    Obtain your Groq API key for language model usage.
    In the app's sidebar, input your Groq API key to enable functionality.

Usage

    Run the application:
          streamlit run app.py

         Input a valid URL in the main text field (YouTube or any other website).
    Click "Summarize the content from YouTube or Website" to generate the summary.
    The app will display a summary in approximately 300 words.

File Structure

    app.py: Main application script.
    requirements.txt: List of dependencies.

Troubleshooting

If you encounter issues with specific URLs, ensure they are publicly accessible. For any other issues, check the Streamlit console for error messages.          


