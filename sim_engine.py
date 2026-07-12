# AtmoSync: Micro-Climate Arbitrage Analytics
# Day 2 - Simulation Engine Variables Setup

# 1. Base Environment Variables
target_location = "Hyderabad_Hub"
base_temperature = 28.5  # in Celsius
base_humidity = 62.0     # in Percentage
data_interval_sec = 5    # 5 seconds log cycle

# 2. Status Tracking Flags
is_engine_active = True
sim_error_count = 0

print("--- AtmoSync Simulation Engine Initialized ---")
print(f"Tracking Location: {target_location}")
print(f"Status: Active, Interval: {data_interval_sec}s")
