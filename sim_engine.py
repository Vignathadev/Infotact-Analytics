# AtmoSync: Micro-Climate Arbitrage Analytics
# Day 3 - Simulation Engine Logic Framework

# 1. Base Environment Variables
target_location = "Hyderabad_Hub"
base_temperature = 28.5  # in Celsius
base_humidity = 62.0     # in Percentage
data_interval_sec = 5    # 5 seconds log cycle

# 2. Status Tracking Flags
is_engine_active = True
sim_error_count = 0

# 3. Arithmetic Analytics Calculations (Day 3 Added Logic)
# Let's calculate simple apparent temperature factor metric equations
# Formula approach: $T_{apparent} = T_{base} + (0.33 \times H_{base}) - 4.0$
apparent_temp = base_temperature + (0.33 * base_humidity) - 4.0

print("--- AtmoSync Simulation Engine Initialized ---")
print(f"Tracking Location: {target_location}")
print(f"Status: Active, Interval: {data_interval_sec}s")
print(f"Calculated Apparent Temperature Matrix Factor: {apparent_temp:.2f}°C")