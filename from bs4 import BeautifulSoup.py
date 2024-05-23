from bs4 import BeautifulSoup
import requests
import pandas as pd
url = "https://www.memc.com.sg/specialists/neurologists/"
page = requests.get(url)
soup = BeautifulSoup(page.text,"html.parser")

all_doctors= soup.find_all("li",class_="doc_name")
print(all_doctors)
#for names in all_doctors:
#    item ={}
#    item["Name"] = names.find("a")
#    print(item)