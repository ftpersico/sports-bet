import requests
import json


print("Welcome to Bets 'R Us")
print("The top sports bet aggregation app in the world")

sport = 'baseball_mlb'
# TODO, allow user to input a sport - input("Which sport did you want to bet on?")
print('Selected sport:',sport)

team = 'New York Yankees'
# TODO, allow user to input a team - input("Which team did you want to bet on?")
print('Selected Team:',team)


region = 'uk'
# TODO, allow user to input a region - input("Which region are you betting in?")
print('Selected Region:',region)

# TODO pull api key from ENV file
apiKey = '1f8a56f5813ca49ce1552283c34d8466'

bet_amount = input("How much money did you want to bet? ")
print(bet_amount)

# URL of the Odds API
request_url = f'https://api.the-odds-api.com/v3/odds/?apiKey={apiKey}&sport={sport}&region={region}&mkt=h2h&dateFormat=iso&oddsFormat=american'


response = requests.get(request_url)
print("API Status:", response.status_code)

allbets = json.loads(response.text)

# TODO use this format to pull odds for each unique site
sample_odds = allbets['data'][0]['sites'][0]['odds']['h2h'][0]

# Variables for each bet site's odds
betfair_odds = 0
williamhill_odds = 0
paddypower_odds = 0
unibet_odds = 0
matchbook_odds = 0
betway_odds = 0
betfred_odds = 0

print(sample_odds)

# no input for game, will just do next game