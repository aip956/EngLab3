# Engineering Lab 3

## Overview

Build containers: docker-compose up --build
Validated for 20 skills, but not for max 250 length
To POST (add):
Start the API using uvicorn main:app --reload
This project is a FastAPI application designed to manage a database of warriors, 
allowing creation, retrieval, and search of warrior records. It leverages PostgreSQL 
and runs entirely within Docker containers.

## Setup Instructions
### To Run the API locally
Enter the env:
    * source env/bin/activate
Start postgres: 
    * Verify you have it installed:  brew list | grep postgresql
    * Install if necessarey: brew insall postresql
    * Start the db: brew services start postgresql@14 (or postgres)
    * Connect: psql -U postgres




### Docker Setup
Ensure Docker and Docker Compose are installed on your machine. 
Clone the repository and navigate to the project directory.

### Building and Running Containers
Build and start the Docker containers:

```
make buildup
```

This command starts all the required services, including the FastAPI application 
and PostgreSQL database, as defined in the docker-compose.yaml file.

### API Endpoints

Access the API through the Docker container's network. Here are some example commands:

#### Create a Warrior

```
curl -X POST "http://localhost:8000/warrior" -H "Content-Type: application/json" -d '{
"name": "Master Yoda",
"dob": "1970-01-01",
"fight_skills": "BJJ, KungFu, Judo"
}'
```

#### Retrieve Warriors

##### All warriors:

```
curl -X GET "http://localhost:8000/warrior"
```

##### Warrior by ID:

```
curl -X GET "http://localhost:8000/warrior/{id}"
```

#### Search and Count Warriors

##### Search by attribute:

```
curl -X GET "http://localhost:8000/warrior?t=Yoda"
```

##### Count warriors:

```
curl -X GET "http://localhost:8000/counting-warriors"
```

### Testing

Access http://localhost:8000/docs to view and interact with the Swagger UI, which provides
a convenient way to test the API directly from your web browser.


