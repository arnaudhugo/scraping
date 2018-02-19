from urllib2 import urlopen
from bs4 import BeautifulSoup as soup

#url = 'https://www.pap.fr/annonce/vente-appartement-immeuble-maison-ile-de-france-g471-r420501087'
url = 'https://www.pap.fr/annonce/vente-appartement-immeuble-maison-ile-de-france-g471-r420500973'

html = urlopen(url)
content = html.read()
html.close()

page_soup = soup(content, "html.parser")

num = page_soup.findAll("strong",{"class":"tel-wrapper"})
title = page_soup.findAll("span",{"class":"h1"})
price = page_soup.findAll("span",{"class":"item-price"})
img = page_soup.findAll("img")

print(num[1].text.strip())
print(title[0].text)
print(price[0].text)
print(img[2])

#f = open("test.txt", "w")
#content = html.read()
#f.write(num[0])
#f.close()
