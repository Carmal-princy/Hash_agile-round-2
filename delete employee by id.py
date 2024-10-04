def delEmpById(collection_name, employee_id):
    url = f"http://localhost:8983/solr/{collection_name}/update?commit=true"
    data = [{"delete": {"id": employee_id}}]
    response = requests.post(url, json=data)
    return response.json()
