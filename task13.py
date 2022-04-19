print("task13")
from task4 import scrape_movie_details
from task12 import scrape_movie_cast
import json,os
from pprint import pprint

with open("task1.json","r") as p:
    d=json.load(p)


def get_movie_list_details(movies):
    text=None
    file_name=d[0]['url'][28:-1]+"_cast.json"
    # print(file_name)
    if os.path.exists("cast_details/"+d[0]['url'][22:-1]+"cast.json"):
        f=open("cast_details"+file_name)
        text=f.read()
        return text
    if text is None:
        x=scrape_movie_details(movies)
        y=d[0]['url']+"fullcredits?ref=ttcl_sm#cast"
        z=scrape_movie_cast(y)
        x["cast"]=z
        file1=open('cast_details/' + file_name,"w")
        raw=json.dumps(x)
        file1.write(raw)
        file1.close()
        return (x)
m=get_movie_list_details(d[0]['url'])
pprint(m)

