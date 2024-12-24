# This files includes all functions that check each individual coloumn

import db

def check_name(current_charID, guess_charID):
    conn = db.connect_to_database()
    cursor = conn.cursor()
    cursor.execute("SELECT Name FROM Characters WHERE CharacterID = ?", (current_charID,))
    curr_charName = cursor.fetchone()
    cursor.execute("SELECT Name FROM Characters WHERE CharacterID = ?", (guess_charID,))
    guess_charName = cursor.fetchone()

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

    if curr_charGender == guess_charGender:
        return 'green'
    else:
        return 'red'
    

def check_residence(current_charID, guess_charID):
    conn = db.connect_to_database()
    cursor = conn.cursor()
    cursor.execute("SELECT Residence FROM Characters WHERE CharacterID = ?", (current_charID,))
    curr_charResidence = cursor.fetchone()
    cursor.execute("SELECT Residence FROM Characters WHERE CharacterID = ?", (guess_charID,))
    guess_charResidence = cursor.fetchone()

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

    if curr_charTK > guess_charTK:
        return 2
    elif curr_charTK < guess_charTK:
        return 1
    else:
        return 0

    


def check_TP(current_charID, guess_charID):
    conn = db.connect_to_database()
    cursor = conn.cursor()
    cursor.execute("SELECT TitanPowers FROM Characters WHERE CharacterID = ?", (current_charID,))
    curr_charTP = cursor.fetchone()
    cursor.execute("SELECT TitanPowers FROM Characters WHERE CharacterID = ?", (guess_charID,))
    guess_charTP = cursor.fetchone()

    if curr_charTP == guess_charTP:
        return 'green'
    else:
        return 'red'

    