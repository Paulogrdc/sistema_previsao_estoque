import psycopg 
from dotenv import load_dotenv
import os 

#Conexão com o banco
def conectar():
    load_dotenv()
    conn = psycopg.connect(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("USER"),
        password=os.getenv("PASSWORD"))
    return conn 

    

