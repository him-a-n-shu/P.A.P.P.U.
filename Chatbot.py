import random

Hello = ('hello','hey','hii','hi')
reply_Hello = ('Hello sir, I am Jarvis',
                'Hello, how are you'
                'Hi')

Bye = ('bye','exit','sleep','go')
reply_Bye = ('Bye sir',
            "It's Okay",
            "It's will be nice to meet you",
            "Bye",
            "Thanks",
            "Okay")

How_are_you = ('how are you')
reply_Howareyou = ('I am fine')

nice = ('nice','good','thanks')
reply_nice = ('Thanks',
                "ohh, It's  okay",
                "Thanks to you")

Functions = ['functions','abilities','what can you do','feathers']
replay_functions = ("I can perform many task or varieties of tasks, How can I help you?",
                    'I can message your mom that you are not studing',
                    'I can tell your class teacher that you had attended all the online classes',
                    'Let me ask first, How can I help you?')

sorry_reply = ("Sorry, that's beyond my abilities",
                "Sorry, I can't do that",
                "Sorry, that is not in my functions")

def ChatterBot(Text):
    Text = str(Text)
    for word in Text.split():
        if word in Hello:
            reply = random.choice(reply_Hello)
            return reply
        elif word in Bye:
            reply = random.choice(reply_Bye)
            return reply
        elif word in How_are_you:
            reply = random.choice(reply_Howareyou)
            return reply
        elif word in Functions:
            reply = random.choice(replay_functions)
            return reply
        else:
            return random.choice(sorry_reply)