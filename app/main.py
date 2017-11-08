# Imports:
from flask import Flask, jsonify
from static.controllers.items_controller import items


app = Flask(__name__)
app.register_blueprint(items, url_prefix='/items')
app.debug = True


@app.route('/')
def index():
    return 'Sample Middleware Application'


@app.errorhandler(400)
@app.errorhandler(401)
@app.errorhandler(403)
@app.errorhandler(404)
@app.errorhandler(405)
@app.errorhandler(409)
@app.errorhandler(500)
@app.errorhandler(504)
def handle_errors(e):
    return jsonify({
        'error': {
            'status': e.code,
            'title': e.name,
			'details': e.description,
            'responder': 'middleware'
        }
    }), e.code


if __name__ == '__main__':
    app.run()