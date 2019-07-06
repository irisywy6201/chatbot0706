
@app.route("/callback",methods=['POST'])
def callback():
	signature = request.headers['X-Line-Signarure']

	body = request.get_data(as_text=True)
	app.logger.info("Request body:" + body)

	try:
		handler.handle(body,signature)
	except InvalidSignatureError:
		print("Invalid Signature plz check your channel access token/channel secret")
		abort(400)

	return 'ok!!'

@handler.add(MessageEvent,message=TextMessage)
def handle_message(event):
	line_bot_api.reply_message(
		event.reply_token,
		TextSendMessage(text=event.message.text))
