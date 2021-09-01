import tkinter as tk
from tkinter import ttk
from tkinter import *
import webbrowser

app = tk.Tk()
app.title('Search system')
app.configure(background='white')

app_name = ttk.Label(app, text='Searching application', font='verdana 18 bold underline', foreground='purple')
app_name.grid(row=0, column=1)

search_label = ttk.Label(app, text='Search')
search_label.grid(row=1, column=0)

text_field = ttk.Entry(app, width=50)
text_field.grid(row=1, column=1)

search_engine = StringVar()
search_engine.set("google") # по умолчанию

def searching():
	if text_field.get().strip() != "":
		if search_engine.get() == "google":
			webbrowser.open('https://www.google.com/search?q=' + text_field.get())
		elif search_engine.get() == "yandex":
			webbrowser.open('https://yandex.ru/search/?lr=213&text=' + text_field.get())
		elif search_engine.get() == "wiki":
			webbrowser.open('https://ru.wikipedia.org/wiki/' + text_field.get())

def enterBtn(event):
	searching()

def clearing():
	text_field.delete(0, END)

btn_search = ttk.Button(app, text='Find', width=10, command=searching)
btn_search.grid(row=1, column=2)

btn_clear = ttk.Button(app, text='Clear', width=10, command=clearing)
btn_clear.grid(row=2, column=2)

text_field.bind('<Return>', enterBtn)


radio_google = ttk.Radiobutton(app, text='Google', value='google', variable=search_engine)
radio_google.grid(row=2, column=1, sticky=W) # W - west

radio_yandex = ttk.Radiobutton(app, text='Yandex', value='yandex', variable=search_engine)
radio_yandex.grid(row=2, column=1, sticky=E) # E - east

radio_wiki = ttk.Radiobutton(app, text='Wikipedia', value='wiki', variable=search_engine)
radio_wiki.grid(row=3, column=1)

app.wm_attributes('-topmost', True) #Приложение поверх остальных
text_field.focus() # сразу активное текстовое поле

app.mainloop()
