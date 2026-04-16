# XSS pattern demo (scanner-only)

from fastapi.responses import HTMLResponse


def render_unsafe_html(q: str) -> HTMLResponse:
    # DO NOT DO THIS in real code.
    html = f"<h1>Hello {q}</h1>"  # unescaped user input
    return HTMLResponse(content=html)
