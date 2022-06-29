from flask import Flask, jsonify, request
from models import setup_db, Plant

def create_app(test_config=None):
    app = Flask(__name__)
    setup_db(app)

    @app.route('/plants', methods=['GET','POST'])
    #@cross_origin
    def get_plants():
        # Implement pagination
        page = request.args.get('page', 1, type=int)
        start = (page - 1) * 10
        end = start + 10

        plants = Plant.query.all()
        formatted_plants = [plant.format() for plant in plants]
        return jsonify({
            'success': True,
            'plants':formatted_plants[start:end],
            'total_plants':len(formatted_plants)
            })

    return app