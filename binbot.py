import telebot
from telebot import types

from bs4 import BeautifulSoup
import requests

TOKEN = '5111791155:AAEafi5YH6Kq_QvpbOc8mklKvdOUjAIQ-Rs'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start','help','about'])
def send_welcome(message):
    if message.text == '/start':
        bot.reply_to(message, '''Привет, я телеграм бот по всем новостям в мире криптовалюты.
Наберите '/help', чтобы узнать подробнее''')

    elif message.text == '/help':
        bot.send_message(message.from_user.id,'''Бот работает с Bitcoin(BTC), Ethereum(ETH), Ripple(XRP)
Выбрать криптовалюту - /crypto
Узнать новости из мира криптовают - /news''')

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    if message.text == '/crypto':
        keyboard = types.InlineKeyboardMarkup()

        key_btc = types.InlineKeyboardButton(text='BTC', callback_data='BTC')
        keyboard.add(key_btc)

        key_eth = types.InlineKeyboardButton(text='ETH', callback_data='ETH')
        keyboard.add(key_eth)

        key_doge = types.InlineKeyboardButton(text='XRP', callback_data='XRP')
        keyboard.add(key_doge)

        bot.send_message(message.from_user.id, text='Выберите валюту',reply_markup=keyboard)

        @bot.callback_query_handler(func=lambda call: True)
        def callback_worker(call):
            if call.data == "BTC":
                BTC_RUB = 'https://www.google.com/search?q=BTC&sxsrf=AOaemvKXmuxFTD-clGAZ0E4WJNSSFlIRMQ%3A1642791496456&ei=SALrYYWoG8fmrgTK8I-4DQ&ved=0ahUKEwiF7Necw8P1AhVHs4sKHUr4A9cQ4dUDCA4&uact=5&oq=BTC&gs_lcp=Cgdnd3Mtd2l6EAMyEAgAEIAEELEDEIMBEEYQggIyCwgAEIAEELEDEIMBMgsIABCABBCxAxCDATILCAAQgAQQsQMQgwEyCAgAELEDEIMBMgUIABCABDILCAAQgAQQsQMQgwEyCAgAELEDEIMBMggIABCABBCxAzILCAAQgAQQsQMQgwE6BwgjEOoCECc6BAgjECc6CwguEIAEEMcBEKMCOggILhCABBCxA0oECEEYAEoECEYYAFDtC1jJEGCbEmgCcAF4AIABbogBlgKSAQMyLjGYAQCgAQGwAQrAAQE&sclient=gws-wiz'

                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'}

                full_page = requests.get(BTC_RUB, headers=headers)

                soup = BeautifulSoup(full_page.content, 'html.parser')
                convert = soup.findAll("span", {"class": "pclqee"})

                btc = convert[0].text
                bot.send_message(call.message.chat.id, f"Сейчас курс биткоина = {btc} рублей")

            elif call.data == "ETH":
                ETH_RUB = 'https://www.google.com/search?q=eth+%D0%BA%D1%83%D1%80%D1%81&sxsrf=AOaemvKEITkyO7Ww_BiQYMYyPMkhDfbINA%3A1642792405478&ei=1QXrYdWfHMmsrgSj2Lgw&oq=eth+&gs_lcp=Cgdnd3Mtd2l6EAEYADIHCAAQRxCwAzIHCAAQRxCwAzIHCAAQRxCwAzIHCAAQRxCwAzIHCAAQRxCwAzIHCAAQRxCwAzIHCAAQRxCwAzIHCAAQRxCwAzIHCAAQsAMQQzIHCAAQsAMQQ0oECEEYAEoECEYYAFCeA1ieA2D3B2gBcAJ4AIABAIgBAJIBAJgBAKABAcgBCsABAQ&sclient=gws-wiz'

                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'}

                full_page = requests.get(ETH_RUB, headers=headers)

                soup = BeautifulSoup(full_page.content, 'html.parser')
                convert = soup.findAll("span", {"class": "hgKElc"})

                eth = convert[0].text
                bot.send_message(call.message.chat.id, f"{eth}")

            elif call.data == "XRP":
                XRP_RUB = 'https://www.google.com/search?q=xrp+%D0%BA%D1%83%D1%80%D1%81&sxsrf=AOaemvKEyHOnZ1bT7fTUXHdBnnjGKeS9og%3A1642794799877&ei=Lw_rYaHxNOelrgSzmb-oCw&ved=0ahUKEwjhxPDDz8P1AhXnkosKHbPMD7UQ4dUDCA4&uact=5&oq=xrp+%D0%BA%D1%83%D1%80%D1%81&gs_lcp=Cgdnd3Mtd2l6EAMyDQgAEIAEEIcCELEDEBQyBAgAEEMyCggAEIAEEIcCEBQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEOgcIABBHELADOgcIABCwAxBDOgQIIxAnOggIABCABBCxAzoHCAAQsQMQQ0oECEEYAEoECEYYAFCDAVjwGWCwG2gBcAJ4AIABcogB0QeSAQM5LjKYAQCgAQHIAQrAAQE&sclient=gws-wiz'

                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'}

                full_page = requests.get(XRP_RUB, headers=headers)

                soup = BeautifulSoup(full_page.content, 'html.parser')
                convert = soup.findAll("div", {"class": "IZ6rdc"})

                xrp = convert[0].text
                bot.send_message(call.message.chat.id, f"Курс Ripple = {xrp}")

bot.infinity_polling()