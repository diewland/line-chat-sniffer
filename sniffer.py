from flask import Flask, request, abort
from linebot import ( LineBotApi, WebhookHandler)
from linebot.exceptions import ( InvalidSignatureError )
from linebot.models import ( MessageEvent, TextMessage, TextSendMessage )

ACCESS_TOKEN = '' # TODO change to channel access token
SECRET = ''       # TODO change to channel secret

app = Flask(__name__)

line_bot_api = LineBotApi(ACCESS_TOKEN)
handler = WebhookHandler(SECRET)

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    #
    # write your logic here
    #
    # MessageEvent - https://github.com/line/line-bot-sdk-python/blob/master/linebot/models/events.py
    # SourceUser   - https://github.com/line/line-bot-sdk-python/blob/master/linebot/models/sources.py
    # TextMessage  - https://github.com/line/line-bot-sdk-python/blob/master/linebot/models/messages.py
    #
    print("[%s] %s" % (event.source.user_id, event.message.text))

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, threaded=True)
