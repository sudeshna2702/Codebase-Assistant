from tree_sitter import Parser
from tree_sitter_language_pack import get_parser


def get_language_parser(language: str) -> Parser | None:
    try:
        return get_parser(language)
    except Exception:
        return None