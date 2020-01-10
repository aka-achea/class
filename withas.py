#

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


from socket import socket, AF_INET, SOCK_STREAM

class LazyConnection:
    def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
        self.address = address
        self.family = AF_INET
        self.type = SOCK_STREAM
        self.sock = None

    def __enter__(self):
        if self.sock is not None:
        raise RuntimeError('Already connected')
        self.sock = socket(self.family, self.type)
        self.sock.connect(self.address)
        return self.sock

    def __exit__(self, exc_ty, exc_val, tb):
        self.sock.close()
        self.sock = None

from functools import partial

conn = LazyConnection(('www.python.org', 80))
# Connection closed
with conn as s:
    # conn.__enter__() executes: connection open
    s.send(b'GET /index.html HTTP/1.0\r\n')
    s.send(b'Host: www.python.org\r\n')
    s.send(b'\r\n')
    resp = b''.join(iter(partial(s.recv, 8192), b''))
    # conn.__exit__() executes: connection closed
    with conn as s2:
        pass