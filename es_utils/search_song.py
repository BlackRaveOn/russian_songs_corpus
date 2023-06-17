from elasticsearch import Elasticsearch

es = Elasticsearch('localhost:9200')

def search(match_list: list, size=15, index_name="song_txt_corpus", query_type="words") -> dict:
    processed = []

    if query_type == "words":
        query = {"query": {"bool": {"must": match_list}}, "size": size}
    elif query_type == "ids":
        query = {"query": {"terms": {"song_id": match_list}}, "size": size}
    else:
        raise ValueError("Incorrect query type!!! use {words, ids}")

    results = es.search(index=index_name, body=query)
    for nest in results['hits']['hits']:
        nested_data = nest["_source"] 
        nested_data["search_score"] = round(nest["_score"], 3)
        processed.append(nested_data)
    return processed