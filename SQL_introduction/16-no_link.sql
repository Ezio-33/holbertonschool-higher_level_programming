-- Lister tous les enregistrements de la table second_table avec un nom
-- Afficher le score et le nom, triés par score décroissant
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;