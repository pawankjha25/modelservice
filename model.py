from flask import Flask,request, jsonify
app = Flask(__name__)

@app.route('/', methods=['GET'])
def test_service():
    return jsonify({'response': 'Model service is live!'})

@app.route('/checkFraud', methods=['GET','POST'])
def get_fraud_service_response():
    if request.method == 'GET':
        c_name=request.args.get('c_name')
        c_score=int(request.args.get('c_score'))
        if c_score < 600:
            message='Fraud classification'
        else:
            message='Not Fraud classification'

        return jsonify({'c_name':c_name ,'c_score':c_score , 'response': message})

    if request.method == 'POST':
        req_data = request.get_json()
        c_name=req_data['c_name']
        c_score=int(req_data['c_score'])
        if c_score < 600:
            message='Fraud classification'
        else:
            message= 'Not Fraud classification'

        return jsonify({'c_name':c_name ,'c_score':c_score , 'response': message})



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug = True)