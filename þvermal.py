thvermal = [4879.4, 12104, 12742,6779, 139820, 116460, 49244, 50724, 2376.6]
hlutfoll = []
planetur = ['merkur', 'venus', 'jordin', 'mars', 'jupiter', 'saturnus', 'uranus', 'neptunus', 'pluto']
a = []


def planet_size(x):
    h = x/thvermal[4]
    for i in thvermal:
        a.append(i*h)
    print([i for i in zip(planetur, a)])

planet_size(2)

