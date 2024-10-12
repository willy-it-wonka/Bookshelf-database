USE ebdb; -- Rename it to suit your database schema.

SET @json = '
-- Here paste code from notes.json
';

INSERT INTO notes (id, content, book_id)
SELECT 
    JSON_UNQUOTE(JSON_EXTRACT(json.value, '$.id')) AS id,
    JSON_UNQUOTE(JSON_EXTRACT(json.value, '$.content')) AS content,
    JSON_UNQUOTE(JSON_EXTRACT(json.value, '$.book_id')) AS book_id
FROM JSON_TABLE(@json, '$[*]' COLUMNS (value JSON PATH '$')) AS json;
