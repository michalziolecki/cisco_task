# Cisco task

## About 
This is simple API written in Python 3.10.2 and newest version of Fast API and Pydantic.

## Requirements
- Docker
- make
- xargs

## Structure
- `/src` directory is a part with solution
- `/tests` is a part with automated unit, integration tests and static analysis
- `pyproject.toml` is a main configuration file created by poetry
- application is available on `localhost`, port `8000`

## Application run instruction
To prepare application use `make` command or copy commands from `Makefile`
### Build image
- `make build`
### Run application
- `make run`
### Run application with mapped project volume
- `make run-locally`
### Stop running container
- `make stop`
### Start stopped container
- `make start`
### Remove container
- `make terminate`
### Clean unused images
- `make clean`

## Test run instruction
### Static analysis
- `make static-analysis`
### Unit-test
- `make unit-tests`