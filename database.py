import psycopg2

def get_db_connection():
    conn = psycopg2.connect(
        dbname="EMS",
        user="postgres",  # Replace with your PostgreSQL username
        password="Ntsako@2000",  # Replace with your PostgreSQL password
        host="localhost",
        port="5433"
    )
    return conn