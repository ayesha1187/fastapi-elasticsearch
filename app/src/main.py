from fastapi import FastAPI

from src.helpers import api_helper


app = FastAPI()

@app.get("/")
def index():
    return api_helper.get_health()

@app.get("/ingest")
def ingest():
    return api_helper.ingest()

@app.get("/search/{query}")
def search(query):
    return api_helper.search(query)

@app.get("/delete/{id}")
def delete_id(id):
    return api_helper.delete_id(id)

@app.get("/delete")
def delete():
    return api_helper.delete()
