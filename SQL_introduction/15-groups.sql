-- Lister le nombre d'enregistrements ayant le même score dans la table second_table
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;