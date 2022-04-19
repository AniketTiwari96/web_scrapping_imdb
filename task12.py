print("task12")
import requests,json
from bs4 import BeautifulSoup
from pprint import pprint


with open ("task1.json","r")as fobj:
    d=json.load(fobj)

def scrape_movie_cast(movies_cast):
    cast=requests.get(movies_cast)
    soup=BeautifulSoup(cast.text,"html.parser")
    info=soup.find("table",class_="cast_list")
    cast1=info.find_all("tr")

    imdb_lst=[]
    for i in cast1:
        td=i.find("td",class_="")

        if td != None:
            cest_dct={}
            name=td.find("a").text
            # ya ham log a tag kin jagah par khali tag bhi likh sakte hai 
            # name=td.find(class_="").text
            imdb_id=td.find("a")["href"][6:15]

            cest_dct["name"]=name.strip()
            cest_dct["imdb_id"]=imdb_id

            imdb_lst.append(cest_dct)
    return imdb_lst

x=scrape_movie_cast(d[0]['urls']+"fullcredits?ref=ttcl_sm#cast")
# pprint(x)
with open("task12.json","w")as fobj:
    json.dump(x,fobj,indent=4)
