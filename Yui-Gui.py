from tkinter import *
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import time
time.clock = time.time                                                          #this because the time.clock wont work
import os
import pyttsx3

#creating the object bot and gving it a name yui
bot = ChatBot('Yui')

#creating the trainer object for the bot
trainer = ListTrainer(bot)

#loop for files in english folder
#for files in os.listdir('data/english/'):
data = open('conversations.yml','r',encoding='utf-8').readlines()          #getting the data for training the chatbot
trainer.train(data)                                                         #training the bot with the data


#when clicked enter or send this function runs where conversation happens between user and yui
def botreply():
    que = messWindow.get()
    ans = bot.get_response(que)                                                 #copies the question from the textarea and stores answer in ans
    chatWindow.insert(END,'You:'+que+'\n')
    chatWindow.insert(END,'Yui:'+str(ans)+'\n')
    #pyttsx3.speak(ans)                                                          #makes yui read it aloud
    messWindow.delete(0,END)                                                     #deletes the contenet from message window after submiting


#creating the window GUI for the chat bot
root = Tk()

root.title("Yui")

root.geometry('400x450')
root.minsize(400,450)
root.maxsize(400,450)

#create a chat window
chatWindow = Text(root,bd=1,bg='black',width=50,height=8,fg='White',font=('Arial',10))
chatWindow.place(x=6,y=6,height=385,width=370)
chatWindow.insert(END,"Yui: Hi I am Yui,how can i help you"+'\n')


#create window for text messages
messWindow = Entry(root,bd=1,bg='white',width=30,fg='black',font=('Arial',10))
messWindow.place(x=6,y=400,height=38,width=250)

#create a button to send text
senbttn = Button(root,text='Send',bg='green',activebackground='light blue',width=12,height=5,font=('Arial',12), command=botreply)
senbttn.place(x=260,y=400,height=38,width=120)

#add scrollbar
scrball = Scrollbar(root,command=chatWindow.yview())
scrball.place(x=375,y=5,height=385)

#binding the enter key
def  click(event):
    senbttn.invoke()
root.bind('<Return>',click)
root.mainloop()