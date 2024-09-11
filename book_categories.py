import json

# Read the JSON file.
with open('book_categories.json', 'r+') as file:
    data = json.load(file)

    # Update book_id.
    current_book_id = None
    new_id = 22
    for item in data:
        if item['book_id'] != current_book_id:
            current_book_id = item['book_id']
            new_id += 1
        item['book_id'] = new_id - 1 # Keep the same book_id for the same book.

    file.seek(0) # Move to the beginning of the file to overwrite it.
    json.dump(data, file, indent=2) # Save the updated data back to the file.
    file.truncate()
