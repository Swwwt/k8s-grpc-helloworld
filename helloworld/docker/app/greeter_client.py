#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from __future__ import print_function
import logging

import grpc

import helloworld_pb2
import helloworld_pb2_grpc


# In[ ]:


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    
    ## with grpc.insecure_channel('localhost:50051') as channel:
    ## channel = grpc.insecure_channel('localhost:50051')
    ## channel = grpc.insecure_channel('server:22222')
    channel = grpc.insecure_channel('helloworld-server:50051')
    stub = helloworld_pb2_grpc.GreeterStub(channel)
    response = stub.SayHello(helloworld_pb2.HelloRequest(name='you'))    
    print("Greeter client received: " + response.message)
    response = stub.SayHelloAgain(helloworld_pb2.HelloRequest(name='you'))
    print("Greeter client received: " + response.message)


# In[ ]:


if __name__ == '__main__':
    logging.basicConfig()
    run()

