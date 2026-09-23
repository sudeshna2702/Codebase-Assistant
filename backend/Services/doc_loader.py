from pathlib import Path
from langchain_core.documents import Document

EXTENSION_LANGUAGE_MAPPING = {
    # Python
    ".py": "python",

    # JavaScript / TypeScript / React
    ".js": "javascript",
    ".jsx": "javascript",
    ".mjs": "javascript",
    ".cjs": "javascript",
    ".ts": "typescript",
    ".tsx": "typescript",

    # Java
    ".java": "java",

    # PHP
    ".php": "php",

    # C / C++
    ".c": "c",
    ".h": "c/cpp",
    ".cpp": "cpp",
    ".hpp": "cpp",

    # C#
    ".cs": "csharp",

    # Go
    ".go": "go",

    # Rust
    ".rs": "rust",

    # Kotlin
    ".kt": "kotlin",
    ".kts": "kotlin",

    # Swift
    ".swift": "swift",

    # Ruby
    ".rb": "ruby",

    # Web
    ".html": "html",
    ".css": "css",
    ".scss": "scss",

    # Shell
    ".sh": "shell",

    # Markdown
    ".md": "markdown",

    # JSON
    ".json": "json",
}


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
    language = EXTENSION_LANGUAGE_MAPPING.get(file_path.suffix.lower(), "unknown")

    return  {
        "file_name": file_path.name,
        "root_path": str(root_path),
        "relative_path": str(file_path.relative_to(root_path)),
        "extension": file_path.suffix,
        "language": language,
        "updated_on": file_stat.st_mtime
    }
