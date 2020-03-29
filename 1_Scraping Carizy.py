#CARIZY
  
from selenium import webdriver
import pandas as pd

modeles=[] 
marques=[]
prixs=[]
liens=[]
for i in range (1,35): 
    driver = webdriver.Chrome()  
    driver.get("https://www.carizy.com/voiture-occasion?q=&hPP=21&idx=CarAlgoliaIndex_prod&p="+str(i))  
    
    for j in range(1,21): 

        modele_element = driver.find_elements_by_xpath('//*[@id="hits-container"]/div/div['+str(j)+']/div/div/div[14]/div/div[1]/div[2]')[0]
        prixvoiture_element = driver.find_elements_by_xpath('//*[@id="hits-container"]/div/div['+str(j)+']/div/div/div[14]/div/div[2]/p[2]')[0]
        marque_element=  driver.find_elements_by_xpath('//*[@id="hits-container"]/div/div['+str(j)+']/div/div/div[14]/div/div[1]/a/h2')[0]
        liens_element =driver.find_elements_by_xpath('//*[@id="hits-container"]/div/div['+str(j)+']/div/div/div[14]/div /div[1]/a')[0]
        marques.append(marque_element.text)
        modeles.append(modele_element.text)
        prixs.append(prixvoiture_element.text)
        liens.append(liens_element.get_attribute('href'))
carizy= pd.DataFrame({'Marques':marques,'Modeles':modeles,'Prix':prixs,'Liens':liens}) 


for z in range(len(carizy['Prix'])):
        carizy['Prix'][z]=carizy['Prix'][z].replace("€","")
   
carizy.to_csv(r'C:\Users\X1 CARBIN\Desktop\python\carizy.csv',index=None,header=True,sep=";")  
