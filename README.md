# Implementing Load Balancer 

_Load Balancer is a server that routes all the incoming requests to the available servers, so that the load is distributed evenly across all the servers. It also increases or decreases the number of servers based on the requirement. Thus availability is ensured._



-----------------------------------------------------------------------------------------------------------------------------
# Prerequisites
**1 .Docker version 24.0.7, build afdd53b**

sudo apt-get update

sudo apt-get install ca-certificates curl gnupg lsb-release

sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
$(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt-get update

sudo apt-get install docker-ce docker-ce-cli containerd.io

-----------------------------------------------------------------------------------------------------------------------------

**2. Docker Compose **

sudo curl -SL https://github.com/docker/compose/releases/download/v2.15.1/docker-compose-linux-x86_64 -o /usr/local/bin/docker-compose

sudo chmod +x /usr/local/bin/docker-compose

sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose


# How to run the application

1. make run
   
    --> this runs 'docker compose up' run command, which will build images for both the loadbalancer and flaskserver, and one container for each of them (lbserver1, server1)
   
    --> this will run in a detached mode. To exit press ctrl+c
   
2. make stop
   
    --> this command removes all the containers and images created previously
   
    --> ## It is recommended to run this command for smooth working of the application ##
   
# Logic
   ## Load Balancer


   ## App.py
      -> It has 4 endpoints (add, rem, rep, <path>)
      
      -> add 
         is post request which accepts two parameters n, replicas
         you can send this request using  ** POSTMAN ** using the below request of POST method
                     http://127.0.0.1:5000/add?n=1&replicas=['s21']
                     if n > len(replicas) then n-len(replicas) number of random servers are created along with ones mentioned in the request
                     
      -> rem
         is post request which accepts two parameters n, replicas
         you can send this request using  ** POSTMAN ** using the below request of POST method
                     http://127.0.0.1:5000/rem?n=1&replicas=['s21']
                     if n > len(replicas) then n-len(replicas) number of random servers are removed along with ones mentioned in the request

      -> rep 
         is a GET request with 0 params
         you can send this request using  ** POSTMAN ** using the below request of GET method
                     http://127.0.0.1:5000/rep
                     returns all available servers

      -> home 
         is a GET request with 0 params
         you can send this request using  ** POSTMAN ** using the below request of GET method
                     http://127.0.0.1:5000/home
                     redirects the request to one of the available servers

                     -> on each request random request id is generated, based on the hashing (given) maps the request to one of the servers
                     -> heartbeat of that server if checked before mapping the request
                     -> If the server is down then new server is spawned 

