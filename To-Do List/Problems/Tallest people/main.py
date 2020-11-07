def tallest_people(**kwargs):
    for k, v in sorted(kwargs.items()):
        if v == max(kwargs.values()):
            print(f'{k} : {v}')
    pass
