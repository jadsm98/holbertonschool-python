-- Number of shows by genre
-- Command
SELECT tv_genres.name 'genre', COUNT(tv_show_genres.genre_id) 'number_of_shows' FROM tv_genres LEFT OUTER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id WHERE tv_show_genres.genre_id <> '0' GROUP BY genre ORDER BY number_of_shows DESC;
