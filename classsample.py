#!/usr/bin/python
#coding:utf-8

from classtools import AttrDisplay

class Person(AttrDisplay):
    def __init__(self,name,job=None,pay=0):
        self.name = name
        self.job = job
        self.pay = pay
    def lastname(self):
        return self.name.split()[-1]
    def giveraise(self,percent):
        self.pay = int(self.pay *(1+ percent))

class Manager(Person):
    def __init__(self,name,pay):
        Person.__init__(self,name,'mgr',pay) # embeded Person object
    def giveraise(self, percent, bonus=.10):
        Person.giveraise(self,percent + bonus)  # intercept and delegate
#    def __getattr__(self,attr):
#        return getattr(self.person,attr)

class Department:
    def __init__(self,*args):
        self.members = list(args)
    def addmember(self, person):
        self.members.append(person)
    def giveraise(self,percent):
        for person in self.members:
            person.giveraise(percent)
    def showall(self):
        for person in self.members:
            print(person)

class Super:
    def method(self):
        print('in Super.method')
    def delegate(self):
        self.action()
    def action(self):
        raise NotImplementedError('Action not defined')

class Inheritor(Super):
    pass

class Replacer(Super):
    def method(self):
        print("in Replacer.method")

class Extender(Super):
    def method(self):
        print('starting Extender.method')
        Super.method(self)
        print('ending Extender.method')

class Provider(Super):
    def action(self):
        print('in Provider.action')

X = 11

def f():
    print(X)

def g():
    X = 22
    print(X)

class C:
    X = 33
    def m(self):
        X = 44
        self.X = 55


if __name__=='__main__':
    """
    bob = Person('Bob Smith')
    sue = Person('Sue Jones',job='dev',pay=100000)
    print(bob.name,bob.pay)
    print(sue.name,sue.pay)
    sue.giveraise(.10)
    print(sue)
    tom = Manager('Tom Jones',50000)
    tom.giveraise(.10)
    print(tom)
    print('------All Three------------')
    for obj in (bob,sue,tom):
        obj.giveraise(.10)
        print(obj)
    print('--------------------------')
    development = Department(bob,sue)
    development.addmember(tom)
    development.giveraise(.10)
    development.showall()
    """
    """
    for klass in (Inheritor,Replacer,Extender):
        print('\n'+klass.__name__ + '...')
        klass().method()
    """

    print(X)
    f()
    g()
    print(X)
    obj = C()
    print(obj.X)
    obj.m()
    print(obj.X)
    print(C.X)
