from fastapi import FastAPI
from responseStructures.response_structure import testResponse, folderRequest
from Services.file_extractor import extract_file
from langchain_core.documents import Document
from Services.doc_loader import load_documents
from pathlib import Path

app = FastAPI()

@app.get("/")
def startMessage():
    print ("Server is running!!!")

    return {
        "message": "Server is running!"
    }

# Defining the structure It gonna get as response is better in terms of main.py 
@app.post("/test")
def get_communication_message(req : testResponse):
    text = req.message
    print("This is the message I got from extension: "+text)

    return {
        "response":"Server got the data!!"
    }


#For getting the Folder selected
@app.post("/folder")
def process_folder_data(req : folderRequest):
    # print ("received folder: "+req.folder_path)

    # To extract the files from the folder
    files = extract_file(req.folder_path)

    #testing
    print( *files, sep = "\n")

    # document loading
    documents = load_documents(files, Path(req.folder_path))

    print("\n========== DOCUMENTS ==========")

    for document in documents[:5]:
        print("\n------------------------------")
        print("Metadata:")
        print(document.metadata)

        print("\nContent preview:")
        print(document.page_content[:200])

    print("\nTotal files:", len(files))
    print("Total documents:", len(documents))

    return {
        "response":"Server got the folder!!"
    }


