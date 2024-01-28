run:
	docker compose up -d

stop:
	docker rm -f $$(docker ps -aq)
	docker rmi flaskserver1
	docker rmi loadbalancer

