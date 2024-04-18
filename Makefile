buildup: ## Build project and run with compose
	docker-compose up --build

build: ## Build project with compose
	docker-compose build

up:	## Run project with compose
	docker-compose up --remove-orphans

clean: ## Reset project
	docker-compose down -v --remove-orphans | true
	docker-compose rm -f | true
