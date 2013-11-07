#!/bin/bash


echo "Do you need to set the proxy variables? (y/N):"
read var_proxy

if [ $var_proxy == 'y' ] || [ $var_proxy == 'Y' ]; then
   # export proxy variables.
   echo "Enter the http proxy url. (Ex: 172.28.84.6)"
   read var_proxy_url

   echo "Enter the http proxy port. (Ex: 3128)"
   read var_proxy_port

   echo "Ether the http proxy usernmae. (Ex:domain/username)"
   read var_proxy_username

   echo "Enter the http proxy password. (Ex: password)"
   read var_proxy_password

   URL="http://$var_proxy_url:$var_proxy_port"
   export http_proxy=$URL
   export http_username="$var_proxy_username"
   export http_password="$var_proxy_password"
fi


#version="3.2.4"
#echo "The zeromq version is: ${version}"
#URL=http://download.zeromq.org/zeromq-${version}.tar.gz

echo 'Downloading Zeromq For Python'
#wget "$URL"

#tar xvf zeromq-${version}.tar.gz
#cd zeromq-${version}
#./configure
#make
#make install

apt-get install libzmq-dev
apt-get install python-zmq



