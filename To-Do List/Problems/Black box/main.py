# use the function blackbox(lst) that is already defined
gg = [1,2,3,4,5,6,7,8]
gg_new = blackbox(gg)
if id(gg) == id(gg_new):
    print('modifies')
else:
    print('new')