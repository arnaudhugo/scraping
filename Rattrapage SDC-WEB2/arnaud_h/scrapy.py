import re
from urllib2 import urlopen
from bs4 import BeautifulSoup as soup

# Url de la page contenant les 10 annonces les plus recentes
url = 'https://www.pap.fr/annonce/location-appartement-maison-ile-de-france-g471-a-partir-de-2-chambres'
html = urlopen(url)
content = html.read()
html.close()

page_soup = soup(content, "html.parser")

link_to_annonce = page_soup.findAll("div",{"class":"search-results-list"})
matches = re.findall('href="(.*?)"', str(link_to_annonce))
#file = open("file2.json", "w")
tmp = ""
for link in matches:
    if link.find("annonce/") == 1:
        if link != tmp:
            tmp = link
            #print(link)
            url_annonce = "https://www.pap.fr/" + link
            html2 = urlopen(url_annonce)
            content2 = html2.read()
            html2.close()
            page_soup2 = soup(content2, "html.parser")
            
            # Trouver le titre
            title = page_soup2.findAll("span",{"class":"h1"})
            if not title:
                print("no title")
            else:
                print(title[0].text.encode('utf-8'))
            # Trouver le numero
            num = page_soup2.findAll("strong",{"class":"tel-wrapper"})
            if not num:
                print("no num")
            else:
                print(num[1].text.strip().encode('utf-8'))

  #num = page_soup.findAll("strong",{"class":"tel-wrapper"})
  #title = page_soup.findAll("span",{"class":"h1"})
#price = page_soup.findAll("span",{"class":"item-price"})
#img = page_soup.findAll("img")
#desc = page_soup.findAll("div",{"class":"item-description margin-bottom-30"})
            
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
