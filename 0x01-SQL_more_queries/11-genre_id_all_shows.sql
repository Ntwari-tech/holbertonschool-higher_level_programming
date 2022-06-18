-- this script list all the shows found in a given server
SELECT tv_shows.titl, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
