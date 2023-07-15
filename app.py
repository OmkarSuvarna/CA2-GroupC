# entry point
from flask import Flask, render_template, url_for
app = Flask(__name__, template_folder='frontend', static_folder='frontend/css')

patient = [
    {
        'id':'100',
        'firstName' : 'John',
        'lastName' : 'Snow',
        'age' : '25',
        'gender' : 'Male'
    },
    {
        'id':'101',
        'firstName' : 'Arya',
        'lastName' : 'Stark',
        'age' : '20',
        'gender' : 'Female'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', patient=patient)

@app.route("/second-page")
def about():
    return "<h1>Second Page will go here</h1>"

# so we do not need to set enviornment variable again, can run directly using python
if __name__ == '__main__':
    app.run(debug=True)