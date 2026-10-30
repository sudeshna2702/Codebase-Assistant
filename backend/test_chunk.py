from pathlib import Path

from langchain_core.documents import Document

from Services.chunker.code_chunker import chunk_document


file_path = Path(r"C:\Test_AI\Greet.py")

content = file_path.read_text(encoding="utf-8")

doc = Document(
    page_content=content,
    metadata={
        "file_name": file_path.name,
        "relative_path": str(file_path),
        "extension": file_path.suffix,
    }
)

chunks = chunk_document(doc)

print(f"Number of chunks: {len(chunks)}")

for i, chunk in enumerate(chunks):
    print(f"\n{'=' * 60}")
    print(f"CHUNK {i + 1}")
    print(f"{'=' * 60}")

    print("Metadata:")
    print(chunk.metadata)

    print("\nContent:")
    print(chunk.page_content)