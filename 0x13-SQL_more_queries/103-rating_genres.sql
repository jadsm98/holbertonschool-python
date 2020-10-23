-- Best genre
-- Commands
SELECT tg.name, SUM(tsr.rate) 'rating' FROM tv_genres AS tg LEFT JOIN tv_show_genres AS tsg ON tsg.genre_id = tg.id LEFT JOIN tv_show_ratings AS tsr ON tsr.show_id = tsg.show_id GROUP BY tg.name ORDER BY rating DESC;
