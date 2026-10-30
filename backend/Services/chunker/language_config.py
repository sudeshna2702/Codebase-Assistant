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

CHUNK_NODE_TYPES = {
    "python": {
        "class_definition": "class",
        "function_definition": "function",
    },

    "cpp": {
        "class_specifier": "class",
        "function_definition": "function",
    },

    "java": {
        "class_declaration": "class",
        "method_declaration": "method",
    },

    "javascript": {
        "class_declaration": "class",
        "function_declaration": "function",
        "method_definition": "method",
        "arrow_function": "function",
    },

    "typescript": {
        "class_declaration": "class",
        "function_declaration": "function",
        "method_definition": "method",
        "arrow_function": "function",
    },

    "tsx": {
        "class_declaration": "class",
        "function_declaration": "function",
        "method_definition": "method",
        "arrow_function": "function",
    },
}



def get_language_from_extension(extension : str) -> str:
    # to get the language
    language = EXTENSION_LANGUAGE_MAPPING.get(extension, "unknown")
    return language

def get_chunk_type(language : str, node_type: str) -> str:
    # To get the language specific block
    language_block = CHUNK_NODE_TYPES.get(language, {})

    return language_block.get(node_type)