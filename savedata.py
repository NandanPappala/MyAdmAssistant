import os
import sys
import lancedb
#import PyMuPDFLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import LanceDB
from langchain_core.documents import Document



# University Knowledge Base
DOCUMENT_FOLDER = "data/pdfs"
DB_DIRECTORY = "vector_database"
TABLE_NAME = "ontario_admissions"

def main():
    # Checking if directory exists
    if not os.path.exists(DB_DIRECTORY):
        print(f"Directory '{DB_DIRECTORY}' does not exist.")
        sys.exit(1)

    print("Analyzing university criteria docs...")
    uni_pdf_docs = []

    #loop through and extract text from each PDF file in the DOCUMENT_FOLDER
    for file in os.listdir(DOCUMENT_FOLDER):
        if file.endswith(".pdf"):
            file_path = os.path.join(DOCUMENT_FOLDER, file)
            print(f"Processing file: {file}")
            data_processor = PyMuPDFLoader(file_path)
            uni_pdf_docs.extend(data_processor.load())

if __name__ == "__main__":
    main()