# Insecure file upload pattern demo (scanner-only)

from pathlib import Path


def save_uploaded_file_unsafely(filename: str, content: bytes) -> Path:
    # DO NOT DO THIS in real code.
    # - no extension/content validation
    # - filename is trusted
    out = Path("public") / "uploads" / filename
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_bytes(content)
    return out
