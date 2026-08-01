<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Heart Disease Predictor</title>
    <style> 
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #f4f7f6;
            color: #333;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .container {
            background: #fff;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
            max-width: 500px;
            width: 100%;
        }
        h2 {
            text-align: center;
            margin-bottom: 20px;
            color: #2c3e50;
        }
        .form-group {
            margin-bottom: 20px;
        }
        label {
            display: block;
            font-weight: bold;
            margin-bottom: 8px;
            font-size: 14px;
        }
        input[type="text"] {
            width: 100%;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 5px;
            box-sizing: border-box;
            font-size: 14px;
        }
        button {
            width: 100%;
            padding: 12px;
            background-color: #3498db;
            color: white;
            border: none;
            border-radius: 5px;
            font-size: 16px;
            font-weight: bold;
            cursor: pointer;
            transition: background 0.3s ease;
        }
        button:hover {
            background-color: #2980b9;
        }
        #result {
            margin-top: 25px;
            font-size: 18px;
            font-weight: bold;
            text-align: center;
            padding: 15px;
            border-radius: 5px;
            display: none;
        }
        .detected { background-color: #f8d7da; color: #721c24; border: 1px solid #f5c6cb; }
        .safe { background-color: #d4edda; color: #155724; border: 1px solid #c3e6cb; }
        .error { background-color: #fff3cd; color: #856404; border: 1px solid #ffeeba; }
    </style>
</head>
<body>

    <div class="container">
        <h2>Patient Risk Assessment</h2>
        <form id="predictionForm">
            <div class="form-group">
                <label for="features">Enter 13 Clinical Parameters (Comma-separated)</label>
                <input type="text" id="features" name="features" required 
                       placeholder="e.g., 52, 1, 0, 125, 212, 0, 1, 168, 0, 1.0, 2, 2, 3">
                <small style="color: #7f8c8d; display: block; margin-top: 5px;">
                    Order: Age, Sex, CP, Trestbps, Chol, FBS, RestECG, Thalach, Exang, Oldpeak, Slope, CA, Thal
                </small>
            </div>
            <button type="submit">Predict Heart Disease</button>
        </form>

        <div id="result"></div>
    </div>

    <script>
        document.getElementById('predictionForm').addEventListener('submit', async function(event) {
            event.preventDefault(); // Prevent page refresh
            
            const featuresInput = document.getElementById('features').value;
            // Convert comma-separated string to an array of numbers
            const featuresArray = featuresInput.split(',').map(num => parseFloat(num.trim()));
            const resultDiv = document.getElementById('result');

            // Reset UI
            resultDiv.style.display = 'block';
            resultDiv.className = '';
            resultDiv.innerText = 'Processing...';

            try {
                const response = await fetch('/predict', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ features: featuresArray })
                });

                const data = await response.json();
                
                if (data.error) {
                    resultDiv.className = 'error';
                    resultDiv.innerText = "Error: " + data.error;
                } else {
                    if (data.prediction === "Heart Disease Detected") {
                        resultDiv.className = 'detected';
                        resultDiv.innerText = "⚠️ " + data.prediction;
                    } else {
                        resultDiv.className = 'safe';
                        resultDiv.innerText = "✅ " + data.prediction;
                    }
                }
            } catch (error) {
                resultDiv.className = 'error';
                resultDiv.innerText = "Failed to connect to the server.";
            }
        });
    </script>

</body>
</html>