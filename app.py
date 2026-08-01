from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained model
try:
    model = joblib.load('model.pkl')
except Exception as e:
    print(f"Error loading model: {e}")

# Serve the frontend HTML page
@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Accept patient details as JSON input
        data = request.get_json()
        
        # Ensure 'features' key exists in the JSON payload
        if 'features' not in data:
            return jsonify({"error": "Missing 'features' key in JSON payload."}), 400
        
        # Convert features to a 2D numpy array for the model
        features = np.array(data['features']).reshape(1, -1)
        
        # Make the prediction
        prediction = model.predict(features)[0]
        
        # Return the prediction as JSON
        result = "Heart Disease Detected" if prediction == 1 else "No Heart Disease Detected"
        
        return jsonify({"prediction": result})
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)