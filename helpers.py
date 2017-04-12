import os

def loadMongoURL():
    res = None

    if os.path.isfile('../mongo.txt'):
        f = open('../mongo.txt')
        res = f.readline().strip('\n')
        f.close()
    else:
        res = os.environ['DB']

    return res
