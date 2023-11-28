import streamlit as st
from langchain.document_loaders.parsers.pdf import PyPDFParser

def main():
    st.title("Upload your PDF")
    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        print(type(bytes_data))
        data = PyPDFParser.parse(self=PyPDFParser, blob=bytes_data)
        print(data)

if __name__ == "__main__":
    main()
