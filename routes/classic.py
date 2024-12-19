from flask import Blueprint, render_template, request, redirect, url_for, session
import db
import random

classic_bp = Blueprint('classic', __name__)

no_of_chars = db.number_of_characters()

global names 
names = []

@classic_bp.route('/classic', methods=['POST','GET'])
def classic():
    found = False

    if request.method == 'POST':
        if db.check_name_in_database(request.form['name']) and not (session['current_char'] == db.get_characterID(request.form['name'])):
            names.append(request.form['name'])
            found = False
        elif db.check_name_in_database(request.form['name']) and  (session['current_char'] == db.get_characterID(request.form['name'])):
            found = True

    print(names)
    rows = db.get_all_saved_characters(names)

    
    return render_template('classic.html', characters=rows, found=found)


@classic_bp.route('/classic/start', methods=['POST','GET'])
def start_game():

    
    session['current_char'] = random.randint(1,no_of_chars)
    print('Current char: ', session['current_char'] )
    
    names.clear()
    return redirect(url_for('classic.classic'))
