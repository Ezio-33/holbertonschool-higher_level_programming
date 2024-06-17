-- Lister tous les enregistrements de la table second_table avec un score >= 10
-- Afficher le score et le nom, triés par score décroissant
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;