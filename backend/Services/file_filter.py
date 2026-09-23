from pathlib import Path

SUPPORTED_EXTENSIONS = {
    # Python
    ".py",

    # JavaScript / TypeScript / React JS
    ".js",
    ".jsx",
    ".mjs",
    ".cjs",
    ".ts",
    ".tsx",

    # Java
    ".java",

    # PHP
    ".php",

    # C / C++
    ".c",
    ".h",
    ".cpp",
    ".hpp",

    # C#
    ".cs",

    # Go
    ".go",

    # Rust
    ".rs",

    # Kotlin
    ".kt",
    ".kts",

    # Swift
    ".swift",

    # Ruby
    ".rb",

    # Web
    ".html",
    ".css",
    ".scss",

    # Shell
    ".sh",

    #Readme
    ".md",

    #package.json
    ".json"
}

def is_supported_file(file_path):
    return file_path.suffix.lower() in SUPPORTED_EXTENSIONS


def load_dotcodebaseignore(folder_path : str):
    ignore_file = Path(folder_path) / ".codebaseignore"

    if not ignore_file.exists():
        return []

    with open(ignore_file, "r", encoding="utf-8") as file:
        patterns = []

        for line in file:
            line = line.strip()

            # Ignore empty lines
            if not line:
                continue

            # Ignore comments
            if line.startswith("#"):
                continue

            patterns.append(line)

    return patterns

def is_codebase_assistant_ignored(file_path : Path , root_path : Path, patterns : list[str]):
    # Fetching the relative path by subtracting the root_path from actual file_path
    relative_path = file_path.relative_to(root_path)

    for pattern in patterns:
        if relative_path.match(pattern) : 
            return True

    return False

    
