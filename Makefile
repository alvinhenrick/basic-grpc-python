
install:
	pip install -r requirements.txt

runprotoc:
	python -m grpc_tools.protoc -I=. --python_out=. --grpc_python_out=. ./app/calculator.proto

runserver:
	python server.py

runclient:
	python client.py

up:
	docker-compose -f docker-compose.yaml build
	docker-compose -f docker-compose.yaml up

down:
	docker-compose -f docker-compose.yaml down