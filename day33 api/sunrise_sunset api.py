import requests
from _datetime import datetime

MY_LAT = 21.306944
MY_LONG = -157.858337

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()  # check error
data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

# split or extract hour
print(sunrise)
sunrise_hr = sunrise.split("T")[1].split(":")[0]
sunset_hr = sunset.split("T")[1].split(":")[0]

print(sunrise_hr)
print(sunset_hr)

time_now = datetime.now()
print(time_now.hour)

