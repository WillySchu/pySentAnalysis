from flask import Flask, request
from analysis import get_score
import json

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods = ['POST'])
def sent():
    return json.dumps([get_score(tweet['text']) for tweet in request.json])

if __name__ == '__main__':
    app.run()
