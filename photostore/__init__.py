from flask import Flask, render_template, url_for, request, redirect
import os

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/templates/family.html', methods=['GET', 'POST'])
def family():
    if request.method == "POST":
        file = request.files["photo"]
        file.save(os.path.join('C:/Users/cglas/PycharmProjects/photostore/static/images', file.filename))
        return file
    return render_template('family.html')

@app.route('/templates/urban.html')
def urban():
    return render_template('urban.html')

@app.route('/templates/rural.html')
def rural():
    return render_template('rural.html')

@app.route('/templates/stylistic.html')
def stylistic():
    return render_template('stylistic.html')

@app.route('/templates/animals.html')
def animals():
    return render_template('animals.html')

@app.route('/templates/profile.html')
def profile():
    return render_template('profile.html')

if __name__ == ('__main__'):
    app.run()
