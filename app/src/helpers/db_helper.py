from fastapi.encoders import jsonable_encoder
from elasticsearch import Elasticsearch, NotFoundError
from elasticsearch.helpers import streaming_bulk
import json

es = Elasticsearch("localhost")

def get_health():
    return es.cluster.health()

def read_json():
    with open("C:\Chinmaya\\fastapi-elasticsearch\\app\src\data\\trades.json") as json_file:
        json_docs = json.load(json_file)
    for trade in json_docs ["data"]["trades"][:2]:
        yield trade

def ingest():
    if not (es.indices.exists(index="trades")):
        es.indices.create(index="trades")

    for _ in streaming_bulk(
        client=es, index="trades", actions=read_json()
    ):
        pass

    return {"status":"ok"}

def search(query):
    return es.search(
        index="trades", body={"query":{"multi_match":{"query":query}}}
    ) 

def delete_id(id):
    try:
        return es.delete(index="trades", id=id)
    except NotFoundError as e:
        return e.info, 404

def delete():
    return es.delete_by_query(index="trades", body={"query": {"match_all": {}}})