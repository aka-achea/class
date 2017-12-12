
from person import Person, Manager

bob = Person('Bob smith')
sue = Person('Sue Jones',job='dev',pay=90000)
tom = Manager('Tome Jones', 50000)

import shelve
db = shelve.open('persondb')
for obj in (bob,sue,tom):
    db[obj.name]=obj
db.close()
