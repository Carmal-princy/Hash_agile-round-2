import requests

def createCollection(collection_name):
    url = f"http://localhost:8983/solr/admin/collections?action=CREATE&name={collection_name}&numShards=1&replicationFactor=1"
    response = requests.get(url)
    return response.json()
department_facets = getDepFacet('employee_data')
print(department_facets)