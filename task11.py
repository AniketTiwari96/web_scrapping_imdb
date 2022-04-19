# print("task11 :")

# import json
# from pprint import pprint
# from task4 import scrape_movie_details

# with open("task1.json","r")as fobj:
#     d=json.load(fobj)
# movies=[]
# for i in range(10):
#     x=(scrape_movie_details(d[i]['urls']))
#     # pprint(x)
#     movies.append(x)
# # pprint(movies)

# def analyse_movies_genre(movies):
#     movie_genre={}
#     for i in movies:
#         # print(i)
#         for j in i["genre"]:
#             if j in movie_genre:
#                 movie_genre[j]+=1
#             else:
#                 movie_genre[j]=1
#     pprint(movie_genre)
# analyse_movies_genre(movies)