import statistics

# Weather data for Gandhinagar (last 10 days)
temperature = [32, 34, 33, 35, 36, 34, 33, 32, 31, 35]   # Celsius
humidity = [60, 65, 63, 70, 72, 68, 66, 64, 62, 69]      # %
aqi = [120, 135, 128, 140, 150, 138, 130, 125, 118, 145] # Air Quality Index

# Temperature analysis
avg_temp = statistics.mean(temperature)
median_temp = statistics.median(temperature)

# Humidity analysis
avg_humidity = statistics.mean(humidity)
median_humidity = statistics.median(humidity)

# AQI analysis
avg_aqi = statistics.mean(aqi)
median_aqi = statistics.median(aqi)

print("Temperature Average:", avg_temp)
print("Temperature Median:", median_temp)

print("Humidity Average:", avg_humidity)
print("Humidity Median:", median_humidity)

print("AQI Average:", avg_aqi)
print("AQI Median:", median_aqi)
