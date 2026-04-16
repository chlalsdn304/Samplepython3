from fastapi import FastAPI

app = FastAPI(title="fastapi-sample")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/")
def root():
    return {"message": "hello"}
