-- SQL script to list bands with Glam rock as their main style, ranked by their longevity


-- Write a SELECT query to retrieve band_name and compute lifespan
SELECT band_name AS band_name, IFNULL(split, 2022) - IFNULL(formed, 0) AS lifespan
FROM metal_bands WHERE style = 'Glam rock'
ORDER BY lifespan DESC;
