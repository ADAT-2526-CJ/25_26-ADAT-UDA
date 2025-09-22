import asyncio
import aiomysql
import time

async def consulta_clientes():
    # Conexión asíncrona con la base de datos
    conn = await aiomysql.connect(
        host="localhost",
        port=3306,
        user="root",
        password="admin",
        db="empresa"
    )

    async with conn.cursor() as cur:
        print("Lanzando consulta a la BD...")
        await cur.execute("SELECT * FROM clientes")
        rows = await cur.fetchall()
        await asyncio.sleep(0)  # Yields control (simula espera)
        print("Respuesta de la BD recibida:")
        for row in rows:
            print(row)

    conn.close()

async def otra_tarea():
    # Simula que el programa hace otra cosa mientras espera la BD
    for i in range(5):
        print(f"Haciendo otra tarea en paralelo... paso {i+1}")
        await asyncio.sleep(1)  # Simula trabajo

async def main():
    start = time.time()

    # Lanzar la consulta y la otra tarea en paralelo
    await asyncio.gather(
        consulta_clientes(),
        otra_tarea()
    )

    end = time.time()
    print(f"Tiempo total: {end - start:.2f} segundos")

# Ejecutar
asyncio.run(main())
