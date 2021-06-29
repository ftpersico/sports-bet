# Sports Betting API

## Installation

Clone [this repo](https://github.com/ftpersico/sports-bet), onto your local computer, then navigate there from the command-line.

To install the packages you'll need for this program run

    pip install -r requirements.txt

To set up your Python environment run the commands:

    conda create -n bet-env python=3.8
    conda activate bet-env

Next create a .env file in your root directory, which you'll use to store your API keys and email address. 

## API Preparation
Before you run the app you'll need to get API keys for The Odds and Sendgrid. 

To get the first key go to https://the-odds-api.com/ and request an API KEY. Save the key in your .env file in the below format:
    
    API_KEY = "Your Key Here"

TO get the second key go to https://signup.sendgrid.com/ and request a key. Save that key, along with the email address you want to send your notification emails from as below:

    SENDGRID_API_KEY = "Your Key Here" 
    SENDER_EMAIL_ADDRESS= "Your email address here"

Now you should be able to run the app.

