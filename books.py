import json

# Read the JSON file.
with open('books.json', 'r+') as file:
    data = json.load(file)
    
    # Update id and user_id.
    for index, item in enumerate(data, start=22):
        item['id'] = index
        item['user_id'] = 3
        
    file.seek(0) # Move to the beginning of the file to overwrite it.
    json.dump(data, file, indent=2, ensure_ascii=False) # Save the updated data back to the file.
    file.truncate()
