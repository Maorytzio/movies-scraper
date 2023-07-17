import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
response.raise_for_status()
html_doc = response.text

soup = BeautifulSoup(html_doc, 'html.parser')
movies = soup.select('div h3')
txt_list = [movie.text for movie in movies[::-1]]

with open('movies.txt', 'w') as file:
    for movie in txt_list:
        try:
            file.write(f"{movie}\n")
        except UnicodeEncodeError:
            continue
