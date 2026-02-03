from fastapi import FastAPI
import socket

app = FastAPI()

hostname = socket.gethostname()
request_count = 0


@app.get("/")
def root():
    global request_count
    request_count += 1

    return {
        "message":"Hello from backend",
        "hostname": hostname,
        "request_count":request_count
    }

@app.get("/health")
def health():
    return {"status":"ok"}

