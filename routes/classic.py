from flask import Blueprint, render_template

classic_bp = Blueprint('classic', __name__)

@classic_bp.route('/classic')
def classic():
    return render_template('classic.html')