from pyrogram import Client, filters
import time as t

api_id = null #api_id
api_hash = null #api_hash
app = Client("my_account", api_id, api_hash)


@app.on_message(filters.command(["vzlom"], prefixes="/"))
def vzlom(client, message):
		app.send_message(message.chat.id, 'Взлом хуя...🌀', reply_to_message_id=message.message_id)
		t.sleep(1)
		try:
			app.edit_message_text(message.chat.id, message.message_id+1, f'**Хуй [{message.reply_to_message.from_user.first_name}](tg://user?id={message.reply_to_message.from_user.id}) успешно взломана!**')
		except BaseException:
			app.edit_message_text(message.chat.id, message.message_id+2, f'**Хуй [{message.reply_to_message.from_user.first_name}](tg://user?id={message.reply_to_message.from_user.id}) успешно взломана!**')

@app.on_message(filters.command(["del"], prefixes="/"))
def delcom(client, message):
	try:
		app.kick_chat_member(message.chat.id, message.reply_to_message.from_user.id)
		app.send_message(message.chat.id, "Вон отсюда! Пользователь забанен.")	
	except BaseException:
		app.send_message(message.chat.id, "Ошибка")

app.run()
