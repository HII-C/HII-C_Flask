def loadMongoURL():
    f = open('mongo.txt')
    res = f.readline().strip('\n')
    f.close()

    return res
