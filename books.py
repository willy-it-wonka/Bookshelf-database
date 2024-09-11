import json

starting_id = 22
new_user_id = 3
new_created_date = "2024-09-10"
new_modified_date = "2024-09-11"

# Update the date, keeping the time.
def update_date(full_date, new_date):
    return f"{new_date} {full_date.split(' ')[1]}"

with open('books.json', 'r+') as file:
    data = json.load(file)
    
    # Update id, user_id and date.
    for index, book in enumerate(data, start=starting_id):
        book['id'] = index
        book['user_id'] = new_user_id
        book['created_date'] = update_date(book['created_date'], new_created_date)
        book['last_modified_date'] = update_date(book['last_modified_date'], new_modified_date)

    file.seek(0) # Move to the beginning of the file to overwrite it.
    json.dump(data, file, indent=2, ensure_ascii=False) # Save the updated data back to the file.
    file.truncate()
