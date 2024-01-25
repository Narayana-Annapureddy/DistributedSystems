# Implementing Load Balancer

Load Balancer is a server that routes all the incoming requests to the available servers, so that the load is distributed evenly
across all the servers. It also increases or decreases the number of servers based on the requirement. Thus availability is ensured.
--------------------------------------------------------------------------------------------------------------------------------
### Logic behind the load balancer  ->


--------------------------------------------------------------------------------------------------------------------------------
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

**2. Docker Compose **

sudo curl -SL https://github.com/docker/compose/releases/download/v2.15.1/docker-compose-linux-x86_64 -o /usr/local/bin/docker-compose

sudo chmod +x /usr/local/bin/docker-compose

sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose


RUN docker compose up
