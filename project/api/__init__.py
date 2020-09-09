from flask import Blueprint, make_response, jsonify

bp = Blueprint('api', __name__)


@bp.route('/test', methods=['GET'])
def test():
    """
    Test
    """
    responseObject = {
        'status': 'success',
        'message': f"It's just a test",
        'data': {
            'test': "test"
        }
    }
    return make_response(jsonify(responseObject)), 200
