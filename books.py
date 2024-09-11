import json

# Read the JSON file.
with open('books.json', 'r+') as file:
    data = json.load(file)
    
    # Update id, user_id and date.
    for index, item in enumerate(data, start=22):
        item['id'] = index
        item['user_id'] = 3
        # Update only the date part of created_date and last_modified_date.
        item['created_date'] = "2024-09-10" + ' ' + item['created_date'].split(' ')[1]
        item['last_modified_date'] = "2024-09-11" + ' ' + item['last_modified_date'].split(' ')[1]
        
    file.seek(0) # Move to the beginning of the file to overwrite it.
    json.dump(data, file, indent=2, ensure_ascii=False) # Save the updated data back to the file.
    file.truncate()
