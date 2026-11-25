from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/reserve', methods=['POST'])
def reserve():

    name = request.form['guest_name']
    email = request.form['email']
    date = request.form['checkin']
    room = request.form['room_type']

    return f"Reservation Successful! Welcome {name}. Your room type is {room}."

if __name__ == '__main__':
    app.run(debug=True)