def getDepFacet(collection_name):
    url = f"http://localhost:8983/solr/{collection_name}/select?q=*:*&facet=true&facet.field=Department"
    response = requests.get(url)
    return response.json()
department_facets = getDepFacet('employee_data')
print(department_facets)
