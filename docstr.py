"I am: docstr.__doc__"
def func(args):
    "1 am: docstr.func.__doc__"
    pass

class spam:
    "I am: spam.__doc__  or docstr.spam.__doc__ "
    def method(self, arg):
        "I am: spam.method.__doc__ or self.method.__doc__"
        pass

if __name__=='__main__':
    import docstr
    print(docstr.__doc__)
    print(docstr.func.__doc__)
    print(docstr.spam.__doc__)
    print(docstr.spam.method.__doc__)
