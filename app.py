# from flask import Flask
# import os

# app = Flask(__name__)


# @app.route('/')
# def home():
#     return 'Hello World!!!'


# if __name__ == "__main__":
#     port = int(os.environ.get('PORT', 5000))
#     app.run(debug=True, host='0.0.0.0', port=port)
from flask import Flask
app = Flask(__name__)
import os
@app.route('/')
def hello():
    return 'Hello World!\n'
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
