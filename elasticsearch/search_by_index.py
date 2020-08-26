from elasticsearch import Elasticsearch

es = Elasticsearch('http://localhost:9200')
es.index(index='my_index', id=1, body={'text': 'this is a test'})
es.index(index='my_index', id=2, body={'text': 'a second test'})
index_values = es.search(index='my_index', body={'query': {'match': {'text': 'this test'}}})
print(index_values)