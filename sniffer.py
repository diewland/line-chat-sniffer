from flask import Flask, request, abort
from pprint import pprint as pp

app = Flask(__name__)

def print_text(tag, req):
    if len(req['events']) > 0:
        this_evt = req['events'][0]
        this_msg = this_evt.get('message', {})
        this_src = this_evt.get('source', {})

        # filter only text
        if (this_msg.get('type') == 'text'):
            info = {
                'src_type': this_src.get('type'),
                'user_id': this_src.get('userId'),
                'group_id': this_src.get('groupId'),
                'text': this_msg.get('text'),
                'timestamp': this_evt.get('timestamp'),
                'destination': req.get('destination'),
            }
            print(tag, info)

@app.route("/callback", methods=['POST'])
def callback():

    tag = '<1337>'
    req = request.json

    #print(tag, req)
    print_text(tag, req)

    return 'OK'

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, threaded=True)
