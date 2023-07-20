import requests

response = requests.get('https://jsonplaceholder.typicode.com/todos')
# print(response)
# print(response.json())

import json

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

jprint(response.json())
# pass_times = response.json()[1]
pass_times = response.json()[0]

jprint(pass_times)

# user =[]
# for person in pass_times:
#     per = person
#     user.append(per)
# print(user)
from datetime import datetime

times = []

for rt in risetimes:
    time = datetime.fromtimestamp(rt)
    times.append(time)
    print(time)