from bs4 import BeautifulSoup 
import requests

url = "https://en.wikipedia.org/wiki/Programming_languages_used_in_most_popular_websites"
url_data = requests.get(url)

#print(url_data)/
soup = BeautifulSoup(url_data.content, 'lxml')


print(soup.title)

print(soup.find("class"='wikitable sortable'))