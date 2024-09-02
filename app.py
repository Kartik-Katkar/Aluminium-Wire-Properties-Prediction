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

if __name__ == '__main__':
    app.run(debug=True)