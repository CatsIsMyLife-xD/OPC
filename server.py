from opcua import Server
import os
import time

server = Server() 
url = "opc.tcp://192.168.1.23:4840"
server.set_endpoint(url)
addSpace = server.register_namespace("OPCUA Server")
node = server.get_objects_node()
ServerInfo = node.add_object(addSpace, "OPC Server")
Param = node.add_object(addSpace, "Parameters")
Water = Param.add_variable(addSpace, "Watering",0)
Shutt = Param.add_variable(addSpace, "Shutter",0)
Water.set_writable()
Shutt.set_writable()
server.start()
print ("{} started at {}".format(server.name, url))

ChangeW, ChangeS = 0, 0
while True:
    file = open ('gen.txt','r')
    for i in range(1):
        buf = file.readline()
        a,b = buf.split('\t')
        Water.set_value(a)
        Shutt.set_value(b[0:-3])
        time.sleep(1)
