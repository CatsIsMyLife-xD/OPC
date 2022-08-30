from opcua import Client 
import time


url = "opc.tcp://192.168.1.23:4840" 

client = Client(url)

client.connect()

print("Client Connected")


while True:
    Water = client.get_node("ns=2;i=3")
    Watering = Water.get_value()
    Shutt = client.get_node("ns=2;i=4")
    Shuttering = Shutt.get_value()
    print (Watering, Shuttering, sep = "\t") 
    time.sleep(1)


	
