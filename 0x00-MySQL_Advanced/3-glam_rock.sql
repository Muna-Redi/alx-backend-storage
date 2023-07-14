-- This MySQL script lists all bands with Glamrock
-- as their main style, and ranked by their lifespan

SELECT band_name, (IFNULL(split, '2022') - formed) AS lifespan
    FROM metal_bands
    WHERE style LIKE '%Glam rock%'
    ORDER BY lifespan DESC;
