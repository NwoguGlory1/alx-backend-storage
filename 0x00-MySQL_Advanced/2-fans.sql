-- ranks column name ordered by number of fans
SELECT origin, nb_fans,
       RANK() OVER (ORDER BY nb_fans DESC) AS rank
FROM metal_bands;
