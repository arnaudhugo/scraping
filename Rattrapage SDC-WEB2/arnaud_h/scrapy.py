import re
import datetime
from urllib2 import urlopen
from bs4 import BeautifulSoup as soup

# Url de la page contenant les 10 annonces les plus recentes
url = 'https://www.pap.fr/annonce/location-appartement-maison-ile-de-france-g471-a-partir-de-2-chambres'
html = urlopen(url)
content = html.read()
html.close()
page_soup = soup(content, "html.parser")

# Recuperer tout les liens vers les 10 annonces les plus recentes
link_to_annonce = page_soup.findAll("div",{"class":"search-results-list"})
matches = re.findall('href="(.*?)"', str(link_to_annonce))

# Nommer le fichier json de la date_heure du scaping
now = datetime.datetime.now()
name_file = now.strftime("%Y-%m-%d_%H-%M")

file = open(name_file + ".json", "w")
file.write("{\n")
tmp = ""
for link in matches:
    if link.find("annonce/") == 1:
        if link != tmp and link.split("-")[12][0] == "r":
            tmp = link
            url_annonce = "https://www.pap.fr/" + link
            html2 = urlopen(url_annonce)
            content2 = html2.read()
            html2.close()
            page_soup2 = soup(content2, "html.parser")

            # Numero annonce (format : rXXXXXXXXX)
            file.write("\t\"" + link.split("-")[12] + "\": {\n")
            
            # Trouver le titre
            title = page_soup2.findAll("span",{"class":"h1"})
            if not title:
                file.write("\t\t\"titre\": \"" + "no title" + "\",\n")
                print("no title")
            else:
                file.write("\t\t\"titre\": \"" + title[0].text.encode('utf-8') + "\",\n")
                print(title[0].text.encode('utf-8'))

            # Trouver le numero
            num = page_soup2.findAll("strong",{"class":"tel-wrapper"})
            if not num:
                file.write("\t\t\"numero\": \"" + "no num" + "\",\n")
                print("no num")
            else:
                file.write("\t\t\"numero\": \"" + num[1].text.strip().encode('utf-8') + "\",\n")
                print(num[1].text.strip().encode('utf-8'))

            # Trouver le prix
            price = page_soup2.findAll("span",{"class":"item-price"})
            if not price:
                file.write("\t\t\"prix\": \"" + "no price" + "\",\n")
                print("no price")
            else:
                file.write("\t\t\"prix\": \"" + price[0].text.encode('utf-8') + "\",\n")
                print(price[0].text.encode('utf-8'))

            # Trouver la description
            desc = page_soup2.findAll("div",{"class":"item-description margin-bottom-30"})
            if not desc:
                file.write("\t\t\"desc\": \"" + "no description" + "\",\n")
                print("no description")
            else:
                file.write("\t\t\"desc\": \"" + desc[0].div.p.text.strip().encode('utf-8').replace('\n',' ').replace('\r','') + "\",\n")
                print(desc[0].div.p.text.strip().encode('utf-8').replace('\n',' ').replace('\r',''))

            # Trouver la/les photo(s)
            img = page_soup2.findAll("img")
            file.write("\t\t\"images\": {\n")
            if not img:
                file.write("\t\t\"image1\": \"" + "no image" + "\",")
                print("no image")
            else:
                var = 0
                for image in img:
                    photo = str(image).split("\"")[3]
                    if photo.split(":")[0] == "https":
                        var = var + 1
                        file.write("\t\t\"image" + str(var) + "\": \"" + photo.encode('utf-8') + "\",\n")
            
            file.write("\t},\n")
file.write("}\n")
file.close()
