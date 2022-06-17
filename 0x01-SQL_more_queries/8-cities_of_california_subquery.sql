-- this script list all the cities of CALI found in the server
SELECT id, name
FROM cities
WHERE state_id IN (
    SELECT id
    FROM states 
    WHERE name = 'California'
)
ORDER BY id ASC;