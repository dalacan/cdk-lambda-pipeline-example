import psycopg2

def handler(event, context):
    try:
        conn = psycopg2.connect(dbname='postgres', user='postgres', password='postgres')
        cur = conn.cursor()
        cur.execute("SELECT * FROM users")
        rows = cur.fetchall()
        conn.close()
    except Exception as e:
        print(e)
        print("Error.")

    return "Success"