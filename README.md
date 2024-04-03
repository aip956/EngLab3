Create env:
python3 -m venv env
activate env:
source env/bin/activate
Install dependencies:
pip install fastapi sqlalchemy psycopg2-binary
connection port to connect postgres to alchemy

pip install uvicorn