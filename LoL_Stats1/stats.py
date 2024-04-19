import requests

api_key = "RGAPI-edfb3f71-4cf2-4188-99da-7213db5b04e7"
api_url = "https://eun1.api.riotgames.com/lol/summoner/v4/summoners/by-name/biybi7"

api_url1 = api_url + '?api_key=' + api_key
resp = requests.get(api_url1)

player_info = resp.json()
print(player_info)
player_acc_id = player_info['accountId']
player_acc_level = player_info['summonerLevel']


