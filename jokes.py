import os
import sys
import requests
import urllib3
import json

def mattermost():
    with open("mattermost.json", "r") as file:
        config = json.loads(file.read())
    print(config)
    # requests.put()

def dad_joke():

    headers = {
        'User-Agent': 'mattermost-dad-jokes (github.com/mfadem/mattermost-dad-jokes)'
    }

    response = requests.get("https://icanhazdadjoke.com/slack", headers=headers)
    content = response.json()
    print(content['attachments'][0]['text'])

def main():
    dad_joke()
    mattermost()

if __name__ == '__main__':
    main()