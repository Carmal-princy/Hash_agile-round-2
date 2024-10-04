def searchByColumn(collection_name, column_name, column_value):
    url = f"http://localhost:8983/solr/{collection_name}/select?q={column_name}:{column_value}"
    response = requests.get(url)
    return response.json()
