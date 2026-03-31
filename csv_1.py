'''
import csv

datne=open("kontakti.csv","r",encoding="utf-8")
dati=list(csv.reader(datne))
datne.close()
print(dati)
'''
'''
import pyjokes
import pyfiglet
import cowsay

joks=pyjokes.get_joke()
parv=pyfiglet.figlet_format(joks,font="bubble")

print(cowsay.ghostbusters(parv))
'''
import csv

datne=open("kontakti.csv",encoding="utf-8")
saturs=list(csv.reader(datne))#parveido par sarakstu
datne.close()
print(saturs)

#izvade pa 1nam
for c in saturs:
   print(c[0],"\t",c[-2])

galvene=["vārds", "uzvārds", "telefons","pilsēt"]
#saglabašana
with open("k1.csv","w",encoding="utf-8",newline="") as fails:
    c=csv.writer(fails)
    c.writerow(galvene)
    c.writerows(saturs)

print(galvene,"\t",saturs)








