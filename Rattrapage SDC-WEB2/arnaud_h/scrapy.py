import sys
import re
from urllib2 import urlopen
from bs4 import BeautifulSoup as soup

#url = 'https://www.pap.fr/annonce/vente-appartement-immeuble-maison-ile-de-france-g471-r420501087'
#url = 'https://www.pap.fr/annonce/vente-appartement-immeuble-maison-ile-de-france-g471-r420500973'
# https://www.pap.fr/annonce/location-appartement-maison-ile-de-france-g471-a-partir-de-2-chambres
url = sys.argv[1]

html = urlopen(url)
content = html.read()
html.close()

page_soup = soup(content, "html.parser")

#num = page_soup.findAll("strong",{"class":"tel-wrapper"})
#title = page_soup.findAll("span",{"class":"h1"})
#price = page_soup.findAll("span",{"class":"item-price"})
#img = page_soup.findAll("img")
#desc = page_soup.findAll("div",{"class":"item-description margin-bottom-30"})

link_to_article = page_soup.findAll("div",{"class":"search-results-list"})
matches = re.findall('href="(.*?)"', str(link_to_article))
tmp = ""
for link in matches:
    if link.find("annonce/") == 1:
        if link != tmp:
            tmp = link
            print(link)

#file = open("file2.json", "w")

#file.write("{\n\"recherche\": {\n\t\"titre\": \"" + title[0].text.encode('utf-8') + "\", \n\t\"numero\": \"" + num[1].text.strip().encode('utf-8') + "\", \n\t\"prix\": \"" + price[0].text.encode('utf-8') + "\", \n\t\"desc\": \"" + desc[0].div.p.text.strip().encode('utf-8').replace('\n',' ').replace('\r','') + "\",\n\t\"images\": {\n")

#var = 0
#for image in img:
#    photo = str(image).split("\"")[3]
#    if photo.split(":")[0] == "https":
#        var = var + 1
#        file.write("\t\t\"image" + str(var) + "\": \"" + photo.encode('utf-8') + "\",\n")

#file.write("\t}\n}}\n")
#file.close()
