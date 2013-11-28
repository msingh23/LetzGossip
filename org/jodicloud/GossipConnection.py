'''
Created on Sep 23, 2013

@author: Manu Singh
Gossip Protocol Implemented With ZeroMq 
'''



import random
import ConfigParser

class GossipConnection():
    
    
    def __init__(self):
        
        # Reading the configuration file
        self.config = ConfigParser.ConfigParser()
        self.config.read('gossip.conf')
        self.reqConnection = self.config.get('GOSSIP_SEND', 'tcp_connect')   
        self.recvConnection = self.config.get('GOSSIP_RECIVE', 'tcp_bind') 
	self.ipList = self.config.get('IPLIST','IP').split(',')
        self.port = self.config.get('DEFAULT','PORT')
        
    def getConnection(self,ipAddr=0):
        
        if ipAddr != 0:
            self.connectionStr = self.reqConnection + ipAddr + self.port
            
        else:
             self.connectionStr = self.recvConnection + self.port
         
        return (self.connectionStr)     
    
    def getPort(self):
        return (self.port)

    # This function randomaly selects the ipaddress from the list.	
    def getIPAddress(self):
        ipAddress = random.choice(self.ipList)
        return ipAddress


        
    
