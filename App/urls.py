from flask import Blueprint

from views import sign_up, login, add_task

bp = Blueprint('api', __name__)
@bp.route('/sign_up', methods=['POST'])
def sign_up_route():
    return sign_up()

@bp.route('/login', methods= ['POST'])
def login_route():
    return login()

@bp.route('/add_task', methods=['POST'])
def add_task_route():
    return add_task()