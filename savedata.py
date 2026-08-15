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


    # 800/150 split chunks
    doc_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 800,
        chunk_overlap = 150,
        length_function = len
    )

    plotted_chunks = doc_splitter.split_documents(uni_pdf_docs)
    print(f" Searchable points: {len(plotted_chunks)}")

    # Vectorization of processed chunks (MiniLM)
    print("Vectorizing chunks using HuggingFace...")
    vector_convertor = HuggingFaceEmbeddings(model_name= "all-MiniLM-L6-v2")

    # Connect and store in vector database
    db_connection = lancedb.connect(DB_DIRECTORY)

    # Clear table avoid duplicates
    if TABLE_NAME in db_connection.table_names():
        print(f"Clearing current table: {TABLE_NAME}")
        db_connection.drop_table(TABLE_NAME)

    # Store vecorized chunks in LanceDB
    LanceDB.from_documents(
        documents = plotted_chunks,
        embedding = vector_convertor,
        connection = db_connection,
        table_name = TABLE_NAME
    )

    print(f"\n Success! Vector base located at: {DB_DIRECTORY} [{TABLE_NAME}]")
    
if __name__ == "__main__":
    main()