import asyncio
import aiomysql #pip install aiomysql
#En Python, cuando trabajamos con asincronía, casi siempre necesitamos también asyncio, que es la librería estándar para manejar el event loop.


# Ejemplo con asincronía:
async def main():
    # Conexión asíncrona con la base de datos
    conn = await aiomysql.connect(
        host="localhost",
        port=3306,
        user="root",
        password="admin",
        db="empresa"
    )

    async with conn.cursor() as cur:
        # Ejecutar la consulta
        await cur.execute("SELECT * FROM clientes")
        rows = await cur.fetchall()

        # Mostrar resultados
        for row in rows:
            print(row)

    conn.close()

# La asincronía permite que, mientras esperamos la respuesta de la BD,
# el programa pueda seguir haciendo otras tareas en paralelo.
asyncio.run(main())

# En los programas habituales, cuando pedimos algo a una base de datos, el programa se bloquea esperando la respuesta.
# Con la asincronía, podemos lanzar varias tareas a la vez y el programa no queda “parado” mientras llega la información.
# En Python, esto se hace con la librería asyncio y, en el caso de MariaDB/MySQL, con aiomysql.
