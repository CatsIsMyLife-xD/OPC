from opcua import Client 
import time
from threading import Thread

url = "opc.tcp://192.168.1.23:4840" 

client = Client(url)

client.connect()

print("Client Connected")

def main():
    while True:
        Water = client.get_node("ns=2;i=3")
        Watering = Water.get_value()
        Shutt = client.get_node("ns=2;i=4")
        Shuttering = Shutt.get_value()
        print (Watering, Shuttering, sep = "\t") 
        time.sleep(1)

def ChangeAtr():
    txtW = input()
    txtS = input()
    f = open('gen.txt','w')
    f.write(f'{txtW}\t{txtS}')

th = Thread(target = main,args = ())
th2 = Thread(target = ChangeAtr, args = ())
th.start()
th2.start()


	
