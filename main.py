import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
web_page = response.text

soup = BeautifulSoup(web_page, 'html.parser')
all_films = [title.getText() for title in soup.find_all(name='h3', class_='title')]
all_films.reverse()
with open('films100.txt', 'w') as films:
    for film in all_films:
        films.write(f'{film}\n')

