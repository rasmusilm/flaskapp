import time
import random
# import raspi cpu params
#from gpiozero import CPUTemperature
# Flask for web-dev
from flask import Flask, render_template, jsonify
import json

def cpu_temp():
    return round(random.random()*100, 2)

# define app
app = Flask('Testing')

@app.route('/')
def index():   
    temps = cpu_temp()
    return render_template('index.html', variable=temps)

@app.route('/api')
def api():
    temps = cpu_temp()
    return jsonify({"temp": temps})

@app.route('/test')
def test():
    return render_template('test.html')

if __name__ == '__main__':
    app.run()