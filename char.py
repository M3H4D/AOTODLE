# This files includes all functions that check each individual coloumn

import db

DEBUT = [
    "The fall of Shiganshina",
    "104th Training Corps",
    "The struggle for Trost",
    "Eve of the Counterattack",
    "The Female Titan",
    "Assault on Stohess"
    "Clash of the Titans",
    "Royal Government",
    "Return to Shiganshina",
    "Marley",
    "War for Paradis"
]

def check_name(current_charID, guess_charID):
    conn = db.connect_to_database()
    cursor = conn.cursor()
    cursor.execute("SELECT Name FROM Characters WHERE CharacterID = ?", (current_charID,))
    curr_charName = cursor.fetchone()
    cursor.execute("SELECT Name FROM Characters WHERE CharacterID = ?", (guess_charID,))
    guess_charName = cursor.fetchone()

    conn.close()

    if curr_charName == guess_charName:
        return 'green'
    else:
        return 'red'
    

def check_gender(current_charID, guess_charID):
    conn = db.connect_to_database()
    cursor = conn.cursor()
    cursor.execute("SELECT Gender FROM Characters WHERE CharacterID = ?", (current_charID,))
    curr_charGender = cursor.fetchone()
    cursor.execute("SELECT Gender FROM Characters WHERE CharacterID = ?", (guess_charID,))
    guess_charGender = cursor.fetchone()

    conn.close()

    if curr_charGender == guess_charGender:
        return 'green'
    else:
        return 'red'
    

def check_affiliation(current_charID, guess_charID):
    conn = db.connect_to_database()
    cursor = conn.cursor()
    cursor.execute("SELECT Affiliation1 FROM Characters WHERE CharacterID = ?", (current_charID,))
    curr_charAf1 = cursor.fetchone()
    cursor.execute("SELECT Affiliation2 FROM Characters WHERE CharacterID = ?", (current_charID,))
    curr_charAf2 = cursor.fetchone()
    cursor.execute("SELECT Affiliation1 FROM Characters WHERE CharacterID = ?", (guess_charID,))
    guess_charAf1 = cursor.fetchone()
    cursor.execute("SELECT Affiliation2 FROM Characters WHERE CharacterID = ?", (guess_charID,))
    guess_charAf2 = cursor.fetchone()

    comparion = []

    if guess_charAf1 == curr_charAf1:
        comparion.append('green')
    elif guess_charAf1 == curr_charAf2:
        comparion.append('yellow')
    else:
        comparion.append('red')

    if guess_charAf2 == curr_charAf2:
        comparion.append('green')
    elif guess_charAf2 == curr_charAf1:
        comparion.append('yellow')
    else:
        comparion.append('red')

    conn.close()

    return comparion


def check_residence(current_charID, guess_charID):
    conn = db.connect_to_database()
    cursor = conn.cursor()
    cursor.execute("SELECT Residence FROM Characters WHERE CharacterID = ?", (current_charID,))
    curr_charResidence = cursor.fetchone()
    cursor.execute("SELECT Residence FROM Characters WHERE CharacterID = ?", (guess_charID,))
    guess_charResidence = cursor.fetchone()

    conn.close()

    if curr_charResidence == guess_charResidence:
        return 'green'
    else:
        return 'red'


def check_status(current_charID, guess_charID):
    conn = db.connect_to_database()
    cursor = conn.cursor()
    cursor.execute("SELECT Alive FROM Characters WHERE CharacterID = ?", (current_charID,))
    curr_charStatus = cursor.fetchone()
    cursor.execute("SELECT Alive FROM Characters WHERE CharacterID = ?", (guess_charID,))
    guess_charStatus = cursor.fetchone()

    conn.close()

    if curr_charStatus == guess_charStatus:
        return 'green'
    else:
        return 'red'
    

def check_TK(current_charID, guess_charID):
    conn = db.connect_to_database()
    cursor = conn.cursor()
    cursor.execute("SELECT TitanKills FROM Characters WHERE CharacterID = ?", (current_charID,))
    curr_charTK = cursor.fetchone()
    cursor.execute("SELECT TitanKills FROM Characters WHERE CharacterID = ?", (guess_charID,))
    guess_charTK = cursor.fetchone()

    conn.close()

    if curr_charTK > guess_charTK:
        return 'up'
    elif curr_charTK < guess_charTK:
        return 'down'
    else:
        return 'green'

    
def check_TP(current_charID, guess_charID):
    conn = db.connect_to_database()
    cursor = conn.cursor()
    cursor.execute("SELECT TitanPowers FROM Characters WHERE CharacterID = ?", (current_charID,))
    curr_charTP = cursor.fetchone()
    cursor.execute("SELECT TitanPowers FROM Characters WHERE CharacterID = ?", (guess_charID,))
    guess_charTP = cursor.fetchone()

    conn.close()

    if curr_charTP == guess_charTP:
        return 'green'
    else:
        return 'red'


def check_debut(current_charID, guess_charID):
    conn = db.connect_to_database()
    cursor = conn.cursor()
    cursor.execute("SELECT Debut FROM Characters WHERE CharacterID = ?", (current_charID,))
    curr_charDebut = cursor.fetchone()
    cursor.execute("SELECT Debut FROM Characters WHERE CharacterID = ?", (guess_charID,))
    guess_charDebut = cursor.fetchone()

    conn.close()

    if DEBUT.index(curr_charDebut[0]) > DEBUT.index(guess_charDebut[0]):
        return 'up'
    elif DEBUT.index(curr_charDebut[0]) < DEBUT.index(guess_charDebut[0]):
        return 'down'
    else:
        return 'green'  
    