build:
	docker build . -t cisco_task

run:
	docker run -d -p 8000:8000 cisco_task:latest

run-locally:
	docker run -v ${PWD}:/app/ -p 8000:8000 cisco_task:latest

start:
	docker container ls -a -q --filter ancestor=cisco_task | head -1 | xargs docker start

stop:
	docker ps -q --filter ancestor=cisco_task | xargs docker stop

terminate:
	docker ps -q --filter ancestor=cisco_task | xargs docker rm -f

clean:
	docker images -f "dangling=true" -q | xargs docker rmi -f

static-analysis:
	docker container run cisco_task:latest bash /app/tests/static_analysis/run_static_analysis.sh

unit-tests:
	docker container run cisco_task:latest pytest tests/unit/ -v