#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install mysql-connector-python


# In[12]:


pip install seaborn


# In[2]:


import mysql.connector
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from mysql.connector import Error


# Verificacion de la conexion 

# In[3]:


import mysql.connector
from mysql.connector import Error

try:
    print("Trying to connect...")
    connection = mysql.connector.connect(
        host='localhost',
        port='3306',
        user='root',
        password='Andrea2024!',
        database='datos_mundiales'
    )
    print("Check status...")
    if connection.is_connected():
        print('Conexión exitosa.')
        # No olvides cerrar la conexión una vez que hayas terminado con ella.
        connection.close()
except mysql.connector.Error as e:
    print('Error al conectar a MySQL:', e)


# Funcion para ejecutar consultas 

# In[4]:


def execute_query(query):
    connection = mysql.connector.connect(
        host='localhost',
        port='3306',
        user='root',
        password='Andrea2024!',
        database='datos_mundiales'
    )
    if connection:
        try:
            with connection.cursor(dictionary=True) as cursor:
                cursor.execute(query)
                result = cursor.fetchall()
                # Convertir los resultados en un DataFrame de pandas
                df = pd.DataFrame(result)
                return df
        except Error as e:
            print(f"Error al ejecutar la consulta: {e}")
        finally:
            connection.close()  # Cerrar la conexión después de la consulta


# In[5]:


query1 = """
SELECT Name AS CountryName, Population
FROM country
WHERE Continent = 'Europe'
ORDER BY Population DESC;
"""


# In[6]:


df1 = execute_query(query1) 
print(df1)


# In[6]:


import mysql.connector
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from mysql.connector import Error

# Función para conectarse a la base de datos
def connect_to_db():
    try:
        # Crear la conexión
        connection = mysql.connector.connect(
            host="localhost",      
            user="root",           
            password="Andrea2024!",  # Contraseña personal
            database="datos_mundiales"    # Nombre de base de datos en MySql
        )
        if connection.is_connected():  # Verificar si la conexión fue exitosa
            print("Conexión exitosa a la base de datos")
            return connection
    except Error as e:
        print(f"Error al conectar a MySQL: {e}")
        return None

# Función para ejecutar consultas SELECT
def execute_query(query):
    connection = connect_to_db()
    if connection:
        try:
            with connection.cursor(dictionary=True) as cursor:
                cursor.execute(query)
                result = cursor.fetchall()
                # Convertir los resultados en un DataFrame de pandas
                df = pd.DataFrame(result)
                return df
        except Error as e:
            print(f"Error al ejecutar la consulta: {e}")
        finally:
            connection.close()  # Cerrar la conexión después de la consulta

query1 = """
SELECT Name AS CountryName, Population
FROM country
WHERE Continent = 'Europe'
ORDER BY Population DESC;
"""

# Ejecutar la consulta y obtener los resultados en un DataFrame
df1 = execute_query(query1)
print(df1)


# *****************Ejercicio 2: Los 5 países mas grandes del mundo*****************

# Esta consulta nos da los países con mas superficie del mundo: 

# In[7]:


#Consulta para obtener los resultados
query2 = """
SELECT Name AS Country, SurfaceArea
FROM country
ORDER BY SurfaceArea DESC
LIMIT 5;
"""

# Ejecutar la consulta y obtener los resultados en DataFrame
df2 = execute_query(query2)
print(df2)


# *****************Ejercicio 3: La población total por continente*****************

# Este query nos mostrará la cantidad de población existente en cada continente ordenado en forma descendente 

# In[8]:


##Consulta para obtención de resultados 
query3 = """
SELECT continent , SUM(Population) AS TotalPopulation
FROM country
GROUP BY continent
ORDER BY TotalPopulation DESC;
""" 

# Ejecutar la consulta y obtener los resultados en DataFrame
df3 = execute_query(query3)
print(df3)


# *****************Ejercicio 4: la población de todos los países de Europa, ordenados descendente*****************

# In[9]:


query4 = """
SELECT city.Name AS CityName, city.Population
FROM city
JOIN country ON city.CountryCode = country.Code
WHERE country.Continent = 'Europe'
ORDER BY city.Population DESC;
"""

# Ejecutar la consulta y obtener los resultados en un DataFrame
df4 = execute_query(query4)
print(df4)


# *****************Ejercicio 5: Actualiza la población de China (código de país 'CHN') a 1500000000 (1.5 mil millones)***************** 

# In[13]:


query5 = """
UPDATE country
SET Population = '1520000000'
WHERE Code = 'CHN';
"""
connection.commit()
print("\nEjercicio 5 - Población de China actualizada.")

# Ejecutar la consulta y obtener los resultados en un DataFrame
df5 = execute_query(query5)
print(df5)


# In[ ]:




