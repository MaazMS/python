from elasticsearch import Elasticsearch
es = Elasticsearch()
es.indices.create(index="about_me", ignore=400)

"""  Run program 
>>>es.indices.exists(index="about_me")
True
>>>es.indices.delete(index="about_me")
{'acknowledged': True}
>>>es.indices.exists(index="about_me")
False
"""


