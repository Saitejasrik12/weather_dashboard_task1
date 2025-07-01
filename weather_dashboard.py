import requests
import matplotlib.pyplot as plt
import seaborn as sns

# Replace with your actual API key
API_KEY = "b6c4500d2c6316db548cd8934d107121"
CITY = "Chennai"

# API URL
url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
response = requests.get(url)
data = response.json()
print(data)  # <- Add this line

# Extract weather information
weather_data = {
    "Temperature (°C)": data["main"]["temp"],
    "Feels Like (°C)": data["main"]["feels_like"],
    "Humidity (%)": data["main"]["humidity"],
    "Pressure (hPa)": data["main"]["pressure"]
}

# Plotting with Seaborn
sns.set(style="whitegrid")
plt.figure(figsize=(8, 5))
sns.barplot(x=list(weather_data.keys()), y=list(weather_data.values()), palette="coolwarm")
plt.title(f"Current Weather in {CITY}", fontsize=16)
plt.ylabel("Value")
plt.tight_layout()
plt.savefig("weather_chart.png")  # Saves the chart
plt.show()
