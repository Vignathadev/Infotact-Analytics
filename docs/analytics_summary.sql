-- Analytical summary queries to aggregate historical telemetry metrics
SELECT 
    location,
    COUNT(*) AS total_records,
    ROUND(AVG(temperature_c), 2) AS avg_temperature,
    ROUND(AVG(humidity_pct), 2) AS avg_humidity,
    ROUND(AVG(apparent_temperature_c), 2) AS avg_apparent_temp,
    MAX(temperature_c) AS max_temperature,
    MIN(temperature_c) AS min_temperature
FROM 
    staging_telemetry
GROUP BY 
    location;