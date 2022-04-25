from bs4 import BeautifulSoup
import requests
import json

URL = "https://auto.ru/moto/add/"
url_api = "https://auto.ru/-/ajax/forms/getBreadcrumbsPublicApi/"
url_api1 = "https://auto.ru/-/ajax/forms/saveDraftFormsToPublicApi"
with open('url_api.json') as file:
    json_api = json.load(file)
# with open('url_api1.json') as file:
#     json_api1 = json.load(file)

HEADERS = {
    'Accept': '*/*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.50'
         }
# first_response = requests.get(URL, headers=HEADERS)
# first_response.encoding = "utf-8"
# print(first_response.status_code)
# transport = []
# if response.status_code:
#     soup = BeautifulSoup(response.text, 'html.parser')
#     items = soup.find_all('span', class_='Radio__text')
#     for item in items:
#         transport.append(item.text)
response = requests.post(url_api, json=json_api, headers=HEADERS)
response.encoding = 'utf-8'
print(response.json())
# with open('response.json', 'w') as file:
#     file.write(response.json())
# response1 = requests.post(url_api1, json=json_api1, headers=HEADERS)
# response = requests.get(URL, headers=HEADERS)
# marks = []
# if response.status_code:
#     soup1 = BeautifulSoup(response.text, 'html.parser')
#     if soup == soup1:
#         print("ЕПТВОЮ МАТЬ ДА КАК ЭТО ЗАПАРСИТЬ")
#         exit()
#     print("ЕБАТЬ ТУТ ЧТО_ТО ДРУГОЕ\n")
#     items = soup1.find_all('div', class_='FormSection__ListItemText')
#     for item in items:
#         marks.append(item.text)
# print(transport,marks)
