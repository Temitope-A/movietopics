# To be called only by script (not directly from terminal due to current-dir
# not coherent).
#
# Input mode is flexible
#
#  AddOmdb(title,...)
#  AddOmdb(title,year,...)
#  AddOmdb([title,year],...)
#
# Mode 3 overrides mode 2
#
# Other options are control (default False) and review (default True)
# When control is True the movie found on Omdb is displayed to the user before
# adding it to the library. When review is true the user is prompted to review
# the movie immediately after the adding it.


def addomdb(library, title, year='null', control=False, review=True):
    from checklist import movie_in_lib
    from loadmovies import load_movie
    from urllib.request import urlopen
    import json
    import reviewmovies
    from names import current_dir

# Option 1 and 3

    try:
        title.replace('a', 'b')
    except:
        try:
            year = title[1]
            title = title[0]
        except:
            title = title[0]
# Option 2

    urltitle = title.replace(' ', '+')
    if year == 'null':
        f = urlopen('http://www.omdbapi.com/?t=' + urltitle)
    else:
        f = urlopen('http://www.omdbapi.com/?t=' + urltitle + '&y=' + str(year))

    s = f.read().decode()
    omdbres = json.loads(s)

    if omdbres['Response'] == 'False':
        print('M > {} was not found'.format(title))
        return

    year = omdbres['Released'].split()[-1]
    omdbtitle = omdbres['Title']

#Control sequence

    if control is True:
        flag = 0
        while flag == 0:
            res = input('M > I found this Movie: {}, {}. Is this what you are'
            ' looking for? Confirm with "y", abort with "n" or input '
            'year.'.format(omdbtitle, year))
            if res == 'y':
                flag = 1
            elif res == 'n':
                return
            else:
                try:
                    y = int(res)
                except:
                    print('M > Not a valid input')
                else:
                    f = urlopen('http://www.omdbapi.com/?t=' + title + 'y=' + y)
                    s = f.read().decode()
                    omdbres = json.loads(s)

                    year = omdbres['Released'].split()[-1]
                    omdbtitle = omdbres['Title']

        if omdbres['Response'] is 'False':
            print('M > "{}" was not found'.format(title))
            return

    director = omdbres['Director']
    imdbrating = omdbres['imdbRating']

# Check if Movie is already in the library

    check = movie_in_lib(omdbtitle, year, library)

    if check is True:
        print('M > "{}" is already in the library'.format(omdbtitle))
        return

# write Movie file

#    MyMovies=open(current_dir+'/MyMovies.txt','a')
    path = current_dir + '/Movies/' + omdbtitle + '(' + year + ').txt'
    f = open(path, 'w')

#    MyMovies.write(omdbtitle+', '+year+'\n')
#    MyMovies.close()

    f.write(omdbtitle + '\n')
    f.write(year + '\n')
    f.write(director + '\n')
    f.write(imdbrating + '\n\n')

    actors = omdbres['Actors'].split(', ')

    for actor in actors:
        f.write(actor + '\n')

    f.close()

    try:
        movie = load_movie(path)
    except:
        print(('M > There was a problem loading the recently added {}.'
        ' Check the file in the library'.format(omdbtitle)))
    else:
        if review is True:
            reviewmovies.review(movie)
            movie = load_movie(path)
        library.append(movie)

        print('M > "{}" was added to your library'.format(omdbtitle))
    return


def addbatch(library):

    from getmovies import fill_from_dir, fill_from_file
    import initialize as init

    raw_movies = []

# Indicate the location of folders containing the movies, append the movies in
# each folder to the list raw_movies

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
        addomdb(library, movie, control=False, review=False)

    return