import json

path = "C:\Users\Роллан\work\Labs\shows.json"
with open(path, "r") as file:
    data = json.loads(file)

for i in data["_embedded"]:
    if data["_embedded"]["episodes"]["rating"]["avarage"] < 8.4:
        print(data["_embedded"]["episodes"]["name"])