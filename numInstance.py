
class  Spam:
    numInstance = 0
    def __init__(self):
        Spam.numInstance += 1
    def printNumInstance():
        print("Number of instances:", Spam.numInstance)
    printNumInstance = staticmethod(printNumInstance)

    def printNum(cls):
        print("Number of instances:", cls.numInstance)
        printNum = classmethod (printNum)


class C:
    numInstance = 0
    def __init__(self):
        Spam.numInstance += 1
    @staticmethod
    def printNumInstance():
        print("Number of instances:", Spam.numInstance)
