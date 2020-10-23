-- My genres
-- Commands
SELECT DISTINCT tg.name FROM tv_genres AS tg LEFT OUTER JOIN tv_show_genres AS tsg ON tg.id = tsg.genre_id LEFT OUTER JOIN tv_shows AS ts ON tsg.show_id = ts.id WHERE ts.title = 'Dexter' ORDER BY tg.name ASC;
