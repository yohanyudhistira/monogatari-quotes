import requests
from bs4 import BeautifulSoup
import pandas as pd

quotes_list = []
url = 'https://animemotivation.com/monogatari-quotes/'


r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
quotes = soup.find_all('blockquote')

for item in quotes:
    quote = {
        'quotes': item.text.strip()
    }
    quotes_list.append(quote)

df = pd.DataFrame(quotes_list)
print('Saved to CSV')
df.to_csv('monogatari_quotes.csv', index=False)

