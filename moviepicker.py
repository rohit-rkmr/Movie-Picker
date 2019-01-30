from imdb import IMDb
from random import randint
obj=IMDb()
top250 = obj.get_top250_movies()
c="y"
while c=="y" or c=="Y":
 num=randint(0,250)
 print(top250[num])
 c=input("Want to see something else(y/n)")

