from flask import Blueprint, url_for
from werkzeug.utils import redirect

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/hello')
def hello_pybo():
    return 'Hello, Pybo'

@bp.route('/')
def index():
    return redirect(url_for('question._list'))
    #question._list에 해당하는 url로 리다이렉트 할 수 있도록
    #question._list : (question:블루프린트 이름 / _list 블루프린트에 등록된 함수명)
    # -> /question/list/ url반환
