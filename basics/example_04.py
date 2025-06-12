"""Example 04: file I/O"""

from pathlib import Path

def write_and_read(path: Path, text: str) -> str:
    """Write text to path and read it back."""
    path.write_text(text)
    return path.read_text()
