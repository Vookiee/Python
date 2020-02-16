from flash import Flask, render_template
from flash import request

app = Flash(__name__)

@app.route('/')
def index():
    return render_template('index.html')


print("hello")