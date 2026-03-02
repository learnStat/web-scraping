from bs4 import BeautifulSoup
import requests

url ="https://quotes.toscrape.com"
response = requests.get(url)
if response.status_code != 200:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
    exit()

soup = BeautifulSoup(response.text, "html.parser")
quotes = soup.find_all("div",class_="quote")
for quote in quotes:
    text = quote.find("span", class_="text").get_text()
    author = quote.find("small", class_="author").get_text()
    print(f"{text} - {author}")
    print("-" * 50)
# movies = soup.find(class_="ipc-metadata-list")
# print(movies)