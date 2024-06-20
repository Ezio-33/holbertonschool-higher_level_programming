-- Lister tous les genres de la base de données hbtn_0d_tvshows et afficher le nombre de shows liés à chaque genre

SELECT tv_genres.name AS genre, COUNT(*) AS number_of_shows
	FROM tv_genres
	INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
	GROUP BY tv_genres.name
ORDER BY number_of_shows DESC;