import sys
import time
import pprint
import telepot
import random
from telepot.delegate import create_open
import json
from watson_developer_cloud import ToneAnalyzerV3Beta
import IBMmethod





#print(json.dumps(tone_analyzer.tone(text='A word is dead when it is said, some say. Emily Dickinson'), indent=2))

#analysis_string= 'A word is dead when it is said, some say. Emily Dickison'




# creating the bot for the telegram

bot = telepot.Bot('213554370:AAE161babrJNopWyXCSFbL6rkQJw6nEgfsc')


def handle(msg):
    #print("This is the second message: ", msg)

    userMessage = msg['text']
    print(userMessage)
    userid = msg['chat']['id']
    #print("this is the message ", msg)
    print ("This is the user ID ",userid)

    


    bot.sendMessage(userid, "Welcome to the semantic bots interview")
    message_list = ["Hello", "Ohhh no I never thought you said that", 
            "I am a chat bot", "I am a very handsome chatbot", "yummmmm",
            "Once your a Hadooore,you are always a haodooooooreee!!!"]
    #print("about to print the content type")
    content_type, chat_type, chat_id = telepot.glance(msg)
    #maxEmotion = IBMmethod.IBMAlgorithm(userMessage, userid)
    #print (content_type, chat_type, chat_id)

# get the IBM API for the semantic expression
    parsed = IBMmethod.parse_data(userMessage)

# this send MEssage is to send back HEllo, and Hello how are you
    bot.sendMessage(userid,random.choice(message_list))

# this send message is to return the biggest score mood and return that
    bot.sendMessage(userid, "Honestly, You are in "+parsed)



    #bot.sendMessage(userid,'Hadooore, Hsadoooooreeeeee!!!')




bot.message_loop(handle)
print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)

