iris = {}

def add_iris(*args, **kwargs):
    global iris
    iris[args[0]] = {}
    iris[args[0]].update({'species': args[1]})
    iris[args[0]].update({'petal_length': args[2]})
    iris[args[0]].update({'petal_width': args[3]})
    iris[args[0]].update(kwargs.items())
    pass
