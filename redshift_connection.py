# Dummy script to test redshift connection
import psycopg2
from dotenv import load_dotenv
import os

host = os.getenv("REDSHIFT_HOST")    # e.g., cluster-name.region.redshift.amazonaws.com
user = os.getenv("REDSHIFT_USERNAME")
password = os.getenv("REDSHIFT_PASSWORD")
port = "5439"  # Default Redshift port
dbname = "dev"

# Connection string
conn_string = f"dbname='{dbname}' user='{user}' host='{host}' port='{port}' password='{password}'"

# Connect to Redshift
try:
    conn = psycopg2.connect(conn_string)
    print("Connected to Redshift!")

    # Create a cursor
    cursor = conn.cursor()

    # Execute a query
    query = "SELECT version();"  # Example query: get version of Redshift
    cursor.execute(query)

    # Fetch and print the result
    version = cursor.fetchone()
    print(f"Redshift version: {version}")

    # Close the cursor and connection
    cursor.close()
    conn.close()

except Exception as error:
    print(f"Error: {error}")