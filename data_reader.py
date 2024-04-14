import psycopg2

HOST = "postgres"
DBNAME = "mydatabase"
USER = "myuser"
PASSWORD = "mypassword"

def read_data():
    try:
        connection = psycopg2.connect(host=HOST, dbname=DBNAME, user=USER, password=PASSWORD)
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM mytable;")
        data = cursor.fetchone()

        print("Data from database:", data)

    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL:", error)

    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

if __name__ == "__main__":
    read_data()