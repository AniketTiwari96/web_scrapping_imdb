# print("task 10: ")
# import requests,json,os
# from bs4 import BeautifulSoup
# from pprint import pprint
# from task4 import scrape_movie_details
# from task5 import get_movie_list_details

# with open ("task1.json","r")as fobj:
#     d=json.load(fobj)
#     # pprint(d)
# movies=[]
# for i in range(10):
#     movies.append(d[i]["urls"])
#     # pprint(movies)

# def analyse_language_and_directors(movies):
#     director_dct={}
#     movies_lst=[]
#     for i in movies:
#         movie_list=scrape_movie_details(i)
#         movies_lst.append(movie_list)
#         # pprint(movies_lst)
#     director=[]
#     for i in movies_lst:
#         for j in i['director']: 
#             director.append(j)
#     # pprint(director)
#     for d in director:
#         # pprint(d)
#         language={}
#         for new in movies_lst:
#             if d in new['director']:
#                 for lang in new["language"]:
#                     if lang not in language:
#                         language[lang]=1
#                     else:
#                         language[lang]+=1
#         # print(language)
#         director_dct[d]=language
#         # print(director_dct)
#     return director_dct
# x=analyse_language_and_directors(movies)
# with open("task10.json","w")as fobj:
#     json.dump(x,fobj,indent=4)

