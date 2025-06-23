from flask import Flask, request, jsonify, render_template
import pickle 
import os
import numpy as np



'''
app=Flask(__name__)
@app.route('/')
def home():
    return 'Model is running. Flask app is working'

if __name__ =='__main__':
    app.run(debug=True)
'''

# Initialize flask app
app=Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, 'best_model.pkl')

# Load the trained model
with open(model_path, 'rb') as f:
    model=pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')


# predict route
@app.route('/predict', methods=['POST'])
def predict():
    try:
        open_price = float(request.form['open_price'])
        prev_close = float(request.form['prev_close'])
        ma_7 = float(request.form['ma_7'])

        features=np.array([[open_price, prev_close, ma_7]])
        prediction=model.predict(features)[0]
        prediction=round(prediction, 2)

        return render_template('index.html', prediction=prediction)
    
    except Exception as e:
        return f"Error: {str(e)}"


# Run the app
if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')



'''
# Home route
@app.route('/')
def home():
    return 'Model is running. Flask app is working!'
if __name__=='__main__':
    app.run(debug=True)
'''

'''
# predict route
@app.route('/predict', methods=['GET'])
def predict():
    try:
        open_price = float(request.args.get('open_price'))
        prev_close = float(request.args.get('prev_close'))
        ma_7 = float(request.args.get('ma_7'))

        # Prepare input data
        input_data = [[open_price, prev_close, ma_7]]
        prediction = model.predict(input_data)

        # Return the result
        return jsonify({'Prediction' : float(prediction[0])})
    
    except Exception as e:
        return jsonify({'Error': str(e)})
'''



