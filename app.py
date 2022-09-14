from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)
import os

app = Flask(__name__)

line_bot_api = LineBotApi(os.environ['YOUR_CHANNEL_ACCESS_TOKEN'])
handler = WebhookHandler(os.environ['YOUR_CHANNEL_SECRET'])

diary_mode_flag = False

@app.route("/")
def test():
    return "<h1>Tests</h1>"

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
def handle_message(event, diary_mode_flag):
    if "日記" in event.message.text:
        if not diary_mode_flag :
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text="どうぞ"))

            #deepl
        else:
            diary_mode_flag = True
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text="作成中"))

            # line_bot_api.reply_message(
            #     event.reply_token,
            #     TextSendMessage(text="作成中"))

        line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))

    else :
        print()


#プッシュメッセージ
@app.route("/send/<message>")
def push_message(message):
    line_bot_api.broadcast([TextSendMessage(text=message)])