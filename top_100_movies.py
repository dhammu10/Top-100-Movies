import requests
from bs4 import BeautifulSoup
URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)

html_file = response.text
# print(html_file)
soup = BeautifulSoup(html_file, "html.parser")

# print(soup.prettify())

all_movies = soup.find_all(name="h3", class_="title")

# print(all_movies)
movies_title = [movies.getText() for movies in all_movies]
movies_title.reverse()
# print(movies_title)

with open("movies.text", mode="w") as file:
    for item in movies_title:
        try:
            file.write(f"{item}\n")
        except UnicodeError:
            file.write("Item Not found\n")
