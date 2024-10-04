import requests

def createCollection(collection_name):
    # For standalone mode, use the create command directly
    url = f"http://localhost:8983/solr/admin/collections?action=CREATE&name={collection_name}&numShards=1&replicationFactor=1"
    response = requests.get(url)
    return response.json()

if __name__ == "__main__":
    v_nameCollection = 'employee_data'  # Use your desired collection name
    result = createCollection(v_nameCollection)
    print(result)
