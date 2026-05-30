from fastapi import FastAPI

from cmd.healthcheck import run_healthcheck

app = FastAPI()


@app.get("/")
def root():

    return {
        "service": "gpu-healthcheck"
    }


@app.get("/health")
def health():

    return run_healthcheck()


@app.get("/cluster")
def cluster():

    return run_healthcheck()["score"]