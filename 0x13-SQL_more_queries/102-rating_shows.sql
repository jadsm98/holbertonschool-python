-- Rotten Tomatoes
-- Commands
SELECT ts.title, SUM(tsr.rate) 'rating' FROM tv_shows AS ts LEFT OUTER JOIN tv_show_ratings AS tsr ON tsr.show_id = ts.id GROUP BY ts.title ORDER BY rating DESC;
