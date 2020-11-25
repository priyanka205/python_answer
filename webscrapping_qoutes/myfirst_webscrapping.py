from bs4 import BeautifulSoup
import requests
import csv

source = requests.get("http://quotes.toscrape.com/").text
soup = BeautifulSoup(source,'lxml')# to make fine lxml
# print(soup.prettify())
# exit()
# print(soup.prettify())
file =  open('quote1.txt','w', encoding="utf-8")
csv_writer = csv.writer(file)
csv_writer.writerow(["quote \t author \t tags"])

quote = soup.find_all('div',{'class':'quote'})# soup.find_all is to find all,soup.find is find particular
for q in quote:
    required_quote = q.find('span',{'class':'text'}).text
    author = q.find('small',{'class':'author'}).text
    tags = q.find('div',{'class':'tags'})
    t = tags.find_all('a')
    required_tags = []
    for tag in t:
        required_tags.append(tag.text)
    tags_joined = " ".join(required_tags)
    row_to_write = [str(required_quote) + "\t" + str(author) + "\t" + str(tags_joined)]
    csv_writer.writerow(row_to_write)
    print(row_to_write)#to see on terminal

file.close()
# print(row_to_write) to print just a line