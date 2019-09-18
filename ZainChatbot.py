# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 18:54:00 2019

@author: Administrator
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 19:03:58 2019

@author: Administrator
"""


import random
import pandas as pd
import re

GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up","hey", "good morning")
GREETING_RESPONSES = ["hi", "hey", "*nods*", "hi there", "hello", "I am glad! You are talking to me"]
def greeting(sentence):
 
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)
        

def zainResponse(user_response):
    user_response=user_response.lower()
    
    question=pd.read_csv('C:\\Users\\Administrator.Omnisec421_05\\.spyder-py3\\chatbots\\questions.csv', encoding='unicode_escape')
    answer=pd.read_csv('C:\\Users\\Administrator.Omnisec421_05\\.spyder-py3\\chatbots\\answers.csv', encoding='unicode_escape')
    wh=question['Question'].values
    an=answer['Answer'].values
    found=False
    for i in range(len(wh)):
        wh[i]=wh[i].lower()
        wh[i]=re.sub(r"[.?!,:;& #%^*$@+*/|]", "",wh[i])
        if user_response in wh[i]:
            print(an[i])
            found=True
    if (found==False):
        print("I don't understand you, how can i help you?")
    
    
    
    
flag=True
print("ZOZA> Hi my name is ZOZA. I'm Zain's virtual agent. I will answer your queries about zain services. If you want to exit, type Bye!")

while(flag==True):
    user_response = input('>>> ').strip()
    user_response=user_response.lower()
    user_response=re.sub(r"[.?!,:;& #%^*$@+*/|]", "",user_response)
    caseGree=re.findall(r"hello|hi|greetings|sup|what's up||hey|good morning",user_response )
    casebye=re.findall(r"bye|good bye", user_response)
    if(casebye!='bye' and casebye!='good bye' ):
        if(user_response=='thanks' or user_response=='thank you' ):
            flag=False
            print("ZOZA> You are welcome..")
        elif (user_response == "nothing" or user_response=="nothing else"):
            flag=False
            print("ZOZA> Thank you for your time.. feel free to ask me any question later...bye")
    
        else:
            if(greeting(user_response)!=None):
                print("ZOZA> "+greeting(user_response))
                print("ZOZA> How can I help you?")
            elif (user_response=='what' or user_response=='why' or user_response=='no' or user_response=='yes'):
                print('What do you want? please, ask another question.')
            else:
                print("ZOZA> ",end=" ")
#                print(response(user_response))
#                sent_tokens.remove(user_response)
                zainResponse(user_response)
                
    else:
        flag=False
        print("ZOZA> Bye! Have a nice day..")
        

