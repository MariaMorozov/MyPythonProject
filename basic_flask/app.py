from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return "This is Flask!"


app.run(host='0.0.0.0', port='5000')

"""
0- requirements: flask
1- Dockerfile
2- docker-compose 
"""


