from src.helpers import db_helper

def ingest():
    return db_helper.ingest()

def get_health():
    return db_helper.get_health()

def search(query):
    return db_helper.search(query)

def delete_id(id):
    return db_helper.delete_id(id)

def delete():
    return db_helper.delete()