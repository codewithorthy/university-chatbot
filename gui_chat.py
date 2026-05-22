import tkinter as tk
from tkinter import *
# Ekhane chat.py theke function gulo import korte hobe
# (Dhori apnar chat.py te get_response function-ti ache)
from chat import get_response, predict_class, intents

def send():
    msg = EntryBox.get("1.0", 'end-1c').strip()
    EntryBox.delete("0.0", END)

    if msg != '':
        ChatLog.config(state=NORMAL)
        ChatLog.insert(END, "You: " + msg + '\n\n')
        ChatLog.config(foreground="#4422ee", font=("Verdana", 12 ))

        # Chatbot er response neya
        ints = predict_class(msg)
        res = get_response(ints, intents)

        ChatLog.insert(END, "Bot: " + res + '\n\n')
        ChatLog.config(state=DISABLED)
        ChatLog.yview(END)

base = tk.Tk()
base.title("My AI Chatbot")
base.geometry("400x500")
base.resizable(width=FALSE, height=FALSE)

# Chat Window
ChatLog = Text(base, bd=0, bg="white", height="8", width="50", font="Arial",)
ChatLog.config(state=DISABLED)

# Scrollbar
scrollbar = Scrollbar(base, command=ChatLog.yview, cursor="heart")
ChatLog['yscrollcommand'] = scrollbar.set

# Send Button
SendButton = Button(base, font=("Verdana", 12, 'bold'), text="Send", width="12", height=5,
                    bd=0, bg="#32de97", activebackground="#3c9d9b", fg='#ffffff',
                    command=send)

# Text Entry Box
EntryBox = Text(base, bd=0, bg="white", width="29", height="5", font="Arial")

# Place all components on screen
scrollbar.place(x=376, y=6, height=386)
ChatLog.place(x=6, y=6, height=386, width=370)
EntryBox.place(x=128, y=401, height=90, width=265)
SendButton.place(x=6, y=401, height=90)

base.mainloop()