from pathlib import Path

from langchain_core.documents import Document

from Services.chunker.language_config import (
    get_language_from_extension,
    get_chunk_type
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

def extract_structural_chunks(node, doc_content, doc, language):

    chunks = []

    # We'll find the chunk-type
    chunk_type = get_chunk_type(language, node)

    if chunk_type is not None:
        chunks.extend(
            create_chunk_from_node(node, doc_content, doc, chunk_type)
        )

        return chunks

    for child in node.children:
        chunks.extend(extract_structural_chunks(child, doc_content, doc, node))

    return chunks

def create_chunk_from_node(node, doc_content, doc, chunk_type):

    # We'll start with starting point and ending point

    start_byte = node.start_byte
    end_byte = node.end_byte

    chunk_content = doc_content[start_byte:end_byte].decode("utf-8")

    start_line = node.start_point.row+1
    end_line = node.end_point.row+1

    metadata = doc.metadata.copy()

    metadata.update({
        "chunk_type": chunk_type,
        "start_line": start_line,
        "end_line": end_line,
    })


    return Document(
        page_content=chunk_content,
        metadata=metadata
    )

def fallback_chunk():
    return []
