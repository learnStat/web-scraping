from bs4 import BeautifulSoup
import requests
from datetime import datetime
import pandas as pd

base_url = "https://quotes.toscrape.com"
quotes = []
url = base_url

while True:
    response = requests.get(url)
    # print(f"Status code: {response.status_code} for {url}")
    if response.status_code != 200:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        exit()
    soup = BeautifulSoup(response.text, "html.parser")
    quotes_on_page = soup.find_all("div", class_="quote")

    for quote in quotes_on_page:
        text = quote.find("span", class_="text").get_text()
        author = quote.find("small", class_="author").get_text()
        quotes.append({"text": text, "author": author})

    next_button = soup.find("li", class_="next")
    if next_button and next_button.a:
        # print(f"Current URL: {url}")
        # print(f"Next button HTML: {next_button}")
        url = base_url + next_button.a['href']
    else:
        break
print(f"Total quotes scraped: {len(quotes)}")
user_input = input("Do you want to view all the quotes? (y/n): ").lower()
if user_input not in ['y', 'n']:
    print("Invalid input, saving to file by default")
    user_input = 'n'

if user_input == 'y':
    for quote in quotes:
        print(f"{quote['text']}  - {quote['author']}")
        print("-" * 50)
else:
    # save to file
    # with open("quotes.txt", "w", encoding="utf-8") as f:
    #     for quote in quotes:
    #         f.write(f"{quote['text']} - {quote['author']}\n")
    # print("Quotes saved to quotes.txt")
    df = pd.DataFrame(quotes)
    filename = datetime.now().strftime("%Y%m%d_%H%M%S") + "quotes.csv"
    df.to_csv(filename, index=False, encoding="utf-8")
    print(f"Quotes saved to {filename}")