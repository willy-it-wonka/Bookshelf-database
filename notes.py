import json

id_start = 4
book_id_start = 22

with open('notes.json', 'r+') as file:
    data = json.load(file)
    
    # Update id and book_id.
    for index, note in enumerate(data):
        note['id'] = id_start + index
        note['book_id'] = book_id_start + index

    file.seek(0) # Move to the beginning of the file to overwrite it.
    json.dump(data, file, indent=2, ensure_ascii=False) # Save the updated data back to the file.
    file.truncate()
