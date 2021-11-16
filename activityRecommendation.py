import requests

def randomActivity(prune=0):
    URL = "https://www.boredapi.com/api/activity/?"

    if prune != 0:
        URL += "participants=1"
        URL += "&price=0"
        URL += "&accessibility=0"
    page = requests.get(URL)
    return page.text