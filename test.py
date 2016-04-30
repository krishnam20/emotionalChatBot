import sys
import time
import pprint
import telepot
import random
from telepot.delegate import create_open
import json
from watson_developer_cloud import ToneAnalyzerV3Beta





tone_analyzer = ToneAnalyzerV3Beta(
   username='0e6e23c5-20c5-4c1e-bed5-f0b81751d3ef',
   password='2F5BGfic6OHZ',
   version='2016-02-11')

#print(json.dumps(tone_analyzer.tone(text='A word is dead when it is said, some say. Emily Dickinson'), indent=2))

analysis_string= 'A word is dead when it is said, some say. Emily Dickison'

# get result from watson
analysis_results = tone_analyzer.tone(analysis_string)

#convert analysis result into string
json_data_string = json.dumps(analysis_results, indent=2)

# put the string into the parsed_data
parsed_data = json.loads(json_data_string)

print ("Data from blue mix is all being parsed in parsed_data")


# creating the bot for the telegram

bot = telepot.Bot('213554370:AAE161babrJNopWyXCSFbL6rkQJw6nEgfsc')


def handle(msg):
    #print("This is the second message: ", msg)

    userMessage = msg['text']

    userid = msg['chat']['id']

    #print("this is the message ", msg)
    print ("This is the user ID ",userid)

    



    bot.sendMessage(userid, "Welcome to the semantic bots interview")
    message_list = ["Hello", "Hello How are you", "I am a chat bot"]
    print("about to print the content type")
    content_type, chat_type, chat_id = telepot.glance(msg)
    #print (content_type, chat_type, chat_id)

    bot.sendMessage(userid, userMessage)



    bot.sendMessage(userid,random.choice(message_list))

    bot.sendMessage(userid,'Hadooore, Hsadoooooreeeeee!!!')
 #   bot.sendMessage(chatID, 'http://www.yahoo.com \n no web page preview', disable_web_page_preview=True)




bot.message_loop(handle)
print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)

