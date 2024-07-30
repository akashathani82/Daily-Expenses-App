from flask import Flask, jsonify
from flask_restful import Api
from models.user import db
from resources.user import UserResource, UserListResource
from resources.expense import ExpenseResource, ExpenseListResource

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///expenses.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
api = Api(app)

with app.app_context():
    db.create_all()

api.add_resource(UserResource, '/users/<int:user_id>')
api.add_resource(UserListResource, '/users')
api.add_resource(ExpenseResource, '/expenses/<int:expense_id>')
api.add_resource(ExpenseListResource, '/expenses')

@app.errorhandler(404)
def not_found_error(error):
    return jsonify({"error": "Not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500

@app.errorhandler(400)
def bad_request_error(error):
    return jsonify({"error": "Bad request"}), 400

if __name__ == '__main__':
    app.run(debug=True)
