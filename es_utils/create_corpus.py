import pandas as pd
from elasticsearch import Elasticsearch


es = Elasticsearch('localhost:9200')


def create_index(mapping: dict, index_name: str) -> None:
    es.indices.create(index=index_name)
    es.indices.put_mapping(index=index_name, body=mapping)


def insert_data(file_path: str, index_name: str) -> None:
    df = pd.read_json(file_path).fillna("")
    for _, row in df.iterrows():
        doc = row.to_dict()
        es.index(index=index_name, body=doc)  


if __name__ == "__main__":

    index_name = "song_txt_corpus"
    file_path = "../data/corpus.json"

    mapping = {
        "properties": {
            "artist": {"type": "text"},
            "song_name": {"type": "text"},
            "song_txt": {"type": "text"},
            "song_href": {"type": "text"},
            "song_id": {"type": "integer"},
            "top_similar": {"type": "integer"},
        }
    }

    create_index(mapping=mapping, index_name=index_name)
    insert_data(file_path=file_path, index_name=index_name)