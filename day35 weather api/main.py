import requests
from twilio.rest import Client

account_sid = "AC5150af91ac1168f07665c86ffb12d7ed"
auth_token = "1666e4fd131f638fcaabfbdc3bc1b86d"


parameters = {
    'appid': "105b39a7386bdc2a4b647d27360bb09c",
    # 'lat': "21.306944",   # honolulu
    # 'lon': "-157.858337", # honolulu
    'lat': "40.440624",   # rainy test
    'lon': "-79.995888",  # rainy test
    'exclude': "current,minutely,daily"
}

# ---------------------------- call twilio ------------------------------- #


def send_sms():
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
            body="It's going to rain today ☔",
            from_='+13257700650',
            to='+18083839709'
        )

    # print(message.sid)
    print(message.status)

# ------------------------------------------------------------------------ #


debug = False      # turn on print statements

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
print(f"Response status code = {response.status_code}")
data = response.json()

if debug:
    print(data)
    print(type(data))
    print(data["timezone"])
    print(data["hourly"][0]["dt"])
    print(data["hourly"][0]["weather"][0]["id"])

weather_codes = []
for i in range(12):
    if debug:
        print(f'{i} {data["hourly"][i]["weather"][0]["id"]}')
    weather_codes.append(data["hourly"][i]["weather"][0]["id"])
    if int(weather_codes[i]) < 700:
        print("Bring an umbrella!")
        send_sms()

for code in weather_codes:
    print(f"code {code}")
