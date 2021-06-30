import requests
import json
from dotenv import load_dotenv
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from datetime import date


# Filter data for first game of selected team and create a dictionary with the odds for all sites
def create_dictionary(data,team):
    all_odds = {}
    for i in data['data']:
        if team in i['teams']:
            team_index = i['teams'].index(team)
            for a in i['sites']:
                all_odds.update({
                    a['site_nice'] : a['odds']['h2h'][team_index]
                })
            print("")
            break
    return all_odds



if __name__ == "__main__":

    load_dotenv()
    # TODO Delete this sample data after build is complete 
    API_KEY = os.getenv("API_KEY", default=0)

    # Convert to USD formart
    def to_usd(my_price):
        """
        Converts a numeric value to usd-formatted string, for printing and display purposes.

        Param: my_price (int or float) like 4000.444444

        Example: to_usd(4000.444444)

        Returns: $4,000.44
        """
        return f"${my_price:,.2f}" #> $12,000.71


    #  Define the available sports and teams to query
    avail_sports = ["baseball_mlb"]
    avail_teams = ["New York Yankees", "Toronto Blue Jays", "Baltimore Orioles", "Boston Red Sox", "Tampa Bay Rays"]
    #avail_teams = ["NYY", "TOR", "BAL", "BOS", "TB"]

    print("")
    print("****************************************")
    print("")
    print("Welcome to Bets 'R Us")
    print("The top sports bet aggregation app in the world")
    print("")


    print("The following sports are available: BASEBALL")
    print("You can also enter 'DONE' to leave the program\n")

    # Allows user to input a sport to query. Checks if sport is in acceptable list
    while True:
        sport = str.lower(input("Which sport did you want to bet on? "))
        if sport in ['baseball', 'mlb']:
            sport = 'baseball_mlb'
        elif sport == 'done':
            exit() 
        if sport in avail_sports:
            print("")
            break
        else:
            print("Sorry, that sport isn't available at this time, please try again")
            print("")


    print("""The following teams are available: 
    New York Yankees
    Toronto Blue Jays
    Baltimore Orioles
    Boston Red Sox
    Tampa Bay Rays""")
    print("You can also enter 'DONE' to leave the program\n")

    # Allows user to input a sport to query. Checks if sport is in acceptable list
    while True:
        team = input("Which team did you want to bet on? ")
        team = str.title(team)
        if team == 'Done':
            exit()
        if team in avail_teams:
            break
        else:
            print("Sorry, that team isn't available at this time, please try again")
            print("")

    print('Selected Team:',team,"\n")

    while True:
        recipient_email = input("What is your email address? ")
        bettor_name = input("What is your name? ")
        break


    region = 'uk'
    print('Selected Region:',region.upper())

    # Pull api key from ENV file
    load_dotenv()
    apiKey = os.getenv("API_KEY", default=0) 

    # Allow user to input an amount they want to bet 
    print("")
    bet_amount = float(input("How much money did you want to bet? "))
    print(to_usd(bet_amount))
    print("")

    # Get response from The Odds API
    request_url = f'https://api.the-odds-api.com/v3/odds/?apiKey={apiKey}&sport={sport}&region={region}&mkt=h2h&dateFormat=iso&oddsFormat=american'
    response = requests.get(request_url)
    print("API Status:", response.status_code)
    all_data = json.loads(response.text)

    # Call function to create odds dictionary
    all_odds = create_dictionary(all_data,team)

    # Determine the opponenent and print name
    opponent = 'Sorry no opponent found'

    for i in all_data['data']:
        if team in i['teams']:
            if i['teams'][0] == team:
                opponent = i['teams'][1]
            elif i['teams'][1] == team:
                opponent = i['teams'][0]

    print("-------------------------------------")
    print(f"Selected Team: {team}")
    print('Opponent:', opponent)

    # Print game day
    game_day ='Sorry no game found'

    for i in all_data['data']:
        if team in i['teams']:
            game_day = i['commence_time'].split("T")[0]

    print('Game Day:', game_day)

    # Return a value if no odds are avaialble 
    best_odds = -10000000000
    best_site = 'Sorry no sites found'
    if not all_odds:
        all_odds = 'Sorry no odds available for that team'
    else:
        for odds in all_odds:
            if all_odds[odds] > best_odds:
                best_odds = all_odds[odds]
                best_site = odds

    # Calculate the amount the user would win
    win = 0
    if best_odds >0:
        win = best_odds/100*bet_amount
    elif best_odds <0:
        win = bet_amount/best_odds*-100


    print(f"Bet amount: {to_usd(bet_amount)}")
    print("")
    print(f"The site with the most favorable odds is {best_site}")
    print(f"{best_site} has odds of {best_odds}")
    print("")
    print(f"If the {team} win, your net winnings are {to_usd(win)}.")
    print(f"If the {team} lose, your loss is {to_usd(bet_amount)}")
    print("")

    print("-------------------------------------")

    #Call email service 

    SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")
    SENDER_EMAIL_ADDRESS = os.getenv("SENDER_EMAIL_ADDRESS")

    def send_email(subject, html, recipient_address=recipient_email):
        """
        Sends an email with the specified subject and html contents to the specified recipient,
        If recipient is not specified, sends to the admin's sender address by default.
        """
        client = SendGridAPIClient(SENDGRID_API_KEY) #> <class 'sendgrid.sendgrid.SendGridAPIClient>
        print("CLIENT:", type(client))
        print("SUBJECT:", subject)
        #print("HTML:", html)
        message = Mail(from_email=SENDER_EMAIL_ADDRESS, to_emails=recipient_address, subject=subject, html_content=html)
        try:
            response = client.send(message)
            print("RESPONSE:", type(response)) #> <class 'python_http_client.client.Response'>
            print(response.status_code) #> 202 indicates SUCCESS
            return response
        except Exception as e:
            print("OOPS", type(e), e.message)
            return None

    # Display outputs in email
    todays_date = date.today().strftime('%A, %B %d, %Y')
    html = ""
    html += f"<h3>Hey {bettor_name}, good luck on your bet!!</h3>"
    html += "<h4>Today's Date</h4>"
    html += f"<p>{todays_date}</p>"
    html += f"<h4>We're recommending you book your bet on {best_site} since the odds are {best_odds}</h4>"
    html += f"<h4>Below are the sites and odds scanned</h4>"
    for i in all_odds:
        html += f"<b>Site:</b> {i} / <b>Odds:</b> {all_odds[i]}<br>" 
    html += f"<h5>Remember, bet with your head, not over it! If you feel like your gambling addiction is spirling out of control because you're a complete degenerate, please contact Gamblers Anonymous at 1-800-522-4700</h5>"
    send_email(subject="Your recommended betting site with Bets 'R Us", html=html)


    exit()
