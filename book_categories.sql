USE ebdb; -- Rename it to suit your database schema.

SET @json = '
-- Here paste code from book_categories.json
';

INSERT INTO book_categories (book_id, category)
SELECT 
    JSON_UNQUOTE(JSON_EXTRACT(json_array.value, '$.book_id')) AS book_id,
    JSON_UNQUOTE(JSON_EXTRACT(json_array.value, '$.category')) AS category
FROM JSON_TABLE(@json, '$[*]' COLUMNS (value JSON PATH '$')) AS json_array;
