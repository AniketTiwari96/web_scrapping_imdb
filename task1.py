
# from textwrap import indent
# from bs4 import BeautifulSoup
# import requests,json
# import pprint
# url="https://www.imdb.com/india/top-rated-indian-movies/"
# page=requests.get(url)
# # print(page.text)
# soup=BeautifulSoup(page.text,'html.parser')
# # print(soup)

# def scrape_top_list():
#     man_div=soup.find('div',class_='lister')
# # yeh samajhane ke liye
#     # return man_div
# # print(scrape_top_list())
#     tbody=man_div.find('tbody',class_='lister-list')
# # agr ham tbody ko return karenge ko to tr milega gaa
# #     return tbody
# # print(scrape_top_list())
#     trs=tbody.find_all('tr')
# # agar ham trs body ko return karege to usaje andar data dikhai degaa
# #     return trs
# # print(scrape_top_list())

#     movis_rank=[]
#     movis_name=[]
#     year_of_realease=[]
#     movis_urls=[]
#     movis_rating=[]

#     for tr in trs:
#         position= tr.find('td',class_ ="titleColumn").get_text().strip()
# # yaha se movise ka position and movise name nikalenge
# #         return(position)
# # print(scrape_top_list())

#         rank=""
#         for i in position:
#             if '.' not in i:
#                 rank+=i
#             else:
#                 break
#         movis_rank.append(rank)
# # yaha se hame movise rank milegaa list me 
# #     return movis_rank
# # print(scrape_top_list())
        
#         title=tr.find('td',class_="titleColumn").a.get_text()
#         movis_name.append(title)
# # yaha se hame movise name mil jayegaa: 
# #         return movis_name
# # print(scrape_top_list())
         
#         year=tr.find('td',class_="titleColumn").span.get_text()
#         year_of_realease.append(year)
# # # yaha se ham sare movis ka year ko nikalenge:
# #     return year_of_realease
# # print(scrape_top_list())

#         rating=tr.find('td',class_='ratingColumn imdbRating').strong.get_text()
#         movis_rating.append(float(rating))
# # yaha se hame reting milti hai movies ki: 
# #     return movis_rating 
# # print(scrape_top_list())

#         link=tr.find('td',class_="titleColumn").a["href"]
#         movies_link="https://www.imdb.com"+link
#         movis_urls.append(movies_link)
# # # yaha se hame movies ka link milega: 
# #         return movis_urls
# # print(scrape_top_list())

#     top_movies=[]
#     details={'position':'','name':'','year':'','rating':'','urls':''}
#     for i in range(0,len(movis_rank)):
#         details['position']=int(movis_rank[i])
#         details['name']=str(movis_name[i])
#         year_of_realease[i]=year_of_realease[i][1:5]
#         details['year']=int(year_of_realease[i])
#         details['rating']=float(movis_rating[i])
#         details['urls']=movis_urls[i]
#         top_movies.append(details.copy())
#         details={'position':'','name':'','year':'','rating':'','urls':''}
#     return top_movies
# # pprint.pprint(scrape_top_list())
# a=scrape_top_list()

# with open("task1.json","w")as f:
#     json.dump(a,f,indent=4)
