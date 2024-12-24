from flask import Blueprint, render_template, request, redirect, url_for, session, flash
import db
import random
import char

classic_bp = Blueprint('classic', __name__)

no_of_chars = db.number_of_characters()

names = []
mistakeColors = []


# Classic game loop
@classic_bp.route('/classic', methods=['POST','GET'])
def classic():

    found = False

    if request.method == 'POST':
        if db.check_name_in_database(request.form['name']) and not (session['current_char'] == db.get_characterID(request.form['name'])):
            names.append(request.form['name'])
            mName = char.check_name(session['current_char'], db.get_characterID(request.form['name']))
            mGender = char.check_gender(session['current_char'], db.get_characterID(request.form['name']))
            mA1 = 0
            mA2 = 0
            mResidence = char.check_residence(session['current_char'], db.get_characterID(request.form['name']))
            mStatus = char.check_status(session['current_char'], db.get_characterID(request.form['name']))
            mTK = char.check_TK(session['current_char'], db.get_characterID(request.form['name']))
            mTP = char.check_TP(session['current_char'], db.get_characterID(request.form['name']))
            mDebut = 0

            mistakeColors.append((mName,mGender,'yellow','red',mResidence, mStatus,mTK,mTP,'yellow'))
            found = False
        elif db.check_name_in_database(request.form['name']) and  (session['current_char'] == db.get_characterID(request.form['name'])):
            found = True



    print(names)
    print(mistakeColors)
    
    rows = db.get_all_saved_characters(names)

    
    return render_template('classic.html', characters=rows, found=found,mistakeColors=mistakeColors)

#Starting or reseting a game
@classic_bp.route('/classic/start', methods=['POST','GET'])
def start_game():

    
    session['current_char'] = random.randint(1,no_of_chars)
    print('Current char: ', session['current_char'] )
    
    names.clear()
    mistakeColors.clear()
    return redirect(url_for('classic.classic'))
