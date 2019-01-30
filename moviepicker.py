from imdb import IMDb
from random import randint
obj=IMDb()
top250 = obj.get_top250_movies()
c="y"
while c=="y" or c=="Y":
 num=randint(0,250)
 movie=str(top250[num])
 print(movie)
 result = obj.search_movie(movie)
 movdat = result[0]
 obj.update(movdat)
 print("Rating : ",movdat['rating'])
 print("Genre : ",movdat['genre'])
 for director in movdat['directors']:
    print("Director : ",director['name'])
 print("Runtime : ",movdat['runtime'],"min")
 c=input("Want to see something else(y/n)")

