import os

# convert to USD formart
def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.

    Param: my_price (int or float) like 4000.444444

    Example: to_usd(4000.444444)

    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71


avail_sports = ["MLB"]
avail_teams = ["NYY", "TOR", "BAL", "BOS", "TB"]

print("")
print("****************************************")
print("")
print("Welcome to Bets 'R Us")
print("The top sports bet aggregation app in the world")
print("")

while True:
    sport = input("Which sport did you want to bet on? ")
    if sport in avail_sports:
        break
    else:
        print("Sorry, that sport isn't available at this time, please try again")
        print("")
print(sport)
print("")


while True:
    team = input("Which team did you want to bet on? ")
    if team in avail_teams:
        break
    else:
        print("Sorry, that team isn't available at this time, please try again")
        print("")
print(team)
print("")

bet_amount = input("How much money did you want to bet? ")
print(bet_amount)
print("")

# no input for game, will just do next game