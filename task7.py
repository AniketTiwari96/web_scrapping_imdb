print("task7")
import json
from bs4 import BeautifulSoup
from pprint import pprint
from task4 import scrape_movie_details

with open("task5.json","r")as fobj:
    d=json.load(fobj)

def analyse_movies_director():
    dct={}
    for i in d:
        for j in i["director"]:
            if j in dct:
                dct[j]+=1
            else:
                dct[j]=1
    return dct
a=analyse_movies_director()
with open ("task7.json","w")as fobj:
    json.dump(a,fobj,indent=4)
