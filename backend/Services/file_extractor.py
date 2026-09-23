from pathlib import Path
import os
from Services.file_filter import is_supported_file, load_dotcodebaseignore , is_codebase_assistant_ignored


# It is the simple version, but we have to do make sure to not extract all the files
# files like node_modules, Scripts, .env etc all those file which we usallly put in .gitignore file.

# Ignored Directories
IGNORED_DIRS = {
    # Version control
    ".git",
    ".svn",
    ".hg",

    # Python
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    ".venv",
    "venv",
    "env",

    # JavaScript / Node
    "node_modules",

    # Java / general build output
    "target",
    "build",
    "dist",

    # IDE
    ".idea",
    ".vscode",

    # Testing / coverage
    "coverage",
}

def extract_file(folder_path : str):

    files = []

    ignored_patterns = load_dotcodebaseignore(folder_path)

    if len(ignored_patterns) != 0:
        print("I have received .codebasignore. ")

    for root, dirs, filenames in os.walk(folder_path):

        # Remove ignored directories from traversal
        dirs[:] = [
            directory
            for directory in dirs
            if directory not in IGNORED_DIRS
        ]

        for filename in filenames:

            file_path = Path(root) / filename


            if is_supported_file(file_path) and not is_codebase_assistant_ignored(file_path, folder_path, ignored_patterns) :
                files.append(file_path)

    return files