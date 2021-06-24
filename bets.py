import requests
import json
from operator import itemgetter
from dotenv import load_dotenv
import os

load_dotenv()
# TODO Delete this sample data after build is complete 
API_KEY = os.getenv("API_KEY", default=0)

sample_data = {
  "success": "true",
  "data": [
    {"id": "159fb6cae00fd84860e37a3e4ebf6ba5","sport_key": "baseball_mlb", "sport_nice": "MLB",
      "teams": ["Kansas City Royals", "New York Yankees"],
      "home_team": "New York Yankees",
      "commence_time": "2021-06-22T23:05:00Z",
      "sites": [
        {"site_key": "paddypower",
          "site_nice": "Paddy Power",
          "last_update": "2021-06-23T01:08:20Z",
          "odds": {"h2h": [150,-200]}},
        {"site_key": "betfair",
          "site_nice": "Betfair",
          "last_update": "2021-06-23T01:08:41Z",
          "odds": {"h2h": [146,-172],"h2h_lay": [174,-145]}}
      ],
      "sites_count": 2
    }
  ]
}

print("Welcome to Bets 'R Us")
print("The top sports bet aggregation app in the world")

sport = input("Which sport did you want to bet on? ")
print(sport)
sport = 'baseball_mlb'
# TODO, allow user to input a sport - input("Which sport did you want to bet on?")
print('Selected sport:',sport)


team = input("Which team did you want to bet on? ") #this is going to have to be an input
# TODO, allow user to input a team - input("Which team did you want to bet on?")
print('Selected Team:',team)


#region = input("Which region did you want to bet?")
#print(team)
#region = 'uk'
# TODO, allow user to input a region - input("Which region are you betting in?")
#print('Selected Region:',region.upper())

bet_amount = input("How much money did you want to bet? ")
print(bet_amount)

# Defined a variable per bet site
# TODO uncomment this when pulling from the API for real
request_url = f'https://api.the-odds-api.com/v3/odds/?apiKey={API_KEY}&sport={sport}&region=us&mkt=h2h&dateFormat=iso&oddsFormat=american'
response = requests.get(request_url)
print("API Status:", response.status_code)
all_data = json.loads(response.text)

#TODO comment this out when switching to the real API. Delete after build is complete
all_data = sample_data

# TODO only pull data for the selected team

# Create a dictionary with the odds for all sites
all_odds = {}

#need to sort the a['site_nice'] on high to low

for a in all_data['data'][0]['sites']:
    all_odds.update({
        a['site_nice'] : a['odds']['h2h'][0]
    })

if not all_odds:
    all_odds = 'Sorry no odds available'
print(all_data)
print(type(all_data))

sorted_odds = sorted(sites, key=itemgetter('h2h'), reverse=True)
print(sorted_odds)
exit()
# TODO remove when done testing app 
print("All Odds:", all_odds)

# TODO Decide if we're going to use these variables for each bet site's odds
betfair_odds = 0
williamhill_odds = 0
williamhill_odds = 0 
paddypower_odds = 0
unibet_odds = 0
matchbook_odds = 0
betway_odds = 0
betfred_odds = 0

# Determine the opponenent and print name
if all_data['data'][0]['teams'][0] == "New York Yankees":
    opponent = all_data['data'][0]['teams'][1]
else:
    opponent = all_data['data'][0]['teams'][0]

print('Opponent:', opponent)

# Print game day
game_day = all_data['data'][0]['commence_time'].split("T")[0]
print('Game Day:', game_day)



# no input for game, will just do next game 
# no input for game, will just do next game