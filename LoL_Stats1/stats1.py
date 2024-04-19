import requests

api_key = "RGAPI-edfb3f71-4cf2-4188-99da-7213db5b04e7"
api_url = "https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/jCVBWDfyHb9j-5_0BWjriIf6DxEL7OMMh22zw0XBhcVFwpdWh4nOxUpVF2tKpbiQL_GyNOht6YNO6A/ids?start=0&count=20"

api_url1 = api_url + "&api_key=" + api_key
resp = requests.get(api_url1)

matches = resp.json()

match = matches[0]

api_url2 = "https://europe.api.riotgames.com/lol/match/v5/matches/EUN1_3540778278"
api_url3 = api_url2 + "?api_key=" + api_key
resp1 = requests.get(api_url3)

game1 = resp1.json()
game1_metadata  = game1['metadata']
game1_info = game1['info']

game1_info_keys = game1_info.keys()
print(game1_info_keys)
print(f"\n{game1_info['participants'][0]['championName']}\n")

print(game1_metadata)

player_puuid = "jCVBWDfyHb9j-5_0BWjriIf6DxEL7OMMh22zw0XBhcVFwpdWh4nOxUpVF2tKpbiQL_GyNOht6YNO6A"

my_stats = game1_metadata['participants'].index(player_puuid)
print("\n")
print(game1_info['participants'][my_stats]['championName'])


