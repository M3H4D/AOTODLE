from flask import Blueprint, render_template, request
import db

classic_bp = Blueprint('classic', __name__)

names = []

@classic_bp.route('/classic', methods=['POST','GET'])
def classic():
    
    if request.method == 'POST':
        if db.check_name_in_database(request.form['name']):
            names.append(request.form['name'])
    rows = db.get_all_saved_characters(names)
    return render_template('classic.html', characters=rows)
