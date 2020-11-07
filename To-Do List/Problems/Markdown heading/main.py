def heading(str_v, level=1):
    if level == None or level <= 0:
        gg = '#' * 1 + ' ' + str_v
    elif level >= 6:
        gg = '#' * 6 + ' ' + str_v
    else:
        gg = '#' * level + ' ' + str_v
    return gg