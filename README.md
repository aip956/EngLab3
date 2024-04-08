Create env:
python3 -m venv env
activate env:
source env/bin/activate
Install dependencies:
pip install fastapi sqlalchemy psycopg2-binary
connection port to connect postgres to alchemy

To run API:
Install uvicorn: pip install uvicorn 
Run the API: uvicorn main:app --reload

To POST (add):
Start the API using uvicorn main:app --reload

curl -X POST "http://127.0.0.1:8000/warrior" -H "Content-Type: application/json" -d '{
    "name": "Master Yoda",
    "dob": "1970-01-01",
    "fight_skills": "BJJ, KungFu, Judo"
}'

Select all warriors:
curl -X GET "http://127.0.0.1:8000/warrior"


GET /warrior/[:id] 
curl -X GET "http://127.0.0.1:8000/warrior/{id}"
curl -X GET "http://127.0.0.1:8000/warrior/{1}" returns the Yoda entry


GET /warrior?t=[:search term] – search warrior attributes 
curl -X GET "http://127.0.0.1:8000/warrior?t=search_term"
curl -X GET "http://127.0.0.1:8000/warrior?t=Yoda" returns Yoda


GET /counting-warriors – count registered warriors;
curl -X GET "http://127.0.0.1:8000/counting-warriors"

Docker: Added postgres to Docker (docker-compose.yaml file). 
To rebuild the Docker containers: docker-compose up --build
