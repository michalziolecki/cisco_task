build:
	docker build . -t cisco_task

run:
	docker run -d cisco_task:latest

run-locally:
	docker run -v ${PWD}:/app/ -p 8000:8000 cisco_task:latest

start-api:
	docker container ls -a -q --filter ancestor=cisco_task | head -1 | xargs docker start

stop-api:
	docker ps -q --filter ancestor=cisco_task | xargs docker stop

terminate-api:
	docker ps -q --filter ancestor=cisco_task | xargs docker rm -f