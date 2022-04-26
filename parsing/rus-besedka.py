import requests
from bs4 import BeautifulSoup
import csv

URL = "https://rusbesedka.ru"


def all_urls():
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    menu_list = soup.find('ul', class_='menu-list').find_all('a')
    all_links = []
    for section in menu_list:
        all_links.append(section.get('href'))
    return all_links


def main():
    urls = all_urls()
    for url in urls:
        response = requests.post(URL + url)
        if response.status_code: print('Successful connection!\n')
        soup = BeautifulSoup(response.text, 'html.parser')
        items = soup.find_all('div', class_='product-card__info')
        hrefs = soup.find_all('a', class_='product-card__link')
        links = []
        for href in hrefs:
            links.append('https://rusbesedka.ru' + href.get('href'))
        links = links[1:]
        data = [url[13:-1]]
        counter = 0
        for item in items:
            price = item.find('span', class_='is-size-4 has-text-weight-bold')
            if price:
                components = [item.find('p', class_='product-card__title').text, price.text.replace('\xa0', ' ')]
            else:
                components = [item.find('p', class_='product-card__title').text, 'Цену уточняйте.']
            if counter < len(links):
                components.append(links[counter])
                data.append(components)
            else:
                data.append(components)
            counter += 1
        print('Processing...')
        with open('rus-besedka.csv', 'a', newline='', encoding='utf-16') as file:
            writer = csv.writer(file)
            writer.writerow([data[0]])
            for line in data[1:]:
                writer.writerow(line)
            writer.writerow('')


if __name__ == '__main__':
    main()
