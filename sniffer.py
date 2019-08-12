import os
from flask import Flask, request, abort
from pprint import pprint as pp

app = Flask(__name__)

def print_text(tag, resp):
    if len(resp['events']) > 0:
        this_evt = resp['events'][0]
        this_msg = this_evt.get('message', {})
        this_src = this_evt.get('source', {})

        # filter only text by user
        if (this_msg.get('type') == 'text') and this_src.get('type') == 'user' :
            info = {
                'user_id': this_src.get('userId'),
                'text': this_msg.get('text'),
                'timestamp': this_evt.get('timestamp'),
                'destination': resp.get('destination'),
            }
            print(tag, info)

@app.route("/callback", methods=['POST'])
def callback():

    tag = '<1337>'
    resp = request.json

    print(tag, resp)
    #print_text(tag, resp)

    return 'OK'

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, threaded=True)
