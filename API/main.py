from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from db import get_data, get_db_connection
import pandas as pd
import uvicorn

app = FastAPI()
origins = ["http://localhost:7000"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
    expose_headers=["Content-Disposition"],
    max_age=600,
)
@app.get("/")
async def read_root():
    return {"hello": "world"} 

@app.get("/kwh")
async def get_items():
    query = "SELECT name, DATE_FORMAT(fecha_trama, '%H:00:00') AS hour, atributos_KWH FROM aparato WHERE name = 'Farola 1' AND fecha_trama BETWEEN '2024-01-01 00:00:00' AND '2024-12-31 23:59:59' GROUP BY hour ORDER BY hour LIMIT 100;"
    
    conn = get_db_connection()
    print(conn)
    if conn is None:
        return {"error": "No se pudo conectar a la base de datos"}

    try:
        
        data = get_data(query)
        labels = data['hour'].tolist()  # Usa 'hour' como alias de fecha_trama
        values = data['atributos_KWH'].tolist()
        return {"labels": labels, "data": values}
    except Exception as e:
        return {"error": f"Error al ejecutar la consulta: {e}"}
    finally:
        conn.close()