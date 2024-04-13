from fastapi import FastAPI

app = FastAPI(
    title="First FastAPI APP",
    version="1.0",
    servers=[
        {
            "url":"https://0.0.0.0:8080",
            "description": "My Server"
        }
    ]
)

@app.get('/')
def read_root():
    return {"Hey":"Im a Hamza"}

@app.get("/item/")
def get_root():
    return {"Hello,": "I love Coding"}