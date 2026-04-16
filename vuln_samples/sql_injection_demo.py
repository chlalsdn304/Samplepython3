# SQL Injection pattern demo (scanner-only)


def build_unsafe_query(user_input: str) -> str:
    # DO NOT DO THIS in real code.
    return "SELECT * FROM users WHERE name = '" + user_input + "'"  # unsafe concatenation
