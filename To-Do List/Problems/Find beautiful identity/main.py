def object_with_beautiful_identity():
    for i in range(10_000):
        gg = str(id(i))
        ind_step = len(gg)
        if gg[ind_step-3:ind_step] == '888':
            return i