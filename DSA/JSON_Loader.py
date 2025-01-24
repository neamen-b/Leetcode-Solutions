import json

def JSON_Loader (json_file_path):
    json_file = open(json_file_path, 'r')
    json_file_data = json.load(json_file)
    return json_file_data
z