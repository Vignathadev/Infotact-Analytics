-- Relational staging schema definitions for inbound raw telemetry
CREATE TABLE IF NOT EXISTS staging_telemetry (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    location TEXT NOT NULL,
    temperature_c REAL NOT NULL,
    humidity_pct REAL NOT NULL,
    apparent_temperature_c REAL NOT NULL,
    timestamp TEXT NOT NULL
);