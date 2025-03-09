from fastapi.fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, this is a test of the EC2 instance!"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}