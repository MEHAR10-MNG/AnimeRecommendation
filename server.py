from flask import Flask, request, jsonify
import pandas as pd
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load anime data
anime_data = pd.read_csv('anime.csv')

# Recommendation function
def get_recommendations(anime_name):
    recommendations = anime_data[anime_data['name'].str.contains(anime_name, case=False)]
    return recommendations[['name', 'genre', 'rating']].head(5).to_dict(orient='records')

@app.route('/recommend', methods=['GET'])
def recommend():
    anime_name = request.args.get('anime')
    if not anime_name:
        return jsonify({"error": "No anime name provided"}), 400
    
    recommendations = get_recommendations(anime_name)
    if not recommendations:
        return jsonify({"error": "No recommendations found"}), 404
    
    return jsonify(recommendations)

if __name__ == '__main__':
    app.run(debug=True)

    