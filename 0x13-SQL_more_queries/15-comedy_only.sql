-- Only Comedy
-- Commands
SELECT DISTINCT ts.title FROM tv_shows AS ts LEFT OUTER JOIN tv_show_genres AS tsg ON ts.id = tsg.show_id LEFT OUTER JOIN tv_genres AS tg ON tsg.genre_id = tg.id WHERE tg.name = 'Comedy' ORDER BY ts.title ASC;
