# Ce code permet de Filtrer les df et les rassembler
# Importer la librairies os qui permet d'importer de montrer le chemin des fichiers qu'on va importer par la suite
import os
os.getcwd()
os.chdir("C:\\Users\\jovan\\Desktop\\M1 ecotr\\Langage de programmation 1\\Web scraping\\csv files")
import pandas as pd
# Importer les données 
# sep = " ; " permet de séparer les colonnes de la data frame par colonnes du fichier csv
cars_df = pd.read_csv("LaCentrale.csv",sep=";")
vpauto_df=pd.read_csv("vpauto.csv",sep=";")
carizy_df = pd.read_csv("carizy.csv",sep=";")
# On retire la marque de chaque element de la colonne modele et on la met dans la colonne marque
cars_df[['Marques','Modeles']] = cars_df["Modeles"].str.split(" ", n = 1, expand = True) 
cars_df = cars_df[['Marques','Modeles','Prix','Liens']]
# Nettoyer carizy
def filtrer_to_float (s):
    s=s.replace(" ","")
    s=float(s)
    return s
carizy_df['Prix']=list(map(filtrer_to_float,carizy_df['Prix']))

# Supprimer les données manquantes
carizy_df = carizy_df.dropna()
# Rassembler la centrale, vpauto et carizy en une seule data frame 
allcars_df= pd.concat([cars_df, vpauto_df, carizy_df])

# L'exporter en csv 
allcars_df.to_csv(r'C:\Users\jovan\Desktop\M1 ecotr\Langage de programmation 1\Web scraping\csv files\Allcars.csv',index = None, header=True,sep=";")
