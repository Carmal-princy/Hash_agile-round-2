import csv
import json
import requests

def indexData(collection_name, exclude_column):
    with open("Employee Sample Data 1.csv", "r") as file:
        reader = csv.DictReader(file)  # Use DictReader for easy access by column names
        for record in reader:
            record.pop(exclude_column, None)  # Exclude specified column
            
            # Send the record to Solr
            response = requests.post(f"http://localhost:8983/solr/{collection_name}/update?commit=true", json=[record])
            print(response.json())  # Print the response from Solr

# Call the function to index data while excluding the 'Phone' column
indexData('employee_data', 'Phone')
