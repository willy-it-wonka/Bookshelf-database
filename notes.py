import json

id_start = 4
book_id_start = 22

with open('notes.json', 'r+') as file:
    data = json.load(file)
    
    # Update id and book_id. And replace "\n" with "\\n" in the 'content' field.
    for index, note in enumerate(data):
        note['id'] = id_start + index
        note['book_id'] = book_id_start + index
        # Comment out the following 2 lines if you will import the JSON file and not using it in a SQL script.
        if 'content' in note:
            note['content'] = note['content'].replace('\n', '\\n')

    file.seek(0)
    json.dump(data, file, indent=2, ensure_ascii=False)
    file.truncate()
