class traceblock:
    def message(self,arg):
        print('running',arg)
    def __enter__(self):
        print('starting with block')
        return self
    def __exit__(self,exc_type,exc_value,exc_tb):
        if exc_type is None:
            print('exited normally\n')
        else:
            print('raise an exception!',exc_type)
            return False

with traceblock() as action:
    action.message('test 1')
    print('reached')

with traceblock() as action:
    action.message('test 2')
    raise TypeError
    print('not reached')
