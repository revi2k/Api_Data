import requests
import json

api_url = "https://api.github.com/users"

response = requests.get(api_url)
data = response.json()


def checkAdmin(user):
    if user['site_admin'] == True:
        return "Administrator"
    else:
        return "No administrator"

for user in data:
    print("Login: "+user['login']+", GitHub URL: "+user['url']+", is admin: "+checkAdmin(user))

