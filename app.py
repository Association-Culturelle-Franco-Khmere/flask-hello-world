# from flask import Flask
# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Wesh mec!'

from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def respond():
    fave_language = request.json;
    print("I like coding in " + fave_language + " the most")
    return Response(status=200)
