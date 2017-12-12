
class Employee:
    def __init__(self,name,salary=0):
        self.name = name
        self.salary = salary
    def lastname(self):
        return self.name.split()[-1]
    def giveraise(self,percent):
        self.salary = int(self.salary *(1+ percent))
    def work(self):
        print(self.name,'does stuff')
    def __repr__(self):
        return "<Employee:name=%s,salary=%s>" % (self.name,self.salary)

class Chef(Employee):
    def __init__(self,name):
        Employee.__init__(self,name,50000) # embeded Person object
    def work(self):
        print(self.name,'make food')

class Server(Employee):
    def __init__(self,name):
        Employee.__init__(self,name,40000) # embeded Person object
    def work(self):
        print(self.name,'serve customer')

class PizzaRobot(Chef):
    def __init__(self,name):
        Chef.__init__(self,name) # embeded Person object
    def work(self):
        print(self.name,'make pizza')



if __name__=='__main__':

    bob = PizzaRobot('Bob Smith')
    print(bob)
    bob.work()
    bob.giveraise(.10)
    print(bob);print()

    for klass in Employee,Chef,Server,PizzaRobot:
        obj = klass(klass.__name__)
        obj.work()
