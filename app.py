from flask import Flask, render_template
from jinja2.utils import markupsafe

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

if __name__ == '__master__':
    app.run(debug=True,port=3000,host='0.0.0.0')