from SPARQLWrapper import SPARQLWrapper, JSON
from cmem.cmempy.dp.proxy.sparql import get_query_api_endpoint
from cmem.cmempy.api import get_access_token

SPARQL_QUERY = """
PREFIX  rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX  rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT  *
WHERE
  { ?sub  rdfs:label  ?obj }
LIMIT   10
    """
# Get the CO sparql endpoint
uri = get_query_api_endpoint().format('default')

# initialize sparqlwrapper
sparql = SPARQLWrapper(uri)
#add authentication
sparql.addCustomHttpHeader("Authorization", f"Bearer {get_access_token()}")

sparql.setReturnFormat(JSON)
sparql.setQuery(SPARQL_QUERY)

try:
    ret = sparql.queryAndConvert()

    for r in ret["results"]["bindings"]:
        print(r)
except Exception as e:
    print(e)