-- SQL script to list bands with Glam rock as their main style, ranked by their longevity

-- Import the provided table dump into your database

-- Write a SELECT query to retrieve band_name and compute lifespan
SELECT band_name,
	(2022 - formed) - split(lifespan, '-', 1)::INT AS lifespan
FROM metal_bands WHERE style = 'Glam rock'
ORDER BY lifespan DESC;
