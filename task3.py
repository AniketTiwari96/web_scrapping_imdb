print("task3")
from pprint import pprint
import json
from bs4 import BeautifulSoup

with open("task2.json","r")as fobj:
    r=json.load(fobj)

def group_by_decade(movies):
    moviedec={}
    list1=[]
    for index in movies:
        mod = int(index) % 10
        decade =int(index)-mod
        if decade not in list1:
            list1.append(decade)
    list1.sort()
    for i in list1:
        moviedec[i]=[]
    for i in moviedec:
        dec10=i+9
        for x in movies:
            if int(x)<=dec10 and int(x)>=i:
                # print(x)
                for v in movies[str(x)]:
                    moviedec[i].append(v)
    return (moviedec)
x=(group_by_decade(r))
with open("task3.json","w") as p:
    json.dump(x,p,indent=4)


