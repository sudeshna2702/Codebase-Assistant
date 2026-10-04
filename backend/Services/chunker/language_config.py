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


def get_language_from_extension(extension : str) -> str:
    # to get the language
    language = EXTENSION_LANGUAGE_MAPPING.get(extension, "unknown")
    return language
