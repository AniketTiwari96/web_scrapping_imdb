print("task4: ")
import requests, json
from bs4 import BeautifulSoup
from pprint import pprint

def scrape_movie_details(url):
    dct1={}
    page=requests.get(url)
    soup=BeautifulSoup(page.text,'html.parser')
    name=soup.find("h1", attrs={"data-testid":"hero-title-block__title"}).text
    dct1["name"]=name

    lst=[]
    director_name=soup.find("div",class_="ipc-metadata-list-item__content-container")
    x=director_name.find_all("li",class_="ipc-inline-list__item")
    for i in x:
        lst.append(i.a.get_text())
        dct1["director"]=lst

    lst1=[]
    language_name=soup.find("li",attrs={"data-testid":"title-details-languages"})
    x1=language_name.find_all(class_="ipc-inline-list__item")
    for i in x1:
        lst1.append(i.a.get_text())
        dct1["language"]=lst1

    country_name=soup.find("li",attrs={"data-testid":"title-details-origin"}).find("a").text
    dct1["country_name"]=country_name

    poster_image_url=soup.find("img",class_="ipc-image")["src"]
    dct1["poster_image_url"]=poster_image_url

    bio=soup.find("span",attrs={"data-testid":"plot-xs_to_m"}).text
    dct1["bio"]=bio

    genre=soup.find("li",attrs={"data-testid":"storyline-genres"})
    Genre=genre.find_all("a")
    lst2=[]
    dct1["genre"]=lst2
    for i in Genre:
        l=i.text
        lst2.append(l)

    # print(lst2

    run_time=soup.find("li",attrs={"data-testid":"title-techspec_runtime"}).text.strip("Runtime")
    w=run_time.split(" ")
    # print(w)
    if len(w)==4:
        m=int(w[0])*60+int(w[2])
    else:
        m=int(w[0])*60
    dct1["runtime"]=m
    return (dct1)

a=scrape_movie_details("https://www.imdb.com/title/tt0986264/")
with open("task4.json","w") as p:
    json.dump(a,p,indent=4)

