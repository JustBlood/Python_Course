from bs4 import BeautifulSoup
import requests
import csv

def get_html(url,headers):
    response = requests.get(url, headers=headers)
    print(response.status_code)
    html = response.text

    soup = BeautifulSoup(html,'html.parser')
    items = soup.find_all('div', class_='audi-headline-order-3')
    items1 = soup.find_all('a', class_='nm-j-teaser-click-item')
    all_names = {}
    names = [item.text for item in items]
    links = ['https://www.audi.ru/'+item.get('href') for item in items1]
    return list(zip(names,links))
def main():
    URL = "https://www.audi.ru/ru/web/ru/model-range/a-models.html"

    HEADERS = {
        'accept': '*/*',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.50',
    }
    names = get_html(URL,HEADERS)
    with open('parsed.csv', 'w', encoding='utf-16', newline='') as file:
        writer = csv.writer(file)
        for i in range(len(names)):
            writer.writerow(names[i])

if __name__ == '__main__':
    main()
