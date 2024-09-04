from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Database configuration
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="TechJita@97",
    database="gym_membership"
)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    full_name = request.form['full_name']
    email = request.form['email']
    phone_number = request.form['phone_number']
    membership_plan = request.form['membership_plan']

    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO members (full_name, email, phone_number, membership_plan) VALUES (%s, %s, %s, %s)",
        (full_name, email, phone_number, membership_plan)
    )
    db.commit()

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
