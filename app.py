from flask import Flask, request, jsonify
from flask_cors import CORS
import util

app = Flask(__name__)
CORS(app)  # Enable CORS to allow frontend requests

@app.route('/predict_cluster', methods=['POST'])
def predict_cluster_route():
    data = request.json
    try:
        income = float(data.get('income'))
        spending_score = float(data.get('spending_score'))
    except (TypeError, ValueError):
        return jsonify({"predicted_cluster": "Invalid input"}), 400

    cluster = util.predict_cluster(income, spending_score)
    return jsonify({"predicted_cluster": cluster})

if __name__ == '__main__':
    print("Starting Flask server...")
    util.load_model()
    app.run(debug=True)
