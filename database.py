import psycopg2
import secret

# Database configuration
db_config = {
    "dbname": secret.dbname,
    "user": secret.user,
    "password": secret.heslo,
    "host": secret.host,  
    "port": secret.port,
    "sslmode":"prefer"  
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