from bs4 import BeautifulSoup
import requests

url = "https://www.newegg.com/asus-geforce-rtx-3070-ti-tuf-rtx3070ti-o8g-gaming/p/N82E16814126512"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

prices = doc.find_all(text="$")
parent = prices[0].parent
strong = parent.find("strong")
print(strong.string)