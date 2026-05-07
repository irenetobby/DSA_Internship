from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

# Load Model Bundle
with open('popularity_model.pkl', 'rb') as f:
    bundle = pickle.load(f)
    model = bundle['model']
    encoders = bundle['encoders']

def gen_ai_strategy(category, genre):
    """Simulates GenAI Strategy Suggestions"""
    strategies = {
        'High': f"Success Predicted! Strategy: Launch international marketing and seek translation rights for the {genre} market.",
        'Medium': f"Good potential. Strategy: Run targeted social media campaigns to boost 'Review Density'.",
        'Low': f"Niche Audience. Strategy: Re-evaluate your 'Price Bucket' or optimize the book description for better engagement."
    }
    return strategies.get(category, "Expand your digital presence.")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # 1. Initialize the 'data' dictionary first!
    data = {
        'Language': request.form['Language'].strip().capitalize(),
        'Genre': request.form['Genre'].strip().capitalize(),
        'Format': request.form['Format'].strip().capitalize(),
        'Price': float(request.form['Price']),
        'Pages': int(request.form['Pages']),
        'Reviews': 100  # Or capture this from a form field if you added one
    }

    # 2. Dynamic Feature Engineering
    # Now that 'data' exists, you can add new keys to it
    data['Review_Density'] = data['Reviews'] / data['Pages']
    
    if data['Price'] <= 400: 
        data['Price_Bucket'] = 'Budget'
    elif data['Price'] <= 900: 
        data['Price_Bucket'] = 'Mid'
    else: 
        data['Price_Bucket'] = 'Premium'
    
   
    # 3. Encode and Predict
    input_df = pd.DataFrame([data])
    for col in ['Language', 'Genre', 'Format', 'Price_Bucket']:
        input_df[col] = encoders[col].transform(input_df[col].astype(str))
        
    prediction = model.predict(input_df[bundle['features']])[0]
    
    # 4. Generate GenAI recommendation
    recommendation = gen_ai_strategy(prediction, data['Genre'])
    
    return render_template('index.html', prediction=prediction, strategy=recommendation)

if __name__ == '__main__':
    app.run(debug=True)