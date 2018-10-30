import telebot
from telebot.types import Message, InputTextMessageContent,\
    InlineKeyboardMarkup, InlineKeyboardButton, InlineQueryResultArticle


TOKEN = "612787394:AAF6Z2SnlrF2CPddvH_2oYCUdvi6cE4wiow"

bot = telebot.TeleBot(TOKEN)

USER = set()


@bot.message_handler(commands=["start"])
def message_handler(message: Message):
    bot.reply_to(message, "start command reply")


@bot.message_handler(commands=["help"])
def send_help(message: Message):
    bot.send_message(message.chat.id, "Try to figure out by yourself!")


@bot.edited_message_handler(content_types=["text"], func=lambda message: True)
@bot.message_handler(content_types=["text"], func=lambda message: True)
def reply_message(message: Message):
    if message.from_user.id not in USER:
        bot.send_message(message.chat.id,
                         "Hi, this is your first message! How are you?")
        USER.add(message.from_user.id)
        print(USER)
    else:
        bot.send_message(message.chat.id,
                         "What has changed since the previous time?")


@bot.inline_handler(lambda query: len(query.query) > 0)
def query_text(query):
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton(
        text="Like", callback_data="data"))
    results = []
    single_msg = InlineQueryResultArticle(
        id="1", title="Press me",
        input_message_content=InputTextMessageContent(
            message_text="Inline message"),
        reply_markup=keyboard
    )
    results.append(single_msg)
    bot.answer_inline_query(query.id, results)


bot.polling()

