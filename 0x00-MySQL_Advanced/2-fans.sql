-- Import the metal_bands table dump
-- Assume the table name is metal_bands

-- ranks column name ordered by number of fans
SELECT origin, SUM(nb_fans) AS total_fans
FROM metal_bands
GROUP BY origin
ORDER BY total_fans DESC;
