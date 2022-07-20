from typing_extensions import runtime
import telebot
from telebot.types import BotCommand, CallbackQuery, Message, MessageID, Sticker
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import urllib3
import json
import random
from newsapi import NewsApiClient
import requests
import os
import datetime
import time
import ast
from telebot import types
import schedule
#zamaniçin
simdikizaman= datetime.datetime.now()
text = str(simdikizaman)
print(text[:10])
    #aylık kullanım miktarı bitti
newsapi = NewsApiClient(api_key='FOR YOUR NEWS API KEY')
apikey = "YOUR GIF KEY"  # test value

# /v2/top-headlines
ap="FOR YOUR ANOTHER NEWS API KEY2"
top_headlines = newsapi.get_top_headlines(q='news',
                                            sources='bbc-news,the-verge',
                                            #category='',
                                            language='en',
                                            )
all_articles2 = newsapi.get_everything(q='sports',
                                        from_param=text[:10],
                                        to=text[:10],
                                        language='en',
                                        sort_by='relevancy',
                                        page=2)

url12=("https://newsapi.org/v2/top-headlines?country=tr&category=technology&apiKey=YOURAPIKEY")
response12=requests.get(url12)
jsonverisi12=response12.json()
#print(jsonverisi["articles"]) türk haberleri
diziurl12=[]
dizidescription12=[]
dizitittle12=[]
for i in jsonverisi12["articles"]: 
    dizitittle12.append(i['title'])
    diziurl12.append (i['url'])
    dizidescription12.append(i['description'])
# /v2/everything
all_articles3 = newsapi.get_everything(q='bitcoin',
                                        from_param=text[:10],
                                        to=text[:10],
                                        language='en',
                                        sort_by='relevancy',
                                        page=2)
all_articles4 = newsapi.get_everything(q='games',
                                        from_param=text[:10],
                                        to=text[:10],
                                        language='en',
                                        sort_by='relevancy',
                                        page=2)
all_articles5 = newsapi.get_everything(q='technology',
                                        from_param=text[:10],
                                        to=text[:10],
                                        language='en',
                                        sort_by='relevancy',
                                        page=2)
selfd = newsapi.get_sources()
diziurl=[]
dizidescription=[]
dizitittle=[]
diziurl2=[]
dizidescription2=[]
dizitittle2=[]
diziurl3=[]
dizidescription3=[]
dizitittle3=[]
diziurl4=[]
dizidescription4=[]
dizitittle4=[]
diziurl5=[]
dizidescription5=[]
dizitittle5=[]
for i in selfd['sources']: 
    diziurl3.append (i['url'])
    dizidescription3.append(i['description'])
for i in all_articles4['articles']:
    dizitittle4.append(i['title'])
    diziurl4.append (i['url'])
    dizidescription4.append(i['description'])
for i in all_articles3['articles']:
    dizitittle.append(i['title'])
    diziurl.append (i['url'])
    dizidescription.append(i['description'])
for i in all_articles2['articles']:    
    dizitittle2.append(i['title'])
    diziurl2.append (i['url'])
    dizidescription2.append(i['description'])
for i in selfd['sources']: 
    diziurl3.append (i['url'])
    dizidescription3.append(i['description'])
for i in all_articles5['articles']: 
    dizitittle5.append(i['title'])
    diziurl5.append (i['url'])
    dizidescription5.append(i['description'])
    #aylık kullanım miktarı bitti
    #url = "http://data.fixer.io/api/latest?access_key=YOURAPIKEY&base=eur&symbols=TRY,CNY,USD,GBP"
    #response = requests.get(url)
    #data = response.text
    #parsed = json.loads(data)
url="http://api.currencylayer.com/live?access_key=YOURAPIKEY&format=1"
    #data = response.text
data=requests.get(url)
parsed=data.json()
#print(parsed["rates"]["USDTRY"])
url2="https://api.mojilala.com/v1/stickers/search?q=cat&api_key=YOURAPIKEY"
response2=requests.get(url2)
jsonverisi=response2.json()
gif = []
png =[]
for i in range(0,50):
    sas = jsonverisi['data'][i]['images']['fixed_height']['url']       
    if sas[-4:] !=".png":
            gif.append(sas)
    else:
            png.append(sas)
url3=("https://g.tenor.com/v1/categories?key="+apikey)
response2=requests.get(url3)
jsonverisi2=response2.json()
gifurl = []
gifname=[]
for i in  range(0,55):
    gifname.append(jsonverisi2['tags'][i]['searchterm'])
    gifurl.append(jsonverisi2["tags"][i]['image'])
bugun = datetime.datetime.now()
DATE = datetime.date.today().day
HOUR = datetime.datetime.now().hour
print(DATE, HOUR)
dgkdeneme = datetime.datetime(1997,1,11)
dgkmami = datetime.datetime(1997,7,20)
dgkonur = datetime.datetime(1998,6,22)
dgkzekeriya = datetime.datetime(1990,9,24)
dgkyusuf = datetime.datetime(1996,7,28)
dgkyunus = datetime.datetime(1996,1,16)
dgkfurkan = datetime.datetime(1996,5,14)
dgkferidun = datetime.datetime(1992,12,23)
#yasmami = bugun.year-dgkmami.year
bot = telebot.TeleBot("5159408560:YOURAPIKEY-B_E")
#https://api.telegram.org/bot<your-bot-token>/getme
#https://api.telegram.org/bot5057886601:AAHo74NywuqV58s52ZL7HJoBfmV8QxMTvHQ/getUpdates
ogrenilensorular=['kemal','chp','turk news','sorular','dating','app','who are you','how are you','gif','gifcat','oyunlar','gifnervous','gifsleepy','haberler','','sıkıldım','nasılsın','kimsin','start','selam','help','merhaba','parabirimleri','para birimleri','currencies','durum','merhaba','ne işe yararsın','GIF','gifsıkılmak','giftired','gifyorulmak','gifbored','giflaughft','gifgülmek','wedding','pngcat']
# bot.forward_message('Hoşgeldin',1522868005,MessageID)
sobet = ['selam','kimsin','nasılsın','ne işe yararsın']
oyun = ['oyunlar','haberler','gifler','Parabirimleri']
bulmaca = ['bulmaca','sorular']
if (HOUR == 17):
    sayac=0
sayac = 1
if sayac<2:
    print(HOUR)
    if (HOUR==10 or HOUR==11 or HOUR==12 or HOUR ==16):
        sayac+1
        if(bugun.month==dgkmami.month and bugun.day == dgkmami.day):
            bot.send_photo(1522868005,photo=open('indir2.png', 'rb'))
            bot.send_message(1522868005,"Happy birthday my creator  ....")
        elif(bugun.month==dgkonur.month and bugun.day == dgkonur.day):
            bot.send_photo(-1001518478516,photo=open('indir2.png', 'rb'))
            bot.send_message(-1001518478516,"Happy birth day Onur....")
        elif(bugun.month==dgkferidun.month and bugun.day == dgkferidun.day):
            bot.send_photo(-1001518478516,photo=open('indir.jpg', 'rb'))
            bot.send_message(-1001518478516,  "Happy birth day Agent47 (Feridun) !!!!!") 
        elif(bugun.month==dgkzekeriya.month and bugun.day == dgkzekeriya.day):
            bot.send_photo(-1001518478516,photo=open('indir2.png', 'rb'))
            bot.send_message(-1001518478516,"Happy birth day Zekariya....")     
        elif(bugun.month==dgkyusuf.month and bugun.day == dgkyusuf.day):
            bot.send_photo(-1001518478516,photo=open('indir2.png', 'rb'))
            bot.send_message(-1001518478516,"Happy birth day Yusuf ....")
        elif(bugun.month==dgkyunus.month and bugun.day == dgkyunus.day):
            bot.send_photo(-1001518478516,photo=open('indir2.png', 'rb'))
            bot.send_message(-1001518478516,"Happy birth day Yunus ....")
        elif(bugun.month==dgkfurkan.month and bugun.day == dgkfurkan.day):
            bot.send_photo(-1001518478516,photo=open('indir2.png', 'rb'))
            bot.send_message(-1001518478516,"Happy birth day Furkan ....")     
        elif(bugun.month==dgkdeneme.month and bugun.day == dgkdeneme.day):
            bot.send_photo(1522868005,photo=open('yunus.jpg', 'rb'))
            bot.send_message(1522868005,"Happy birth day deneme ")                                
@bot.message_handler(commands=ogrenilensorular[:])
def send_welcome(message):
    string = message.text
    print(string[1:])
    print(message.text)
    print(message.chat.id)        
    if (message.text.capitalize()== "/start"):
        bot.reply_to(message, "The bot has been successfully launched. You can type /help for commands you can type... \U0001F916")
    elif(message.text.lower()=="/help"):
        bot.reply_to(message,"chat commands you can reach me..: "+str(sobet[:])+"\nGame Commands ..: "+str(oyun[:])+"\n Puzzle commands..:"+str(bulmaca[:]))
    elif (message.text.lower()=="/haberler"):
        bot.reply_to(message,"For news sites: news site, for news categories you can access immediately ..: Bitcoin, Sports, Teknology,etc..")
    elif (message.text.lower()=="/clear"):
        os.system("cls" if os.name == "nt" else "clear")
    elif (message.text.lower()=="/oyunlar"):
        bot.reply_to(message,"Seni bire Oyun kategorileri ...: Bulmaca , Adam asmaca")
    elif (message.text.lower()=="/ssss"):
        bot.reply_to(message,"Seni bire Oyun kategorileri ...: Bulmaca , Adam asmaca")
    elif (message.text.lower()=="/parabirimleri" or message.text.lower()=="/para birimleri" or message.text.lower()=="/currencies"):
        bot.reply_to(message,"For currencies, simply type /para or /money")
    elif (message.text.lower()=="/kimsin" or message.text.lower()=="/ne işe yararsın" or message.text.lower()=="/who are you"):
        bot.reply_to(message, "\U0001F916 My developer created me for you. I coded in a simple way via python using telegram api. I can answer some of your questions. You can type /help to find out.")
    elif (message.text.lower()=="/nasılsın" or message.text.lower()=="/durum" or message.text.lower()=="/how are you"):
        bot.reply_to(message, "Sanırım iyiyim \n ")
    elif (message.text.lower()=="/chp" or message.text.lower()=="/kılıçdaroğlu" or message.text.lower()=="/kemal"):
            bot.reply_to(message, "dedemm yaaaaaa \n ")             
    elif (message.text.lower()=="/gülçin kim"):
        bot.reply_to(message, "Yartıcımın hayatının aşkı.. yani seni öyle tanımlamış \n ")
    elif(message.text.lower()=="/selam" or message.text.lower()=="/merhaba"):
        bot.reply_to(message, "Hello and welcome, I can help you with limited transactions right now and unfortunately I can answer a few questions \U0001F916")
    elif(message.text.lower()=="/wedding" or message.text.lower()=="/düğün"):
        bot.reply_to(message, "bikarlar: yunus, yusuf \U0001F609") 
    elif(message.text.lower()== "/gifcat"):
        ran = random.randint(0,9)
        print(gif[ran])  
        bot.send_sticker(chat_id=message.chat.id, data=gif[ran])
    elif(message.text.lower()== "/pngcat"):
        ran = random.randint(0,40)
        print(png[ran])  
        bot.send_photo(chat_id=message.chat.id, photo=png[ran])
    elif(message.text.lower()== "/gif" or message.text.lower()=="/GIF"):
        ran = random.randint(0,55)
        #bot.send_message(1522868005,"GIF name is ...: "+str(gifname[ran]))
        bot.send_sticker(chat_id=message.chat.id, data=gifurl[ran])
    elif(message.text.lower()== "/giflaughft" or message.text.lower()=="/gifgülmek"):
        ran = random.randint(0,55)
        #bot.send_message(1522868005,"GIF name is ...: "+str(gifname[ran]))
        bot.send_sticker(chat_id=message.chat.id, data="https://media.tenor.com/images/85beb6c5fd3baea71dc8502e09bc5b2c/tenor.gif")
    elif(message.text.lower()== "/giftired" or message.text.lower()=="/gifyorulmak" or message.text.lower()=="/gifsleepy"):
        ran = random.randint(0,55)
        #bot.send_message(1522868005,"GIF name is ...: "+str(gifname[ran]))
        bot.send_sticker(chat_id=message.chat.id, data="https://media.tenor.com/images/815a7cd9ba42f91700acfc5579bee3ee/tenor.gif")
    elif(message.text.lower()== "/gifbored" or message.text.lower()=="/gifsıkılmak"):
        ran = random.randint(0,55)
        #bot.send_message(1522868005,"GIF name is ...: "+str(gifname[ran]))
        bot.send_sticker(chat_id=message.chat.id, data="https://media.tenor.com/images/b6aa13ef42baa403e0472e350a4eb9ed/tenor.gif")
    elif(message.text.lower()== "/gifnervous" or message.text.lower()=="/giftedirgin"):
        ran = random.randint(0,55)
        bot.send_sticker(chat_id=message.chat.id, data="https://media.tenor.com/images/9fb0999caf3b46e5763b4c0d3dd5357b/tenor.gif")
    elif(message.text.lower()=="/dating" or message.text.lower()=="/app"):
        bot.reply_to(message, "You can use , Tinder , Swarm ,OkCupid , Siberalem, Muslima \U0001F609")
stringList = {"USD": "1 USD/EUR", "CNY": "1 USD / CNY", "TRY": "1 USD / TRY"}
crossIcon = u"\u274C"
def makeKeyboard():
    markup = types.InlineKeyboardMarkup()
    for key, value in stringList.items():
        markup.add(types.InlineKeyboardButton(text=value,
                                                callback_data="['value', '" + value + "', '" + key + "']"),
        types.InlineKeyboardButton(text=crossIcon,
                                    callback_data="['key', '" + key + "']"))
    return markup
@bot.message_handler(commands=['para','money','PARA','MONEY'])
def handle_command_adminwindow(message):
    bot.send_message(chat_id=message.chat.id,
                        text="Just click which unit you want to choose from below \U0001F609",
                        reply_markup=makeKeyboard(),
                        parse_mode='HTML')
    print("---------------------------")
    print(message.chat.id)
@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):
    if (call.data.startswith("['value'")):
        print(f"call.data : {call.data} , type : {type(call.data)}")
        print(f"ast.literal_eval(call.data) : {ast.literal_eval(call.data)} , type : {type(ast.literal_eval(call.data))}")
        valueFromCallBack = ast.literal_eval(call.data)[1]
        keyFromCallBack = ast.literal_eval(call.data)[2]
        print(keyFromCallBack)
        if (keyFromCallBack=="USD"):
            bot.answer_callback_query(callback_query_id=call.id,
                                show_alert=True,
                                text="You Clicked " + valueFromCallBack + " and  " + str(parsed["quotes"]["USDEUR"]))
        elif(keyFromCallBack=="CNY"):
            bot.answer_callback_query(callback_query_id=call.id,
                                show_alert=True,
                                text="You Clicked " + valueFromCallBack + " and  " + str(parsed["quotes"]["USDCNY"])) 
        elif(keyFromCallBack=="TRY"):
            bot.answer_callback_query(callback_query_id=call.id,
                                show_alert=True,
                                text="You Clicked " + valueFromCallBack + " and  " + str(parsed["quotes"]["USDTRY"]))                              
    if (call.data.startswith("['key'")):
            keyFromCallBack = ast.literal_eval(call.data)[1]
            del stringList[keyFromCallBack]
            bot.edit_message_text(chat_id=call.message.chat.id,
                                text="Just click which unit you want to choose from below",
                                message_id=call.message.message_id,
                                reply_markup=makeKeyboard(),
                                parse_mode='HTML')
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    print() 
    string =message.text.lower()
    kategori=string[4:]
    sayac = 0
    print(gifname)
    print("---------------------------------------")
    for i in range(len(gifname)):
        print(gifname[i])
        if (gifname[i]==str(kategori)):
                print("++++++++++++++++++++++++++++++++++++++++++++++++++")
                katurl = gifname.index(kategori)
                bot.send_sticker(chat_id=message.chat.id, data=gifurl[katurl])
                sayac=1
                print(sayac)
                break   
    if (message.text.lower()=="/bitcoin"):
            ran = random.randint(1,15)
            bot.reply_to(message,dizitittle[ran]+" -- "+dizidescription[ran]+" LINK .: "+diziurl[ran])
    elif (message.text.lower()=="/spor" or message.text.lower()=="/sports"  ):
            ran = random.randint(1,15)
            bot.reply_to(message,dizitittle2[ran]+" -- "+dizidescription2[ran]+"\n LINK .: "+diziurl2[ran])
    elif (message.text.lower()=="/games"):
            ran = random.randint(0,14)
            bot.reply_to(message,dizitittle4[ran]+" -- "+dizidescription4[ran]+"\n LINK .: "+diziurl4[ran])
    elif (message.text.lower()=="/haber sitesi" or message.text.lower()=="/habersitesi" or message.text.lower()=="/new site"  ):
            ran = random.randint(0,14)
            bot.reply_to(message,dizidescription3[ran]+"\n LINK .: "+diziurl3[ran])
    elif (message.text.lower()=="/teknoloji" or message.text.lower()=="/technology" or message.text.lower()=="/tekno"  ):
            ran = random.randint(0,14)
            bot.reply_to(message,dizidescription5[ran]+"\n LINK .: "+diziurl5[ran])
    elif (message.text.lower()=="/turk news" or message.text.lower()=="/turkhaber" or message.text.lower()=="/turk haber"  ):
            ran = random.randint(0,14)
            bot.reply_to(message,dizitittle[ran]+"\n"+dizidescription12[ran]+"\n LINK .: "+diziurl12[ran])
    else:
        if sayac<=0:
            bot.reply_to(message, "Unlearned command... These are the commands I know for now \uE404 ..: \n "  + str(ogrenilensorular[:]))
        else:
            sayac=0
            #kullanıcıdizi.append(message.text)
while True:
    try:
        bot.polling(none_stop=True, interval=0, timeout=0)
    except:
        time.sleep(5)
 