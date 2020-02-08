#!/usr/bin/env python
# coding: utf-8

# In[5]:


from concurrent import futures
import logging

import grpc

import helloworld_pb2
import helloworld_pb2_grpc


# In[ ]:


class Greeter(helloworld_pb2_grpc.GreeterServicer):
        
        def SayHello(self, request, context):
            return helloworld_pb2.HelloReply(message='Hello, %s!' % request.name)
        
        def SayHelloAgain(self, request, context):
            return helloworld_pb2.HelloReply(message='Hello again, %s!' % request.name)


# In[ ]:


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:50051')
    ## server.add_insecure_port('[::]:22222')
    server.start()
    server.wait_for_termination()


# In[ ]:


if __name__ == '__main__':
    logging.basicConfig()
    serve()


# In[7]:


try:    
    get_ipython().system('jupyter nbconvert --to python greeter_server.ipynb')
    # python即转化为.py，script即转化为.html
    # file_name.ipynb即当前module的文件名
except:
    pass

