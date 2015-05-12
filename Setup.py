#Setup script

from addomdb import addomdb
from getmovies import fill_from_dir, fill_from_file
import initialize as init

print('M > Initializing...')

init.init_linux()

print('M > Setting up database...')
raw_movies = []
newlib = init.newsession_linux()

# Indicate the location of folders containing the movies, append the movies in
# each folder to the list raw_movies

###To do, get year from folder or file title

print('M > Input folders containing your movies (in this case a movie is a'
' folder containing the video file or the video file itself)')

path = init.path_input('M > Indicate path to folder,'
' hit "Enter" to finish\n', '')

while path != '':
    fill_from_dir(raw_movies, path)
    path = init.path_input('M > Indicate path to folder,'
    'hit "Enter" to finish\n', '')

#Indicate a file containing a list of movies in the format
#
# title 1
# title 2, year 2

print('M > Indicate path to file with a list of Movies in the format: name,'
' year newline. The year entry is optional.')

path_file = init.path_input('M > Indicate path to file,'
'hit "Enter" to finish\n', '')

if path_file != '':
    fill_from_file(raw_movies, path_file)

#AddOmdb movies in raw_list

for movie in raw_movies:
    addomdb(newlib, movie, control=False, review=False)

print('M > Setup completed. Now run Movie_lib.py. Bye')
