run:
	docker compose up 

stop:
    docker rm -f $(docker ps -aq)
    docker rmi flaskserver1
    docker rmi loadbalancer
