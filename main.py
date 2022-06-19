import requests
from bs4 import BeautifulSoup
import datetime
import pandas as pd

url = "https://www.coingecko.com/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

table = soup.select("tbody tr")
time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

with open("crypto_data.csv", mode="a+") as file:
    header = "Name,Ticker,Current Price,24h Change,7d Change,Market Cap,Time\n"
    file.seek(0)
    if file.readline() != header:
        file.write(f"{header}")

    for i in range(10):
        name = table[i].a.text.split("\n")[1]
        ticker = table[i].span.text.split("\n")[1]
        mc = table[i].select("span")[-1].text.replace(",", "")
        seven_days_change = table[i].select("span")[-3].text
        twenty_four_h_change = table[i].select("span")[-4].text
        current_price = table[i].select("span")[-6].text.replace(",", "")
        content = f"{name},{ticker},{current_price},{twenty_four_h_change},{seven_days_change},{mc},{time}\n"
        file.write(content)


df = pd.read_csv("crypto_data.csv")
print(df)
    