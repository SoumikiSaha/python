import json

def read_json_file(filepath):
    with open(filepath, 'r') as file:
        data = json.load(file)
    return data

def extract_categories(data, parent_key=""):
    categories = {}
    for key, value in data.items():
        if "blocks" in value and value["blocks"]:
            subcategories = {}
            for block in value["blocks"]:
                block_id = block["blockId"]
                if block_id in data:
                    subcategories.update(extract_categories({block_id: data[block_id]}, parent_key=key))
            categories[key] = subcategories
        else:
            categories[key] = None

    return categories

file_path = r"D:\Code_Repo\Python\niq\categories.json"
data = read_json_file(file_path)

categories_structure = extract_categories(data)

print(json.dumps(categories_structure, indent=4))
