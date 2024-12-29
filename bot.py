from models import get_models
from wiki_collection import get_wiki_collection
from search import search_page, get_answer
import telebot

retriever, reranker, qa = get_models()
wiki = get_wiki_collection()

def wiki_search(query):
  doc, url = search_page(query, wiki, retriever, reranker)
  summary = doc[:200]+'...'
  answer = get_answer(qa, query, doc)
  return f"{answer}\n{'='*10}\n{summary}\n{'='*10}\n{url}"

BOT = telebot.TeleBot('7663049239:AAEts0Igzfkyttz4DVkHJd_HNIeYWcWXsqU')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "/start":
        BOT.send_message(message.from_user.id, "Здравствуйте, я WikiBot. Что вы хотите узнать?")
    else:
        BOT.send_message(message.from_user.id, "Ваш запрос обрабатывается. Пожалуйста, подождите.")
        query = message.text
        answer = wiki_search(query)
        BOT.send_message(message.from_user.id, answer)

if __name__=="__maint__":
  BOT.polling(none_stop=True, interval=0)
