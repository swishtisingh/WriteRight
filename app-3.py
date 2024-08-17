import requests
from flask import Flask,render_template,url_for,jsonify
from flask import request as req
from flask_cors import CORS

app = Flask(__name__, template_folder='template')
CORS(app)

@app.route("/", methods = ["GET", "POST"])

def Index():
  return(render_template('index.html'))

@app.route('/Summarise', methods = ['GET','POST'])

def Summarise():
   if req.method == 'POST':
        try:

            API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
            headers = {"Authorization": f"Bearer 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"}
            data = req.json['userInput']
            #print(data,type(data))
            minL = 20
            maxL = int(req.json['maxL'])

            def query(payload):
                response = requests.post(API_URL, headers=headers, json=payload)
                print(response)
                return response.json()
            
            output = query({
                "inputs": data,
                'parameters':{'min_length':minL, 'max_length':maxL},
            })

            #print(output[0]['summary_text'])
            return jsonify({'summary_text': output[0]['summary_text']})

        except Exception as e:
            return jsonify({'error': str(e)}), 500

   else:
       return jsonify({'error': 'Method not allowed'}), 405

if __name__ == '__main__':
    app.debug = True
    app.run()
