-- SQL Query engine logic to automatically unpack JSON data rows attributes into clean staging target columns
SELECT 
    json_extract(value, '$.location') AS location,
    json_extract(value, '$.temperature_c') AS temperature_c,
    json_extract(value, '$.humidity_pct') AS humidity_pct,
    json_extract(value, '$.apparent_temperature_c') AS apparent_temperature_c,
    json_extract(value, '$.timestamp') AS timestamp
FROM 
    json_each(read_file('storage/telemetry_data.jsonl'));