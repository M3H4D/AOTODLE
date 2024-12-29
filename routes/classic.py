from flask import Blueprint, render_template, request, redirect, url_for, session, flash
import db
import random
import char

classic_bp = Blueprint('classic', __name__)

no_of_chars = db.number_of_characters()

names = []
mistakeColors = []
found = False

# Classic game loop
@classic_bp.route('/classic', methods=['POST','GET'])
def classic():

    global found

    if request.method == 'POST':
        if request.form['name'] not in names:
            if (db.check_name_in_database(request.form['name']) and not found):
                names.insert(0,request.form['name'])
                mName = char.check_name(session['current_char'], db.get_characterID(request.form['name']))
                mGender = char.check_gender(session['current_char'], db.get_characterID(request.form['name']))
                mA = char.check_affiliation(session['current_char'], db.get_characterID(request.form['name']))
                mResidence = char.check_residence(session['current_char'], db.get_characterID(request.form['name']))
                mStatus = char.check_status(session['current_char'], db.get_characterID(request.form['name']))
                mTK = char.check_TK(session['current_char'], db.get_characterID(request.form['name']))
                mTP = char.check_TP(session['current_char'], db.get_characterID(request.form['name']))
                mDebut = char.check_debut(session['current_char'], db.get_characterID(request.form['name']))

                mistakeColors.insert(0,(mName,mGender,mA,mResidence, mStatus,mTK,mTP,mDebut))
            if (session['current_char'] == db.get_characterID(names[0])):
                found = True
            else:
                found = False



    print(names)
    print(mistakeColors)
    
    rows = db.get_all_saved_characters(names)
    namesCount = len(names)
    
    return render_template('classic.html', characters=rows, found=found,mistakeColors=mistakeColors, score=namesCount)

#Starting or reseting a game
@classic_bp.route('/classic/start', methods=['POST','GET'])
def start_game():

    global found 

    session['current_char'] = random.randint(1,no_of_chars)
    print('Current char: ', session['current_char'] )
    
    names.clear()
    mistakeColors.clear()
    found = False
    return redirect(url_for('classic.classic'))
