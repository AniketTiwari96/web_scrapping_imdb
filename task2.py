# print("my task2")
# import json
# from pprint import pprint
# with open("task1.json","r")as fobj:
#     d=json.load(fobj)
# def group_by_year(movies):
#     years=[]
#     for i in movies:
#         year=i["year"]
#         if year not in years:
#             years.append(year)
#     movie_dct={i:[]for i in years}
#     for i in movies:
#         year=i['year']
#         for x in movie_dct:
#             if str(x) == str(year):
#                 movie_dct[x].append(i)
#                 # print(movie_dct)
#     return movie_dct
# p=(group_by_year(d))
# with open("task2.json","w")as fobj:
#     json.dump(p,fobj,indent=4) 


# print("akash task2: ")
# import json,requests
# from bs4 import BeautifulSoup
# from pprint import pprint

# with open("task1.json","r") as p:
#     d=json.load(p)
# def group_by_year():
#     dic={}
#     for i in d:
#         year=i['year']
#         movie_year=[]
#         for y in range(len(d)):
#             if year==d[y]['year']:
#                 movie_year.append(d[y])
#         dic[year]=movie_year
#     return dic

# x=(group_by_year())
# with open("task2.json","w") as p:
#     json.dump(x,p,indent=4)  
# 



