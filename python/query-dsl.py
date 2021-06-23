from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search
from elasticsearch.connection import create_ssl_context

es = Elasticsearch(
    ['node1']
    )

s = Search(using=es, index='test,es2:test')

response = s.execute()

# Print the result of the query.
print('')
print('----------')          
for hit in response:
  print('_id: %(id)s' % hit.meta)
  print('index: %(index)s' % hit.meta)
  print('name: %(name)s' % hit)
  print('----------')          

print('')
