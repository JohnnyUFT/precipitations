from sqlite3 import connect, Error
import os

PATH_DATA = os.environ.get('PATH_DATA')
DB_NAME = os.environ.get('DB_NAME')

def insert_into_local(conn, values):
    ''' insert data into table '''
    sql = f'''INSERT INTO local (nome, codigo_estacao, latitude, longitude, altitude, situacao,
        data_inicial, data_final, periodicidade) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)'''
    cur = conn.cursor()
    cur.execute(sql, values)
    conn.commit()
    return cur.lastrowid

def insert_into_data(conn, values):
    ''' insert data into table '''
    sql = f'''INSERT INTO data (data_medicao, dias_precip, mensal_aut, precip_total,
                    mensal_aut_mb, pressao_atmosferica, media_mensal_aut,
                temperatura_media, mensal_aut_c, vento, velocidade_maxima, 
                local_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
    cur = conn.cursor()
    cur.execute(sql, values)
    conn.commit()
    return cur.lastrowid

def create_table_local():
    ''' create a table from the create_table_sql statement '''
    conn = create_connection(DB_NAME)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS "local" (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        codigo_estacao TEXT,
        latitude TEXT,
        longitude TEXT,
        altitude TEXT,
        situacao TEXT,
        data_inicial TEXT,
        data_final TEXT,
        periodicidade TEXT
    );
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
        data_medicao TEXT,
        dias_precip INTEGER,
        mensal_aut INTEGER,
        precip_total INTEGER,
        mensal_aut_mb INTEGER,
        pressao_atmosferica INTEGER,
        media_mensal_aut REAL,
        temperatura_media REAL,
        mensal_aut_c REAL,
        vento INTEGER,
        velocidade_maxima INTEGER,
        vento_rev INTEGER,
        velocidade_media REAL,
        local_id INTEGER,
        CONSTRAINT data_FK FOREIGN KEY (local_id) REFERENCES "local"(id)
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