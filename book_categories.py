import json

previous_book_id = None
new_book_id = 22

with open('book_categories.json', 'r+') as file:
    data = json.load(file)

    # Update book_id.
    for category in data:
        if category['book_id'] != previous_book_id:
            previous_book_id = category['book_id']
            new_book_id += 1
        category['book_id'] = new_book_id - 1 # Keep the same book_id for the same book.

    file.seek(0) # Move to the beginning of the file to overwrite it.
    json.dump(data, file, indent=2) # Save the updated data back to the file.
    file.truncate()
