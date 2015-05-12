def review(movie):
    from names import keys, current_dir
    import os

    title = movie.title
    year = str(movie.year)

    print('M > Insert an integer between -3 (value totally on the left)'
    'and 3 (value totally on the right)')

    att = {}

    for key in keys:
        flag = 0
        while flag == 0:
            att['key'] = input('M < {}: '.format(key))
            try:
                value = int(att['key'])
            except:
                print('M > Invalid input, insert an integer')
            else:
                if abs(value) <= 3:
                    flag = 1
                else:
                    print('M > Value out of range, input must be in [-3,3]')

    f = open(current_dir + '/Reviews/' + title + '(' + year + ').txt', 'w')

    for key in keys:
        f.write(key + ' ' + att['key'] + '\n')

    f.close()

    movie.att = att
    movie.reviewed = 1
    movie.sync = 0

    path = current_dir + '/.Sync/' + title + '(' + year + ').txt'
    if os.path.exists(path) is True:
        os.unlink(path)

    return()
