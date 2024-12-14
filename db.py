import sqlite3

def connect_to_database():
    conn = sqlite3.connect('aot.db',isolation_level=None)
    return conn


def create_tables():
    conn = connect_to_database()

    # Create Characters Table
    conn.execute('''
        CREATE TABLE IF NOT EXISTS characters (
            CharactedID INTEGER PRIMARY KEY AUTOINCREMENT,
            Name TEXT,
            Gender BINARY,
            Affiliations TEXT,
            Residence TEXT,
            Alive TEXT,
            TitanKills INTEGER,
            TitanPowers BINARY,
            Debut TEXT
        )
    ''')

    conn.commit()
    conn.close()