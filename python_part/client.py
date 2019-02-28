# -*- coding: utf8 -*-
import thriftpy2
hello_world_thrift = thriftpy2.load("hello_world.thrift", module_name="hello_world_thrift")

from thriftpy2.rpc import make_client

client = make_client(hello_world_thrift.HelloWorld, '127.0.0.1', 6000)
print(client.call_me())