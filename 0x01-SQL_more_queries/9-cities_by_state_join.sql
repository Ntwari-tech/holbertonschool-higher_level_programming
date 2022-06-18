-- this scripts lists all the cities found in the server
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states on cities.state_id = state_id
ORDER BY cities.id ASC;
