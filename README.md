LetzGossip 0.1



h2. Gossip

|groupId|artifactId|version|
|org.jodicloud|gossip|0.1


h3. Code Repositories


https://github.com/jodicloud/LetzGossip

h1. Available artifacts

h2. Gossip Service Analysis



<pre>


Problem Statement

Level 0:  To get the status (Heart beat) of GNs in a GG
Level 1:  To get the status (Heart beat) + specific services health of GNs in a GG
Level 2:  To get the status (Heart beat) + specific services health + metrics collection of GNs in a GG

 

Design 
Tools planed for building prototype (level 0)
1.	Zeromq
2.	Python 

•	Zeromq capability of socket connection will be leveraged in building the gossip prototype.
•	Zeromq pub/sub model is ideal.
•	LetzGossip.py (our code with know the number of GNs in GG, with the IP or DNS name, which is used in establishing connection across the GNs).
•	Python is selected to catch up the POC with open source cloud stacks plugins .



Tools planed for building prototype (level 0 + features)
3.	Zeromq 
4.	Socket programing
5.	Python 

•	Socket programing will be added advantage with the data transfer with the udp packet
•	And providing the drivers to select to select the Gossip implementation 
•	Like zeromq or udp based socket programing 

</pre>
