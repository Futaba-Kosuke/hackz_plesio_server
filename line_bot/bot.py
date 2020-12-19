from settings import LINE_CHANNEL_ACCESS_TOKEN

from linebot import (
	LineBotApi
)
from linebot.models import ImageSendMessage

# 環境変数取得
line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)


def broadcast(image_url: str):
	image_messages = ImageSendMessage(
		original_content_url=image_url,
		preview_image_url=image_url
	)
	line_bot_api.broadcast(messages=image_messages)
