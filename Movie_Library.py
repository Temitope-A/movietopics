import sys
import initialize as init
import addomdb as add
import reviewmovies as review
import dbconnector as db


def print_menu(menu):
    print('M > What do you want to do? Select the number corresponding to'
    ' the desired action\n')
    print('|=======Menu=======|')
    for i in range(0, 8):
        print(i, menu[i])
    print('|==================|')


def print_unrated(library):
    index = 1
    print('============Unrated Movies============')
    for movie in library:
        if movie.reviewed == 0:
            print(index, movie.title, movie.year)
        index += 1
    print('======================================')


def print_all(library):
    index = 1
    print('==============Library=================')
    for movie in library:
        print(index, movie.title, movie.year)
        index += 1
    print('======================================')


print('M > Loading library...')
library = init.newsession_linux()
library.sort(key=lambda movie: movie.title)

if library == 'runsetup':
    sys.exit()

#Library is loaded
print('M > Library loaded')

menu = ('View library', 'Add single movie', 'Add Movies from folder or file',
     'Review single movie', 'Review all unreviewed movies',
     'Sync library', 'Search Movies', 'Quit')

choice = '0'

while choice != '7':
    print_menu(menu)
    print('')
    choice = input('M < Input: ')

# Choice 0: View library
    if choice == '0':
        print_all(library)

# Choice 1: Add single movie
    elif choice == '1':
        title = input('M < Input title: ')
        year = input('M < Input year.( Hit Enter to pass): ')
        try:
            y = int(year)
        except:
            add.addomdb(library, title, control=True, review=True)
        else:
            add.addomdb(library, title, year, control=True, review=True)

# Choice 2: Add Movies from folder or file
    elif choice == '2':
        add.addbatch(library)

# Choice 3: Review single movie
    elif choice == '3':
        print_unrated(library)
        print('M > Chose the index of the movie you want to review')
        x = input('M < Input: ')
        try:
            index = int(x)
        except:
            print('M > Invalid input')
        else:
            try:
                movie = library[index - 1]
            except:
                print('M > Input out of range')
            else:
                print('M > Reviewing "{}"'.format(movie.title))
                review.review(library[index - 1])

#Choice 4: Review all unreviewed movies
    elif choice == '4':
        n = len(library)
        for i in range(0, n):
            if library[i].reviewed == 0:
                print('M > Next to be reviewed: "{}". Hit Enter to continue,'
                '"p" to pass to next movie; any other input '
                'will stop the process'.format(library[i].title))
                x = input('M < Input: ')
                if x == '':
                    review.review(library[i])
                elif x == 'p':
                    pass
                else:
                    break

#Choice 5: Sync library
    elif choice == '5':
        username = input('M < Username: ')
        password = input('M < Password: ')
        db.sync(library, username, password)

#Choice 6: Search Movies
    elif choice == '6':
        pass

# Quit
    elif choice == '7':
        pass

# Any other input
    else:
        print('M > Your input was not recognized.')


#closing operations
print('M > Bye')

sys.exit()