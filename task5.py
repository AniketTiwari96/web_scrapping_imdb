print("task5")
import json,requests
from bs4 import BeautifulSoup
from pprint import pprint
from task4 import scrape_movie_details
with open ("task1.json")as fobj:
    d=json.load(fobj)
q=1
movies=[]
for i in range(10):
    movies.append(d[i]["urls"])
    # print(q,movies)
    q+=1
def get_movie_list_details(movies):
    movies_details=[]
    for i in movies:
        movies_details.append(scrape_movie_details(i))
    return movies_details

a=get_movie_list_details(movies)
with open("task5.json","w")as fobj:
    json.dump(a,fobj,indent=4)