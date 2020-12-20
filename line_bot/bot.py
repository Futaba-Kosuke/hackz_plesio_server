from settings import LINE_CHANNEL_ACCESS_TOKEN

from linebot import (
	LineBotApi
)
from linebot.models import TextSendMessage

# 環境変数取得
line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)


def broadcast(text: str):
	text_messages = TextSendMessage(
		text=text
	)
	line_bot_api.broadcast(messages=text_messages)
