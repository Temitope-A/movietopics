def ensure_dir(path):
    import os

    if os.path.exists(path) is False:
        os.makedirs(path)


def path_input(phrase, exception):
    import os

    path = input(phrase)

    if os.path.exists(path) is True:
        print ('> path found')
        return path
    elif path == exception:
        print('> No location given')
        return path
    else:
        print('> Not a valid path')
        return path_input(phrase, exception)


def init_linux():

    from names import current_dir

    ensure_dir(current_dir + '/Movies')
    ensure_dir(current_dir + '/Reviews')
    ensure_dir(current_dir + '/.Sync')


def newsession_linux():

    from names import current_dir
    from loadmovies import load_movie
    import os

    if os.path.exists(current_dir + '/Movies') is False:
        print('M > I could not find the Movies folder. Run Setup.py.')
        return 'runsetup'

    if os.path.exists(current_dir + '/Reviews') is False:
        print(('M > I could not find the Reviews folder. I am creating it now'
        ' but all your previous reviews might be lost.'))
        os.makedirs(current_dir + '/Reviews')

    filenames = os.listdir(current_dir + '/Movies')
    library = []
    count = 0

    for name in filenames:
        output = load_movie(current_dir + '/Movies/' + name)
        if output == 'nofile':
            print(('M > There is something wrong going with {}, perhaps '
            'the path does not exist?'.format(name)))
        elif output == 'lowimdbrating':
            pass
        else:
            library.append(output)
            count += 1

    print('M > {} movies were found in the library'.format(count))
    return library
