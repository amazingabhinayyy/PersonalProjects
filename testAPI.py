#python3 -m venv .venv
#(base) Abhinays-MacBook-Pro-2:EzWorld abhinayputta$ chmod +x env/Scripts/activate
#(base) Abhinays-MacBook-Pro-2:EzWorld abhinayputta$ source env/Scripts/activate
import requests
import random 

path = "https://uselessfacts.jsph.pl/api/v2/facts/random"
path2 = "https://api.quotable.io/random"
path3 = "https://cataas.com/cat/says/"

response = requests.get(path)
resjson = response.json()

response2 = requests.get(path2)
resjson2 = response2.json()

res3 = requests.get(path3)


print(resjson["text"])

path3 = path3 + resjson2["content"]
print(resjson2["content"])

response3 = requests.get(path3)
print(response3.)

