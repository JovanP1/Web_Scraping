#Vpauto
import requests
from bs4 import BeautifulSoup
import pandas as pd
marques=[]
modeles =[]
prixs =[]
   
url='https://vpauto.fr/vehicule/resultats?page=2' 
page=requests.get(url) 
html=BeautifulSoup(page.text,'html.parser')              
modele=html.find_all('div',{'class':'elmt-modele'})       
modele=[x.getText() for x in modele]                     
modele=[x.replace('\n','') for x in modele]               
marque=html.find_all('div',{'class':'elmt-marque'})
marque=[x.getText() for x in marque]
marque=[x.replace('\n','') for x in marque]
prix=html.find_all('span',{'class':'prix'})
prix=[x.getText() for x in prix]
prix=[x.replace('€','') for x in prix]
d={'marque':marque,'modele':modele,'prix de vente':prix} 
cars=pd.DataFrame(data=d) 
