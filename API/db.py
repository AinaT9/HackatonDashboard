import mysql.connector
import pandas as pd
# from typing import List

# Configuración de la conexión MySQL
def get_db_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="sam3000"
    )
    return conn

# Función para obtener datos usando una consulta SQL
def get_data(query: str) -> pd.DataFrame:
    conn = get_db_connection()
    try:
        # Realizar consulta
        df = pd.read_sql(query, conn)
        return df
    finally:
        conn.close()