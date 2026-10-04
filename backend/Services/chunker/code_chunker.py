from pathlib import Path

from langchain_core.documents import Document

from Services.chunker.language_config import (
    get_language_from_extension,
)

from Services.chunker.parser_manager import (
    get_language_parser,
)


def chunk_documents(doc: Document) -> list[Document]:
    # We will fetch the document
    extension = doc.metadata.get("extension")

    # We will get the language from document
    language = get_language_from_extension(extension)
    if language is None:
        # Here the fallback strategy will come
        return [doc]

    # We will get the parser
    parser = get_language_parser(language)

    if parser is None:
        return [doc]

    source = doc.page_content.encode("utf-8")
    tree = parser.parse(source)