from pathlib import Path

from langchain_core.documents import Document

from Services.chunker.language_config import (
    get_language_from_extension,
)

from Services.chunker.parser_manager import (
    get_language_parser,
)


def chunk_document(doc: Document) -> list[Document]:
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

    # Actual parsing will happen here
    chunks = extract_structural_chunks(
        tree.root_node,
        source,
        doc,
        language,
    )

    if not chunks:
        return fallback_chunk(doc)

    print_tree(tree.root_node,0)

    return [doc]

# For testing purpose
def print_tree(node, depth=0):
    indent = "  " * depth

    print(
        f"{indent}{node.type} "
        f"[{node.start_point.row + 1}:"
        f"{node.end_point.row + 1}]"
    )

    for child in node.children:
        print_tree(child, depth + 1)

def chunk_all_documents(docs : list[Document]) -> list[Document]:

    chunks = []
    for document in docs:
        chunks.extend(chunk_document(document))

    return chunks