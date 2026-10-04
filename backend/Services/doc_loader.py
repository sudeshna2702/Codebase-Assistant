from pathlib import Path
from langchain_core.documents import Document
from Services.chunker.language_config import get_language_from_extension


def load_documents(file_paths : list[Path], root_path: Path) -> list[Document]:

    documents = []

    for file_path in file_paths:
        document = load_file(file_path, root_path)

        if document is not None:
            documents.append(document)

    return documents


def load_file(file_path : Path, root_path : Path) -> Document|None:
    try: 
        content = file_path.read_text(
            encoding="utf-8",
            errors="ignore"
        )

        file_metadata = get_file_metadata(file_path, root_path)

        return Document(
            page_content = content,
            metadata = file_metadata
        )
    except Exception as e:
        print(f"Error while loading file {file_path} : {e}")
        return None

def get_file_metadata(file_path : Path, root_path: Path) -> dict:
    file_stat = file_path.stat()
    language = get_language_from_extension(file_path.suffix.lower())

    return  {
        "file_name": file_path.name,
        "root_path": str(root_path),
        "relative_path": str(file_path.relative_to(root_path)),
        "extension": file_path.suffix,
        "language": language,
        "updated_on": file_stat.st_mtime
    }
