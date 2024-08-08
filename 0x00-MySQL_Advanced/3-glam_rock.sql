-- Retrieves a list of glam rock metal bands, sorted by their lifespan in descending order.
-- The lifespan is calculated as the difference between the band's split year (or 2022 if the band is still active) and the year they were formed.

SELECT band_name, ((IFNULL(split, 2022)) - formed) AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;