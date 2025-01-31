import psycopg2

def get_db_connection():
    conn = psycopg2.connect(
        dbname="EMS",
        user="postgres",  
        password="Ntsako@2000",  
        host="localhost",
        port="5432"
    )
    return conn