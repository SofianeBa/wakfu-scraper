import requests
import json

#Here we specify we only accept jsons
headers = {'Accept': 'application/json'}

#We send our request to get our json
#For more information about what links you can use to get jsons and data visit:
#https://www.wakfu.com/fr/forum/467-coin-developpeurs/416762-donnee-json
r = requests.get('https://wakfu.cdn.ankama.com/gamedata/1.78.1.7/states.json', headers=headers)

#Then we write it to the right file
with open(r".\Ressources\\1.78.1.7states.json", "w",encoding='utf-8') as file:
    json.dump(r.json(), file)

