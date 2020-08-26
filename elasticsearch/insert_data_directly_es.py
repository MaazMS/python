from elasticsearch import Elasticsearch

es = Elasticsearch()

doc1 = {'city': 'pune' , 'country' : 'india'}
doc2 = {'city': 'makka', 'country' : 'Saudi Arabia' }

cities_details_india = es.index(index="cities", body=doc1 , id=1)
cities_details_saudi = es.index(index="cities", body=doc2 , id=2)

cities_details_india =  es.get(index="cities", id=1)
cities_details_saudi =  es.get(index="cities", id=2)

print(cities_details_india['_source'])
print(cities_details_saudi['_source'])

