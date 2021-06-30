import pytest
from bets import create_dictionary


sample_data = {
  "success": "true",
  "data": [
    {"id": "111","sport_key": "baseball_mlb", "sport_nice": "MLB",
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
          "odds": {"h2h": [146,-250],"h2h_lay": [174,-145]}}
      ],
      "sites_count": 2
    },
    {"id": "111","sport_key": "baseball_mlb", "sport_nice": "MLB",
      "teams": ["Baltimore Orioles", "New York Yankees"],
      "home_team": "New York Yankees",
      "commence_time": "2021-06-23T23:05:00Z",
      "sites": [
        {"site_key": "paddypower",
          "site_nice": "Paddy Power",
          "last_update": "2021-06-23T01:08:20Z",
          "odds": {"h2h": [300,-500]}},
        {"site_key": "betfair",
          "site_nice": "Betfair",
          "last_update": "2021-06-23T01:08:41Z",
          "odds": {"h2h": [350,-600],"h2h_lay": [174,-145]}}
      ],
      "sites_count": 2
    }
  ]
}


def test_create_dictionary():
    all_odds = {}
    data = sample_data
    all_odds = create_dictionary(data,'New York Yankees')
    assert all_odds == {"Paddy Power":-200, "Betfair":-250}
    print(all_odds)