import os
import sys

# University Knowledge Base
DOCUMENT_FOLDER = "data/pdfs"
DB_DIRECTORY = "vectorstore"
TABLE_NAME = "ontario_admissions"

def main():
    # Checking if directory exists
    if not os.path.exists(DB_DIRECTORY):
        print(f"Directory '{DB_DIRECTORY}' does not exist.")
        sys.exit(1)



if __name__ == "__main__":
    main()