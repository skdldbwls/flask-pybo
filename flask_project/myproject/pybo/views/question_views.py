from ..forms import QuestionForm

from flask import Blueprint, render_template

from pybo.models import Question

bp = Blueprint('question', __name__, url_prefix='/question') #main_view와 다른 점 : url_prefix


@bp.route('/list/') #main_view와 다른 점 : / -> /list/
def _list(): #main_view와 다른 점 : index -> _list
    question_list = Question.query.order_by(Question.create_date.desc())
    return render_template('question/question_list.html', question_list=question_list)


@bp.route('/detail/<int:question_id>/')
def detail(question_id):
    question = Question.query.get_or_404(question_id)
    return render_template('question/question_detail.html', question=question)


@bp.route('/create/')
def create():
    form = QuestionForm()
    return render_templete('question/question_form.html', form=form)
