-- Lister tous les shows contenus dans la base de données hbtn_0d_tvshows, y compris ceux qui n'ont pas de genre lié

SELECT tv_shows.title, tv_show_genres.genre_id
	FROM tv_shows
	LEFT JOIN tv_show_genres 
	ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;