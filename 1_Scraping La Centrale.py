# Importer pandas pour utiliser les dataFrames
# Importer selenium pour le webscraping
# Importer Options pour pouvoir scraper sans ouvrir les pages web
import pandas as pd
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options

#Nous commençons par créer une liste avec 55 marques 'connues' qui sevieront à changer le lien du site Lacentrale et des listes vides où l'on mettera les données scrapés après.
marques_index=["ABARTH","BMW","MERCEDES","CITROEN","OPEL","VOLKSWAGEN","RENAULT","HYUNDAI","FORD","PEUGEOT","DACIA","NISSAN","AUDI","TOYOTA","MERCEDES-BENZ","SKODA","ISUZU","MAZDA","FIAT","HONDA","ALFA ROMEO","MINI","SUZUKI","KIA","SAAB","CHEVROLET","SEAT","MITSUBISHI","LAND ROVER","JEEP","MAN","CHRYSLER","FERRARI","VOLVO","PORSHCE","ASTON MARTIN","BENTLEY","BUGATTI","CADILLAC","CHEVROLET USA","DAEWOO","DODGE","JAGUAR","LADA","LANCIA","LEXUS","LOTUS","TESLA","SMART","INFINITY","SUBARU","ROLLS ROYCE","MASERATI","MAYBACH","MC LAREN"]
modeles=[]
prix=[]
hrefs =[]
# Boucle principale qui permet de scrapper les prix et liens de toutes les voitures de marques indiquées dans la liste précedemment
for v in marques_index :
    #options.headless permet de scraper sans ouvrir de page web (plus rapide)
    #window size permet d'éviter des problèmes de taille de la page web (des fois il trouve pas l'element web si la page est trop petite)
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(options=options)
    driver.set_window_size(1440, 900)
    # definir la page web qu'on va scrapper. Ici c'est à l'interieur d'une boucle donc il va scrapper toutes les marques dans la liste à l'aide de v
    # .lower() est utilisé pour mettre les marques en miniscule car elle est de base en miniscule dans le site
    url = "https://www.lacentrale.fr/occasion-voiture-marque-"+v.lower()+".html"
    # driver.get permet d'ouvrir le lien mentionnée entre parenthèses
    driver.get(url)
    # nous avons inspecter la page web, on a découvert que les noms des modèles sont écrites en html dans la classe:"brandModel"
    # les prix sont dans la classe:"fieldPrice" et les liens sont dans l'attribut href.
    # find_elemnts_by_class_name permet de trouver les éléments web par leur nom de classe
    # nous avons utiliser by_class_name aulieu de by_xpath ici car les xpath des voitures dans la liste ne sont pas ordonnées, ce qui rend difficile les scraper
    
    modeles_elm = driver.find_elements_by_class_name("brandModel")
    prix_elm = driver.find_elements_by_class_name("fieldPrice")
    href_elm = driver.find_elements_by_class_name("linkAd")
    
    # après avoir créé 3 listes contenant les webelements des modele,des prix et des lien
    # Nous allons procéder à prendre les textes de chaque webelement pour modeles et prix, et les hrefs de chaque webelement pour les liens
    for i in range(len(modeles_elm)):
        hrefs.append(href_elm[i].get_attribute('href'))
        modeles.append(modeles_elm[i].text)
        prix.append(prix_elm[i].text)
        
      
# Partie manipulation de données et filtrage 
# Nous avons rassemblé les listes en data frame, La colonne modeles contient les marques et les modeles
cars_df = pd.DataFrame({'Modeles':modeles,'Prix':prix,'Liens':hrefs})

# Dans cette partie nous avons transformé les prix en float car ils étaient en string (chaines de caractères)
# Pour ce faire nous avions besoin de filtrer ce qui se trouve dans les variables prix, à savoir le symbole € et des éspaces

def filtrer_to_float (s):
    s=s.replace("€","")
    s=s.replace(" ","")
    s= float(s)
    return s


cars_df = pd.DataFrame({'Modeles':modeles,'Prix':list(map(filtrer_to_float,prix)),'Liens':hrefs})
# On retire la marque de chaque element de la colonne modele et on la met dans la colonne marque:
cars_df[['Marques','Modeles']] = cars_df["Modeles"].str.split(" ", n = 1, expand = True) 
cars_df = cars_df[['Marques','Modeles','Prix','Liens']]
# Exporter la Df to csv
cars_df.to_csv(r'C:\Users\mehdi\Desktop\M1 ecotr\Langage de programmation 1\Web scraping\csv files\LaCentrale.csv',index = None, header=True,sep=";")


