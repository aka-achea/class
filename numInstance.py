
class  Spam:
    numInstance = 0
    def __init__(self):
        Spam.numInstance += 1
    def printNumInstance():
        print("Number of instances:", Spam.numInstance)
    print = staticmethod(printNumInstance)
