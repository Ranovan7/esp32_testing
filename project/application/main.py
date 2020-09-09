from flask import Blueprint, render_template

bp = Blueprint('main', __name__)


@bp.route('/', methods=['GET'])
def test():
    """
    Test
    """
    return render_template('main/test.html',
                            message="This is a test!",
                            followup="Wouldn't you agree, Jean Pierre Polnareff?")
