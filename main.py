from flask import Flask, request
from caesar import encrypt

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius:10px;
            }
            textarea{
                margin:10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
        <form action="" method="post">
            <label for="rot">Rotate by:</label>
            <input type="text" name="rot" value= 0 />
            <br>
            <textarea name="text"> </textarea>
            <input type="submit"/>
        </form>
    </body>
</html>

"""

@app.route("/")
def index():
    return form

@app.route("/encode", methods=['POST'])
def encode(rot,text):
    rot = request.form['rot']
    text = request.form['text']
    new_message = encrypt(text,rot)
    return '<h1>' + new_message + '</h1>'




app.run()