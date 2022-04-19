print("task9")
from task4 import scrape_movie_details
import requests,json,os,random,time
from pprint import pprint
from bs4 import BeautifulSoup

with open ("task1.json","r")as fobj:
    d=json.load(fobj)

def scrape_movie_details(url):
    text=None
    file_name=url[27:-1]+".json"
    if os.path.exists("movie_details/"+file_name):
        f=open("movie_details/"+file_name)
        text=f.read()
        f.close()
        return text
    random_sleep=random.randint(1,3)
    if text is None:
        time.sleep(random_sleep)
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

        file1=open('movie_details/' + file_name,"w")
        raw=json.dumps(dct1)
        file1.write(raw)
        file1.close()
        return (dct1)
for i in d:
    url=i['urls']
    a=scrape_movie_details(url)
    with open ("task9.json","w")as fobj1:
        json.dump(a,fobj1,indent=4)



