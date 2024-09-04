from flask import Flask, render_template

app = Flask(__name__)

# Define a route for the home page
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/reports')
def reports():
    return render_template('reports.html')
    
@app.route('/casting')
def casting():
    return render_template('casting_values_automatic.html')

@app.route('/desired')
def desired():
    return render_template('desired_input.html')

@app.route('/initial')
def initial():
    return render_template('Initial_casting_values.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/manual')
def manual():
    return render_template('manual_checking.html')

@app.route('/prediction')
def prediction():
    return render_template('prediction.html')

@app.route('/usecase')
def usecase():
    return render_template('use_case.html')

if __name__ == '__main__':
    app.run(debug=True)