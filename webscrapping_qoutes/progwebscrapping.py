from bs4 import BeautifulSoup 
import requests

url = "https://en.wikipedia.org/wiki/Programming_languages_used_in_most_popular_websites"
url_data = requests.get(url)

#print(url_data)/
soup = BeautifulSoup(url_data.content, 'lxml')


print(soup.title)

table = soup.find("table", class_ ='wikitable sortable')
# table = soup.find_all("table",class_ = 'weikitable sortable')[1] if we need first table from entier website
# print(table)

# headers = table.find("thead/tr")
headers = table.find_all("th")
print(headers)

final_headers = []
for h in headers:
    final_headers.append(h.text.strip())

# print(final_headers)
table_rows = table.find_all('tr')
for tr in table_rows:
    table_data = tr.find_all("td")
    for td in table_data:
        print(td.text)




