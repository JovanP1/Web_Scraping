# Le but de cette partie est de créer une interaction avec le client qui profitera de notre base de données
# L'interaction consiste à demander au client d'insérer des marques et un budget, ensuite le code cherchera les voitures de ces marques spécifiées disponibles
# dans notre base de donnée à un prix inférieur à son budget (avec les liens directs vers le site pour les acheter).
# le code spécifiera aussi le nombre d'autres voitures de la même marques choisie par le client mais à un prix supérieur à son budget.

# Importer la librairies os qui permet d'importer de montrer le chemin des fichiers qu'on va importer par la suite
import os
os.getcwd()
os.chdir("C:\\Users\\jovan\\Desktop\\M1 ecotr\\Langage de programmation 1\\Web scraping\\csv files")
import pandas as pd

# Importer les données 
# sep = " ; " permet de séparer les colonnes de la data frame par colonnes du fichier csv
allcars=pd.read_csv("Allcars.csv",sep=";")

# Partie interaction avec le client
# On commence par définir des listes vides qu'on va utiliser par la suite
marques_available = []
modeles_available=[]  
prix_available=[] 
liens_available=[] 
# la fonction input de python permet à l'utilisateur du pc d'intéragir avec le code. elle mettera en mémoire ce qui a été écrit dans une variable.
client_marques = input("Choisissez des marques :  ").upper()
# Cette partie permet de corriger la variable. si l'utilisateur a laisser un éspace à la fin des marques choisies, ce code le supprimera.
if client_marques[-1:]== " ":
    client_marques = client_marques.replace(client_marques[-1:],"")
client_marques = client_marques.split(" ")
# même fonction (input) pour prendre le budget du client cette fois
# try except est utilisé pour envoyer une exception si le code n'arrive pas à transformer ce qu'il a été écrit en float.
# Il affichera le cas échéant le deuxième message qui demande d'écrire le budget en numérique. Le replace est utilisé pour éliminer les espaces.
try:       
    client_budget = float(input("Inserez votre budget : ").replace(" ",""))
except :
   client_budget = float(input("Veuillez inserer votre budget en numerique: ").replace(" ",""))

# Cette partie permet de retirer les éléments de notre base de données qui corréspondent aux critères mentionnées par le client, à savoir marques et budget
# On commence par définir une liste vide, chaque élément de cette liste montrera le nombre de voitures à marque précisée par le client qui ont un prix supérieure à son budget 
p = []
# on crée une premiere boucle qui retirera chaque marque précisée par le client
for i in range(len(client_marques)):
    # on prédéfinit une variable qu'on utilisera comme compteur
    k = 0
    # Cette deuxième boucle permet de comparer la marque retiré de la liste des marques précisées par le client pour le comparer avec toutes les marques qu'on a dans la data frame
    for j in range(len(allcars['Marques'])):
        # cette conndition permet de comparer la marque retirée avec les voitures disponibles et comparer le budget avec le prix de ces voitures disponibles
        if client_marques[i] in allcars['Marques'][j] and client_budget >= allcars['Prix'][j]:
            # si la condition est réspectée le code qui suit permet de rajouter la voiture j, son prix et son lien direct à des listes prédifinies avant
            marques_available.append(allcars['Marques'][j])
            modeles_available.append(allcars['Modeles'][j])
            prix_available.append(allcars['Prix'][j])
            liens_available.append(allcars['Liens'][j])
        # cette condition permer de comptes les voitures à marques choisie qui ont un prix supérieure ua budget du client
        elif client_marques[i] in allcars['Marques'][j] and client_budget < allcars['Prix'][j]:          
            k +=1      
    # On rassemble le nombre de voitures qui réspectent la deuxième condition dans cette liste qu'on utilisera juste après
    p.append(k)
# Cette boucle-condition permet de dire au client combien de voitures à marques choisies ont un prix supérieure à son budget,
# s'il veut eventuellement augmenter son budget pour voir les nouvelles voitures disponibles
for z in range(len(client_marques)):    
    if p[z] > 0:
        print("On retrouve "+str(p[z])+" autres "+client_marques[z]+" mais à plus de "+str(client_budget)+" €")

# cette partie permet de tout rassembler dans une data-frame pour bien présenter les voitures disponibles (marque-prix-lien)    
cars_available = pd.DataFrame({'Marques Disponible':marques_available,'Modeles Disponible':modeles_available,'Prix':prix_available,'Liens':liens_available})

print(cars_available)
