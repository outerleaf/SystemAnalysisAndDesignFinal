from flask import Flask, redirect, url_for, render_template, request
import sqlite3 as sql
app = Flask(__name__)

@app.route('/', methods = ['GET'])
def home():
    return render_template('welcome.htm')

@app.route('/login', methods = ['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        user = request.form['un']
        pswd = request.form['pw']
        if user == 'admin' and pswd == 'Panther$':
            return render_template('room_list.htm')
        else:
            return render_template('welcome.htm')
    else:
        return render_template('login.htm')

@app.route('/reservation', methods = ['GET', 'POST'])
def reservation():
    if request.method == 'POST':
        fname = request.form['fname']
        lname = request.form['lname']
        checkin = request.form['checkin']
        checkout = request.form['checkout']
        roomtype = request.form['roomtype']

        cmd = "INSERT INTO reservations (fname, lname, checkin, checkout, roomtype) VALUES ('{0}', '{1}', '{2}', '{3}', '{4}')".format(fname, lname, checkin, checkout, roomtype)
        with sql.connect('database1.db') as conn:
            cur = conn.cursor()
            cur.execute(cmd)
            conn.commit()
            msg = 'Reservation information was successfully added to the database.'
            return render_template('confirmation.htm', msg = msg, fname = fname, lname = lname, checkin = checkin, checkout = checkout, roomtype = roomtype)
    return render_template('reservation.htm')

@app.route('/confirmation', methods = ['GET'])
def confirmation():
    return render_template('confirmation.htm')

@app.route('/room_list', methods = ['GET', 'POST'])
def list_rooms():
    conn = sql.connect('database1.db')
    conn.row_factory = sql.Row

    cmd = 'SELECT * FROM reservations'
    cur = conn.cursor()
    cur.execute(cmd)
    rows = cur.fetchall()
    conn.close()
    return render_template('room_list.htm', rows = rows)

if __name__ == "__main__":
    app.run(debug=True)