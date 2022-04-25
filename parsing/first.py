import csv
import requests # type: ignore
from bs4 import BeautifulSoup

url = "https://scrapingclub.com/exercise/list_basic/"

headers = {
    'accept': '*/*',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.44'
}

resp = requests.get(url)
resp.encoding = 'utf-8'
soup1 = BeautifulSoup(resp.text,'html.parser')
nums = []
all_pages = soup1.find_all('li',class_='page-item')

final_list = [["Название","Ссылка","Цена"]]

for i in range(1,len(all_pages)):

    new_url = url + f'?page={i}'
    response = requests.get(new_url,headers=headers)
    response.encoding = 'utf-8'
    print(response.status_code)
    if response.status_code:
        soup = BeautifulSoup(response.text, 'html.parser')
        #print(soup)
        all_bodies = soup.find_all("div", class_="col-lg-4 col-md-6 mb-4")
        #soup.find()
        for n,i in enumerate(all_bodies,start=1):
            #print(i)
            final_list.append([i.find('h4', class_='card-title').text.strip(),url + i.find('a')['href'],i.find('h5').text])
with open('names.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(final_list)