import requests
import json
from openpyxl import Workbook

api_url = "https://api.github.com/users"

response = requests.get(api_url)
data = response.json()

#FUNCTION CHECKING IF USER = ADMIN
def checkAdmin(user):
    if user['site_admin'] == True:
        return "Administrator"
    else:
        return "No administrator"


#SAVE API DATA TO EXCEL
def save_as_excel():
    wb = Workbook()
    filepath = "here_specific_path_to_save"
    ws = wb.active
    ws.append(['Login', 'GitHub URL', 'IsAdmin?'])
    for user in data:
        ws.append([user['login'], user['url'], checkAdmin(user)])
    wb.save(filepath)

save_as_excel()