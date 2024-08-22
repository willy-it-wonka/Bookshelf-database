import json

# Read the JSON file.
with open('notes.json', 'r+') as file:
    data = json.load(file)
    
    # Update id and book_id.
    for index, item in enumerate(data, start=4):
        item['id'] = index
        item['book_id'] = index

    file.seek(0) # Move to the beginning of the file to overwrite it.
    json.dump(data, file, indent=2, ensure_ascii=False) # Save the updated data back to the file.
