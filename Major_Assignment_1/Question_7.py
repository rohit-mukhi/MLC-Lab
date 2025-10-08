import numpy as np

daily_temperatures = np.full(31, 0)

for day in range(31):
    daily_temperatures[day] = np.random.randint(20, 41)

print("The daily temperatures were as follows:")
print(daily_temperatures)
print(f"The temperature was highest on day {np.argmax(daily_temperatures) + 1}")
print(f"The average temperature was: {np.mean(daily_temperatures):.1f} degree celsius")
print(f"The median temperature stood at: {np.median(daily_temperatures):.1f} degree celsius")
print(f"The standard deviation in daily temperatures was: {np.std(daily_temperatures):.1f}")
