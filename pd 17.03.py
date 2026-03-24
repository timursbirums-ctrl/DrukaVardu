'''
pilsetas=['pilsetas1', 'pilsetas2', 'pilsetas3', 'pilsetas4', 'pilsetas5']
pilsetas1=input("ievadi pilsetu: ")
pilsetas2=input("ievadi pilsetu: ")
pilsetas3=input("ievadi pilsetu: ")
pilsetas4=input("ievadi pilsetu: ")
pilsetas5=input("ievadi pilsetu: ")

V_pilsetas=["Ventspils", "Liepāja", "Rēzekne"]

abc=V_pilsetas.sort()
print(abc)
file=("pilsetas.txt", "w", encodings="utf-8")
'''
'''
import json 

f=open("uzd.json","r+")
skaitli=[1,2,3,4,1]

json.dump(skaitli,f)
f.close()
f=open("uzd.json","r+")
dati=json.load(f)
print(dati)

'''
'''
import re

text="mans telefona numurs ir 12345678"

atbilde=re.search(r"\d{8}",text)
print(atbilde.group())

atbilde2=re.findall(r"\d{8}",text)
print(atbilde2)

atbilde3=re.search(r"\btelefona",text)
print(atbilde3.group())

atbilde4=re.sub(r"\b\d{8}\d","telefona nr.",text)
print(atbilde4.)
'''
'''
import re
datne=open("re.txt",encoding="utf-8")
dati=datne.read()
datne.close()
print(type(dati))
atbilde1=re.findall(r"\blaimests|bezmaksas|bankas konts\b",text,re.IGNORECASE)
print(atbilde1)
'''
import re
with open("klienti.txt","r",encoding="utf-8") as datne:
    dati=datne.read()#virkne

epasti=re.findall(r"\w+@\w+\.\w+",dati)
print(epasti)#saraksts
print(len(epasti))

telefoni=re.findall(r"\b\d{8}\b",dati)
print(telefoni)

a=re.sub(r"\d{8}","📞",dati)
print(a)

datne=open("klienti_anon.txt","w",encoding="utf-8")
datne.close()
s
















