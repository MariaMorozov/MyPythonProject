from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello():
    print("GGG")
    return "Hello From Flask"


app.run()
