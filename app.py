import os

from flask import Flask

app = Flask(__name__)

@app.route('/') # test function
def hello():
    return 'Hello World... again'

# if __name__ == '__main__':
#     app.run(host=os.environ.get("IP"),
#     port=int(os.environ.get("PORT")),
#     debug=True)
    
if __name__ == '__main__':
    app.run(
        # host='http://127.0.0.1',
        port=8080,
        debug=True
    )