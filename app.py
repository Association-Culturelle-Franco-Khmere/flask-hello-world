# from flask import Flask
# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Wesh mec!'

from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def respond():
    print(request.json);
    return Response(status=200)
