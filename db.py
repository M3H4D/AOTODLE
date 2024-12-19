import sqlite3

def connect_to_database():
    conn = sqlite3.connect('aot.db',isolation_level=None)
    return conn


def create_tables():
    conn = connect_to_database()

    # Create Characters Table
    conn.execute('''
        CREATE TABLE IF NOT EXISTS Characters (
            CharacterID INTEGER PRIMARY KEY AUTOINCREMENT,
            Name TEXT,
            Gender BINARY,
            Affiliation1 TEXT,
            Affiliation2 TEXT,
            Residence TEXT,
            Alive TEXT,
            TitanKills INTEGER,
            TitanPowers BINARY,
            Debut TEXT,
            ImageURL TEXT
        )
    ''')

    conn.commit()
    conn.close()


def add_character_to_database(n,g,a1,a2,r,a,tk,tp,d,i):
    conn = connect_to_database()

    conn.execute('''
        INSERT INTO Characters (Name,Gender,Affiliation1,Affiliation2,Residence,Alive,TitanKills,TitanPowers,Debut,ImageURL)
        VALUES (?,?,?,?,?,?,?,?,?,?)
    ''',(n,g,a1,a2,r,a,tk,tp,d,i))

    conn.commit()
    conn.close()

def get_characterID(name):
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute("SELECT CharacterID FROM Characters WHERE Name = ?", (name,))
    charID = cursor.fetchone()

    conn.close()
    return charID[0]

def get_all_saved_characters(names):
    results = []
    conn = connect_to_database()
    cursor = conn.cursor()
    
    for name in names:
        cursor.execute("SELECT * FROM Characters WHERE Name = ?", (name,))
        rows = cursor.fetchall()

        results.extend(rows)
    return results

def check_name_in_database(name):
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Characters WHERE Name = ?", (name,))
    rows = cursor.fetchall()
    if not rows:
        return False
    else:
        return True
    
def number_of_characters():
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM Characters")
    no_of_chars = cursor.fetchone()
    return no_of_chars[0]