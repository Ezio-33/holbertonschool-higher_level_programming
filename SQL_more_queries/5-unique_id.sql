-- Créer la table unique_id avec les colonnes id et name
CREATE TABLE IF NOT EXISTS unique_id 
(
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);