from flask import jsonify
from . import api_v1

@api_v1.route('/status')
def status():
    return jsonify({'status': 'API is running'})