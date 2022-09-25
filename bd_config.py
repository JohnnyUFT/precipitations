from sqlite3 import connect, Error
import os

PATH_DATA = os.environ.get('PATH_DATA')
DB_NAME = os.environ.get('DB_NAME')

def insert_into_local(conn, values):
    ''' insert data into table '''
    sql = f'''INSERT INTO local (nome) VALUES ('{values}')'''
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    return cur.lastrowid

def insert_into_data(conn, values):
    ''' insert data into table '''
    print('\nvalues: ', values)
    sql = f'''INSERT INTO data (data_medicao, precipitacao_total, 
            mensal_aut_mm, temp_media, mensal_aut_c) VALUES ({values})'''
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    return cur.lastrowid

def create_table_local():
    ''' create a table from the create_table_sql statement '''
    conn = create_connection(DB_NAME)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS "local" (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome TEXT(64) NOT NULL);
        ''')
    conn.commit()
    conn.close()

def create_table_data():
    ''' create a table from the create_table_sql statement '''
    conn = create_connection(DB_NAME)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS "data" (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        data_medicao TEXT NOT NULL,
        precipitacao_total INTEGER,
        mensal_aut_mm INTEGER,
        temp_media INTEGER,
        mensal_aut_c INTEGER,
        CONSTRAINT data_FK FOREIGN KEY (id) REFERENCES "local"(id)
    );''')
    conn.commit()
    conn.close()

def create_connection(db_file):
    """ create a database connection to a SQLite database """
    try:
        conn = connect(db_file)
        print('Connected to SQLite database')
        return conn
    except Error as e:
        print(e)

    return None

def close_connection(conn):
    if conn:
        conn.close()

def main():
    create_table_local()
    create_table_data()

if __name__ == '__main__':
    main()