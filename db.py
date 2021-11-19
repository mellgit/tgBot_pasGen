import sqlite3
import conf

try:
    conn = sqlite3.connect(conf.PATH_TO_DB)
    cursor = conn.cursor()

    # cursor.execute("insert or ignore into 'test' ('name') values (?)", ('steam',))

    pas = cursor.execute("SELECT * FROM test;")
    print(pas.fetchall())

    conn.commit()

except sqlite3.Error as error:
    print(f"Error: {error}")

finally:
    if(conn):
        conn.close()


"""
добавить запись 
записать изменения
"""