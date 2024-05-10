-- SQL script to list bands with Glam rock as their main style, ranked by their longevity


-- Write a SELECT query to retrieve band_name and compute lifespan
SELECT band_name AS band_name, IFNULL(split, 2022) - IFNULL(formed, 0) AS lifespan
-- if split column is NULL, it uses 2022 as the formation year
-- if formed column is NULL, it uses 0 as the value
-- it calculates longevity by subtracting formed year from split year
FROM metal_bands WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;
