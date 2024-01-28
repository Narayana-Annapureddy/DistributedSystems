run:
	docker compose up -d 

stop:
	docker compose down
	docker rm -f $$(docker ps -aq)
	docker rmi -f loadbalancer
	docker rmi -f flaskserver1
	