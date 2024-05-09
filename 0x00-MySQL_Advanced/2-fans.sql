-- Import the metal_bands table dump
-- Assume the table name is metal_bands

-- ranks column name ordered by number of fans
SELECT origin, SUM(fans) AS nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;
