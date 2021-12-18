from tkinter import *
import tkinter as tk
from functools import partial
import os
import random
import msvcrt as m


def text_label(txt):
    return Message(root, textvariable=txt, font=("Arial","80"),justify=CENTER,width=1800)

def category_button(txt):
    b = Button(root, text=txt)
    return b

def button_click(txt):
    quest, a, b = get_question_ans_set(txt, grouped_dict)
    text.set(quest[0])
    live_cat.set(txt)
    live_index.set(b)

def get_answer():
    text.set(grouped_dict[live_cat.get()][int(live_index.get())][1])
    grouped_dict[live_cat.get()].pop(int(live_index.get()))

def clear():
    text.set("")

def get_question_ans_set(category, group_dict):
    questions = group_dict[category]
    rand = random.randint(0, len(questions)-1)
    # gives [question, answer], questions left, question index
    return questions[rand], len(questions)-1, rand

#finding absolute path for this device
#dirname = os.path.dirname(__file__)
#fq = os.path.join(dirname, 'questions.txt')

#parsing through txt input
with open("questions.txt") as questions:
    lines = questions.readlines()
    qlist = []
    for l in lines:
        as_list = l.split("; ")
        qlist.append([as_list[0], as_list[1], as_list[2].strip()])

grouped_dict = {}

# {Category1:[[Q1, A1],[Q2, A2]], Category2:[[Q1, A1],[Q2, A2]]}
for group in qlist:
    if group[1] not in grouped_dict.keys():
        grouped_dict[group[1]] = [[group[0], group[2]]]
    else:
        grouped_dict[group[1]].append([group[0], group[2]])

categories = list(grouped_dict.keys())

root = Tk()
sideWindow = tk.Toplevel(root)
root.title("HOOSmarter")
root.configure(background="#0b48a6")



text = StringVar()
text.set('')

live_cat = StringVar()
live_cat.set('')
live_index = StringVar()
live_index.set('')

myLabel = text_label(text)
myLabel.configure(background="#0b48a6")
myLabel.place(anchor="c", relx=.5, rely=.5)
myLabel.configure(fg="#f48a4a")

i = 2
buttons = []
for category in categories:
    buttons.append(Button(sideWindow, text=category, command=partial(button_click, category)))

for button in buttons:
    button.grid(row=0, column=i)
    i += 1

answer_button = Button(sideWindow, text="ANSWER", command=get_answer)
answer_button.grid(row=0,column=1)

clear_button = Button(sideWindow, text="CLEAR", command=clear)
clear_button.grid(row=0,column=0)

root.mainloop()
