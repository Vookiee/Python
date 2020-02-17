from flask import Flask, render_template
from flask import request
import sqlite3
import http.server

app = Flask(__name__,template_folder='index')

@app.route('/')
def index():
    return render_template('index.html')


# @app.route('/register', methods=['POST'])
# def register():
#     print(request.form.values)
#     print(request.form.get('payment', 'Not set'))
    
    
# app.run(host='0.0.0.0', port = 5000)
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')