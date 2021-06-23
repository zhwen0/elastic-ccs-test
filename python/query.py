from elasticsearch import Elasticsearch 

es = Elasticsearch(
    ['node1']
    )

res = es.search(index='test,es2:test', body=
         {
           'query': {
              'match_all': {}
           }
         }
      )

# Print the result of the query.
print('')
print('----------')
for hit in res['hits']['hits']: 
    print('_id: %(_id)s' % hit)
    print('index: %(_index)s' % hit)
    print(hit['_source'])
    print('----------')

print('')
