import requests
from bs4 import BeautifulSoup

page = requests.get('https://www.tickertape.in/market-mood-index')

soup = BeautifulSoup(page.content, 'html.parser')

# title = soup.title.text

first_h1 = soup.select('h1')[0].text

seventh_p_text = soup.select('p')[6].text

market_mood_index = first_h1+" : "+seventh_p_text

mmi = float(seventh_p_text)

if mmi > 80:
    comment = "High Extreme Greed Zone, Do not open new positions, Markets are overbought and likely to turn downwards"
elif mmi > 70:
    comment = "Extreme Greed Zone, Keep tracking actively"
elif mmi > 50:
    comment = "Greed Zone, No need to react"
elif mmi > 30:
    comment = "Fear Zone, No need to react"
elif mmi > 20:
    comment = "Extreme Fear Zone, Keep tracking actively"
else:
    comment = "High Extreme Fear Zone, Good time to open fresh positions, Markets are likely to be oversold and soon might turn upwards"


print(market_mood_index+"\n"+comment )





