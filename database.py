import psycopg2

# Database configuration
db_config = {
    "dbname": "tablename",
    "user": "jirka",
    "password": 'Diplom10*',
    "host": "127.0.0.1",  
    "port": "3306",
    "sslmode":"disable"      
}

connection = None

try:
    # Establish a connection to the database
    connection = psycopg2.connect(**db_config)
    print("Connected to the database!")
    
    # Add your database operations here
    
except psycopg2.Error as e:
    print("Error connecting to the database:", e)
finally:
    # Close the connection when done (if it was successfully created)
    if connection:
        connection.close()