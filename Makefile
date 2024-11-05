
build-java:
	@echo "\nBuilding Java..."
	@cd java && javac -cp .:gson-2.11.0.jar Main.java Helper.java

build-go:
	@echo "\nBuilding Go..."
	@cd golang && go build

build-cplus:
	@echo "\nBuilding CPlus..."
	@cd cplus && cmake . && make

build-rust:
	@echo "\nBuilding Rust..."
	@cd rustapp && cargo build --release

build-all:
	@make build-java
	@make build-go
	@make build-cplus
	@make build-rust

run-cplus:
	@echo "\nRUNNING CPlus..."
	@cd cplus && ./search_program

run-java:
	@echo "\nRUNNING Java..."
	@cd java && java -cp .:gson-2.11.0.jar Main 

run-go:
	@echo "\nRUNNING Go..."
	@cd golang && ./gosearching

run-js:
	@echo "\nRUNNING JavaScript..."
	@cd javascript && node main.js

run-php:
	@echo "\nRUNNING PHP..."
	@cd php && php main.php

run-py:
	@echo "\nRUNNING Python..."
	@cd py && python main.py

run-rust:
	@echo "\nRUNNING Rust..."
	@cd rustapp && ./target/release/rustapp

run-all:
	@make run-cplus
	@make run-go
	@make run-java
	@make run-js
	@make run-php
	@make run-py
	@make run-rust

run:
	@make run-all > run.log