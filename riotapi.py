import requests

api_key = "RGAPI-03af00bd-4e57-4b49-b325-5913b83dfa47"
summoner_name = 'limion'

# 소환사명으로 소환사 정보 가져오기
response = requests.get(f'https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summoner_name}?api_key={api_key}')
summoner_data = response.json()

print(summoner_data)


account_id = summoner_data['accountId']
response = requests.get(f'https://kr.api.riotgames.com/lol/match/v4/matchlists/by-account/{account_id}?api_key={api_key}&endIndex=1')
match_data = response.json()




print(match_data)
#game_id = match_data['matches'][0]['gameId']
#response = requests.get(f'https://kr.api.riotgames.com/lol/match/v4/matches/{game_id}?api_key={api_key}')
#game_data = response.json()

#print(game_data)

url = f"https://kr.api.riotgames.com/lol/match/v4/matchlists/by-account/{account_id}?api_key={api_key}"
response = requests.get(url)
recent_games = response.json()

print(recent_games)
