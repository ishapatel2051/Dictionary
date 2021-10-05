#!/usr/bin/env python
# coding: utf-8

# In[1]:





# In[1]:


import sys
get_ipython().system('{sys.executable} -m pip install PyDictionary')


# In[ ]:





# In[28]:


import tkinter as tk
from tkinter import ttk
from PyDictionary import PyDictionary

root = tk.Tk()
s = ttk.Style(root)
s.theme_use('xpnative')
root.title("Dictionay")
root.resizable(0,0)
root.geometry("300x200")
root.config(bg = '#3399ff')

def result(*args):
    word = text_entry.get()
    if word:
        try:
            dict = PyDictionary()
            mean_dict = dict.meaning(word)
        except exception as e:
            mean_dict = None
            label3['text'] = 'Error : \n'+str(e)
            
        if mean_dict:
            label1['text'] = word.capitalize()
            label2['text'] = "/".join(list(mean_dict.keys()))
            
            meaning_string = ''
            line_counter = 0
            for meanings in list(mean_dict.values())[0]:
                if len(meaning_string)<200:
                    line_counter+=1
                    s = meaning_string
                    meaning_string+=meanings.capitalize()+".\n"
                if line_counter==3:
                    break
                label3['text'] = s
                label3.config(fg = 'black')
            else:
                label1['text'] = word.capitalize()
                label2['text'] = "No such word found"
                label3.config(fg = 'red')
                label3['text'] = f"we can't find any match =>\n\"{word}\""

text_entry = ttk.Entry(root, width=20, font=("Sitka Small", 11), justify=tk.CENTER)
text_entry.bind("<Return>",result)
text_entry.place(x=10, y=21)

search_btn = tk.Button(root, text = "Search", bg= '#ffff00', fg='black', font=("Sitka Small", 9), width=7, relief=tk.FLAT, command=result)
search_btn.place(x=220,y=20)

output_frame = tk.Frame(root, bg='white')
output_frame.place(x=10, y=70, height=120, width=280)

label1 = tk.Label(output_frame,font=("Sitka Small", 12, 'bold'), bg= 'white', fg='black')
label1.place(x=10,y=5)

label2 = tk.Label(output_frame, font=("Sitka Small", 6, 'italic'), justify=tk.LEFT, fg='#8c8c8c', bg= 'white')
label2.place(x=10,y=30)

label3 = tk.Message(output_frame, width =250, font=("Sitka Small", 8), justify=tk.LEFT, bg= 'white', fg='black')
label3.place(x=10, y=45)

root.mainloop()

