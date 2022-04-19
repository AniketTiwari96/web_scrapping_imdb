# print("task6")
import json
from bs4 import BeautifulSoup
from pprint import pprint
from task5 import get_movie_list_details

with open("task5.json","r")as fobj:
    d=json.load(fobj)
    # print(d)
def analyse_movies_language():
    dct={}
    for i in d:
        for j in i["language"]:
            if j in dct:
                dct[j]+=1
            else:
                dct[j]=1
    return dct
a=analyse_movies_language()
with open ("task6.json","w")as fobj:
    json.dump(a,fobj,indent=4)



