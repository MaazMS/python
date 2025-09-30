class ObjectCounter:

    numberOfObjects = 0

    def __init__(self):
        ObjectCounter.numberOfObjects +=1

    @staticmethod
    def displayCount():
        print("number of objec", ObjectCounter.numberOfObjects)
        
obj1 = ObjectCounter()
Obj2 = ObjectCounter()
obj3 = ObjectCounter()
Obj4 = ObjectCounter()

ObjectCounter.displayCount()
obj1.displayCount()