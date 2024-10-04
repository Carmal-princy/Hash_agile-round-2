def getEmpCount(collection_name):
    url = f"http://localhost:8983/solr/{collection_name}/select?q=*:*&rows=0"
    response = requests.get(url)
    return response.json()['response']['numFound']
