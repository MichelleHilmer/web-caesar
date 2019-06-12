from flask import Flask

app = Flask(__name__)
app.confit['DEBUG'] = True

@app.route("/")
def index():
    return "Hello World"

app.run()