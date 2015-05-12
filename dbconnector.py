def sync(library, user, pwd, database='movietopicsdb', host='localhost'):

    import mysql.connector
    from mysql.connector import errorcode

    config = {
        'user': user,
        'password': pwd,
        'database': database,
        'host': host
        }

    try:
        cnx = mysql.connector.connect(**config)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('M > Something is wrong with your user name or password')
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print('M > Database does not exist, contact the developer')
        else:
            print(err)
        return
    else:
        print('MD > Connection succesfull! Welcome {}.'.format(user))

    n = len(library)
    for i in range(0, n):
        if library[i].reviewed == 1 and library[i].sync == 0:
            #create entry in movie_data if not present
            ensure_entry(cnx, library[i])

            #clear user title year row from all movie keys if present and update
            library[i].sync = replace_keys_entry(cnx, user, library[i])

    cnx.close()


#create entry in movie_data if not present

def ensure_entry(connection, movie):

    cur = connection.cursor()

    actors = ''
    for actor in movie.actors:
        actors = actors + ', ' + actor

    add_movie = "INSERT INTO movie_data VALUES ('{}',{},'{}','{}',{})".format(
    movie.title, movie.year, movie.director, actors, movie.imdbrating)

    try:
        cur.execute(add_movie)
    except:
        pass
    else:
        connection.commit()
        print('MD > Data for {} uploaded'.format(movie.title))

    cur.close()


def replace_keys_entry(connection, user, movie):

    from names import keys, current_dir

    cur = connection.cursor()
    add_key = []

    for i in range(1, 16):
        add_key.append("REPLACE INTO key{} VALUES ('{}','{}','{}',{})".format(
            i, user, movie.title, movie.year, movie.att[keys[i - 1]]))

    try:
        for i in range(1, 16):
            cur.execute(add_key[i - 1])
            connection.commit()
    except:
        print('MD > There was a problem synchronizing keys for {}'.format(
            movie.title))
        return 0
    else:
        f = open(current_dir + '/.Sync/' + movie.title + '(' +
        str(movie.year) + ').txt', 'w')
        f.close()
        print('MD > Keys for {} uploaded'.format(movie.title))
        return 1

    cur.close()