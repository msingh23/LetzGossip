'''
Created on Sep 23, 2013

@author: Manu Singh
Gossip Protocol Implemented With ZeroMq 
Connect REP socket to tcp://<IP-Address>:<Port>
'''

import zmq
import time
from multiprocessing import Process
from GossipConnection import *

class GossipSend(Process):
	
	# Create a Req Socket With The given IPAddress, Perform The Send 
	# Operation And Close The Req Socket.
	def run(self):
		
	   	# Create a Context
	   	context = zmq.Context()

		reqConnect  = GossipConnection()
		port = reqConnect.getPort()
				   	
		while True:
			# Create a Request Socket
			req = context.socket(zmq.REQ)
			ipAddress = reqConnect.getIPAddress()
			
			reqConnection = reqConnect.getConnection(ipAddress)	
			req.connect(reqConnection)

			cmd = 'BETA'

			try:
				# Send a Request To Execute a Command.
				req.send(cmd)

                # Receive The Output.
                # outputMsg = req.recv()
                # print outputMsg
				time.sleep(7)

			except TypeError as err:
				print (str(err))

	  		finally:
	  			req.close()

