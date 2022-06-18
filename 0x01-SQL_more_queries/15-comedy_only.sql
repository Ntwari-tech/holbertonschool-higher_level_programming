-- this script lists all the comdedy shows in a given database
SELECT tv_shows.title
from tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_show_genres.name = 'Comedy'
ORDER BY tv_shows.title ASC;
