from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

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

@app.route('/desired', methods=['GET', 'POST'])
def desired():
    if request.method == 'POST':
        elongitivity = request.form.get('elongitivity')
        uts = request.form.get('uts')
        conductivity = request.form.get('conductivity')
        # Optionally: Process form data or store it as needed
        return redirect(url_for('initial'))
    return render_template('desired_input.html')

@app.route('/initial')
def initial():
    return render_template('Initial_casting_values.html')

# @app.route('/login')
# def login():
#     return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Process login information here (authentication)
        return redirect(url_for('prediction'))
    return render_template('login.html')


@app.route('/manual')
def manual():
    return render_template('manual_checking.html')

@app.route('/prediction', methods=['GET', 'POST'])
def prediction():
    if request.method == 'POST':
        # Process form data if needed
        # Redirect or render the prediction page as required
        return render_template('prediction.html')
    return render_template('prediction.html')


@app.route('/usecase')
def usecase():
    return render_template('use_case.html')
@app.route('/threed')
def threed():
    return render_template('threed.html')

if __name__ == '__main__':
    app.run(debug=True)
