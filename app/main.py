from fastapi import FastAPI

app = FastAPI(title="IWIS Backend")

@app.get("/")
def read_root():
    return {"message": "Integrated Water Information System API is running"}