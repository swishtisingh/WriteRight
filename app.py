import requests
from flask import Flask, render_template, url_for, jsonify
from flask import request as req
from flask_cors import CORS

app = Flask(__name__, template_folder='template')
CORS(app, resources={r"/grammer": {"origins": "chrome-extension://daaaleeohlfokjfihhapljbmapfkploh"}})

@app.route("/", methods=["GET", "POST"])
def Index():
    return render_template('index.html')

@app.route('/grammer', methods=['POST'])
def grammer():
    if req.method == 'POST':
        try:
            # Verify that request is JSON and has the correct fields
            if not req.is_json:
                return jsonify({'error': 'Request must be JSON'}), 400

            # Extract JSON data
            data = req.json.get('userInput')
            maxL = req.json.get('maxL')

            if not data or not maxL:
                return jsonify({'error': 'Missing userInput or maxL in the request body'}), 400

            API_URL = "https://api-inference.huggingface.co/models/vennify/t5-base-grammar-correction"
            headers = {"Authorization": "Bearer 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"}
            minL = 20

            # Define function to query Hugging Face API
            def query(payload):
                response = requests.post(API_URL, headers=headers, json=payload)
                response.raise_for_status()  # Will raise an error for bad responses
                return response.json()

            # Call the API with the user input
            output = query({
                "inputs": data,
                'parameters': {'min_length': minL, 'max_length': int(maxL)},
            })

            # Check if the response contains the expected data
            if 'summary_text' in output[0]:
                return jsonify({'summary_text': output[0]['summary_text']})
            else:
                return jsonify({'error': 'Unexpected API response format'}), 500

        except requests.exceptions.RequestException as e:
            return jsonify({'error': f'API request failed: {str(e)}'}), 500
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    return jsonify({'error': 'Method not allowed'}), 405

if __name__ == '__main__':
    app.debug = True
    app.run()
