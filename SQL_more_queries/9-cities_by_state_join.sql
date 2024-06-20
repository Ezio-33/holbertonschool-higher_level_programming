-- Lister toutes les villes contenues dans la base de données hbtn_0d_usa avec leurs noms d'état correspondants
SELECT cities.id, cities.name, states.name 
	FROM cities
	INNER JOIN states
	ON cities.state_id = states.id
ORDER BY cities.id ASC;