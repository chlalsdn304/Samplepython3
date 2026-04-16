# Directory traversal pattern demo (scanner-only)

from pathlib import Path


def read_file_unsafely(user_path: str) -> bytes:
    # DO NOT DO THIS in real code.
    # user_path might be "../../etc/passwd" etc.
    return Path(user_path).read_bytes()
