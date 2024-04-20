import requests
import time

api_key = "RGAPI-22fd9f5f-6e39-4747-85c5-b3ddd066650f"
api_url = "https://eun1.api.riotgames.com/lol/summoner/v4/summoners/by-name/biybi7"

api_url = api_url + '?api_key=' + api_key

resp = requests.get(api_url)
player_info = resp.json()
player_account_id = player_info['accountId']

api_url = "https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/jCVBWDfyHb9j-5_0BWjriIf6DxEL7OMMh22zw0XBhcVFwpdWh4nOxUpVF2tKpbiQL_GyNOht6YNO6A/ids?start=0&count=20"
api_url = api_url + '&api_key=' + api_key
resp = requests.get(api_url)

matches = resp.json()
match1 = matches[0]

api_url = "https://europe.api.riotgames.com/lol/match/v5/matches/EUN1_3540778278"
api_url = api_url + "?api_key=" + api_key

resp = requests.get(api_url)
match_data = resp.json()

puuid = player_info['puuid']

puuid = "jCVBWDfyHb9j-5_0BWjriIf6DxEL7OMMh22zw0XBhcVFwpdWh4nOxUpVF2tKpbiQL_GyNOht6YNO6A"
puuid = "jCVBWDfyHb9j-5_0BWjriIf6DxEL7OMMh22zw0XBhcVFwpdWh4nOxUpVF2tKpbiQL_GyNOht6YNO6A"
part_index = match_data['metadata']['participants'].index(puuid)

# print(match_data['metadata']['participants'].index(puuid))

# print(match_data['info']['participants'][part_index]['kills'])
# print(match_data['info']['participants'][part_index]['assists'])
# print(match_data['info']['participants'][part_index]['deaths'])
# print(match_data['info']['participants'][part_index]['win'])


api_url = "https://europe.api.riotgames.com/lol/match/v5/matches/EUN1_3540778278?api_key=RGAPI-22fd9f5f-6e39-4747-85c5-b3ddd066650f"

region = "EUROPE"
match_id = "EUN1_3540778278"
api_key = "RGAPI-22fd9f5f-6e39-4747-85c5-b3ddd066650f"

def get_match_data(region, match_id, api_key):
    api_url = (
        "https://" + 
        region + 
        ".api.riotgames.com/lol/match/v5/matches/" + 
        match_id + 
        "?api_key=" + 
        api_key
    )
    resp = requests.get(api_url)
    data = resp.json()
    return data



match_data = get_match_data(region, match_id, api_key)

def did_win(puuid, match_data):
    part_index = match_data['metadata']['participants'].index(puuid)
    return match_data['info']['participants'][part_index]['win']
    



# for match_id in matches:
#     try:
#         match_data = get_match_data(region, match_id, api_key)
#         print(did_win(puuid,match_data))
#     except:
#         print("Null")

api_url = "https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/jCVBWDfyHb9j-5_0BWjriIf6DxEL7OMMh22zw0XBhcVFwpdWh4nOxUpVF2tKpbiQL_GyNOht6YNO6A/ids?type=ranked&start=0&count=100"


def get_matches(region, puuid, count, api_key):
    api_url = (
        "https://" + 
        region +
        ".api.riotgames.com/lol/match/v5/matches/by-puuid/" + 
        puuid + 
        "/ids" + 
        "?type=ranked&" + 
        "start=0&" + 
        "count=" +
        str(count) + 
        "&api_key=" + 
        api_key
    )
    while True:
        resp = requests.get(api_url)

        if resp.status_code==429:
            print("Wait")
            time.sleep(10)
            continue

        resp = requests.get(api_url)
        return resp.json()

matches = get_matches(region, puuid, 100, api_key)
matches.extend(matches)
print(len(matches))

game_number = 0
for match_id in matches:
    print(match_id)
    try:
        match_data = get_match_data(region, match_id, api_key)
        print(did_win(puuid,match_data))
        print("")
    except:
        print("Null")
# resp = requests.get(api_url)
# print(requests.get(api_url))

