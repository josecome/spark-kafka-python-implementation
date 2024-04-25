from kafka import KafkaProducer
from flask import Flask, request, redirect, url_for, session, render_template
import json

app = Flask(__name__, template_folder='templates')

producer = KafkaProducer(bootstrap_servers=['localhost:9092'], api_version=(0,1,0))

@app.route('/form', methods=['GET', 'POST'])
def form():    
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['password'] # c2gx42pwhp9ym4x5p0brniturk834j
        
        if all(v is not None for v in [firstname, lastname]):
            _str = '{ "firstname": "' + str(firstname) + '", "lastname": "' + str(lastname) + '"}'
            producer.send('my_favorite_topic', bytes(str(_str), encoding='utf8'))
            producer.flush()

            return "Successfully submitted!"
        else:
            msg = 'Please, fill FirstName and LastName!'
            return redirect(url_for('form',msg=msg))
        
    return  render_template('form.html')
