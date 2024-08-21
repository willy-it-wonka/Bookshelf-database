USE ebdb; -- Rename it to suit your database schema.

SET @json = '
-- Here paste code from books.json
';

INSERT INTO books (id, author, created_date, last_modified_date, link_to_cover, status, title, user_id)
SELECT 
    JSON_UNQUOTE(JSON_EXTRACT(json.value, '$.id')) AS id,
    JSON_UNQUOTE(JSON_EXTRACT(json.value, '$.author')) AS author,
    JSON_UNQUOTE(JSON_EXTRACT(json.value, '$.created_date')) AS created_date,
    JSON_UNQUOTE(JSON_EXTRACT(json.value, '$.last_modified_date')) AS last_modified_date,
    JSON_UNQUOTE(JSON_EXTRACT(json.value, '$.link_to_cover')) AS link_to_cover,
    JSON_UNQUOTE(JSON_EXTRACT(json.value, '$.status')) AS status,
    JSON_UNQUOTE(JSON_EXTRACT(json.value, '$.title')) AS title,
    JSON_UNQUOTE(JSON_EXTRACT(json.value, '$.user_id')) AS user_id
FROM JSON_TABLE(@json, '$[*]' COLUMNS (value JSON PATH '$')) AS json;
