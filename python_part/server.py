# -*- coding: utf8 -*-
import thriftpy2
hello_world_thrift = thriftpy2.load("hello_world.thrift", module_name="hello_world_thrift")

from thriftpy2.rpc import make_server

class Dispatcher(object):
    def call_me(self):
        return "hello world"

server = make_server(hello_world_thrift.HelloWorld, Dispatcher(), '127.0.0.1', 6000)
server.serve()



