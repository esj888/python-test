# https://pixe.la/v1/users/jasminemutt/graphs/graph1.html

import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "jasminemutt"
TOKEN = "thisismydogfrommililani2020"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

graph_config = {
    "id": "graph1",
    "name": "walking graph",
    "unit": "mi",
    "type": "float",
    "color": "ajisai"
}

# today = datetime(year=2022, month=7, day=22)
today = datetime.now()

add_pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("how many miles did jasmine walk today? ")
}

update_pixel_config = {
    "quantity": "2.5"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# create account
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# create graph
# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response)

# post a pixel to graph
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"
response = requests.post(url=graph_endpoint, json=add_pixel_config, headers=headers)
print(response)

# update a pixel
# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/20220722"
# response = requests.put(url=graph_endpoint, json=update_pixel_config, headers=headers)
# print(response)

# delete a pixel
# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/20220722"
# response = requests.delete(url=graph_endpoint, headers=headers)
# print(response)
