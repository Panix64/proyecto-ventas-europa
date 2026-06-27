import sqlite3
import os

# Buscamos la carpeta actual donde está este script de Python
ruta_carpeta = os.path.dirname(os.path.abspath(__file__))
ruta_base_datos = os.path.join(ruta_carpeta, 'Europe_Sales_Project.db')

# 1. Conectamos con la base de datos de la misma carpeta
conn = sqlite3.connect(ruta_base_datos)
cursor = conn.cursor()

# 2. Tu query de los "Tiburones de Élite" (>1000€)
query = """
SELECT 
    c.full_name,
    c.country,
    SUM(s.amount_eur) AS total_gastado_eur
FROM Sales_Europe s
INNER JOIN Customers_Europe c 
    ON s.customer_id = c.customer_id
GROUP BY c.full_name, c.country
HAVING total_gastado_eur > 1000
ORDER BY total_gastado_eur DESC;
"""

# 3. Ejecutamos la consulta desde Python
print("🚀 Conectando a Europe_Sales_Project.db...")
try:
    cursor.execute(query)
    resultados = cursor.fetchall()

    # 4. Pintamos el reporte ejecutivo en la terminal
    print("\n📊 REPORTE DE VENTAS ELITE (MÁS DE 1000€):")
    print("-" * 50)
    for fila in resultados:
        print(f"👤 Cliente: {fila[0]} | 🌍 País: {fila[1]} | 💰 Total: {fila[2]}€")
    print("-" * 50)
except sqlite3.OperationalError as e:
    print(f"\n❌ Error de tablas: {e}")
    print("💡 Consejo: Asegúrate de volver a ejecutar los scripts de inserción en DBeaver si la tabla está vacía.")

# 5. Cerramos la conexión de forma segura
conn.close()
print("🔒 Conexión cerrada con éxito. ¡Buen trabajo, Alex!")