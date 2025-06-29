import requests

API_KEY = "44ff5034c0fae764719eb470ca0a72d6"
def get_data(place, forecast_days=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]

    return filtered_data

if __name__ == "__main__":
    print(get_data(place="Bengaluru", forecast_days=3, option="Temperature"))

# The below API also works
# API_KEY = "ab9d2e9488de2cba52f966b91c622d24"
# def get_data(place, forcast_days, option):
#     url = (f"https://api.weatherstack.com/current?
#     access_key={API_KEY}&query={place}")
#     return data
