-- Not my genre
-- Commands
SELECT DISTINCT tg.name FROM tv_genres AS tg LEFT OUTER JOIN tv_show_genres AS tsg ON tg.id = tsg.genre_id WHERE tg.id NOT IN (SELECT tsg.genre_id FROM tv_show_genres AS tsg LEFT OUTER JOIN tv_shows AS ts ON tsg.show_id = ts.id WHERE ts.title = 'Dexter') ORDER BY tg.name ASC;
