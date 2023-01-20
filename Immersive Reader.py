import tkinter
import pyttsx3
import time
from tkinter.filedialog import askopenfile
from tkinter.filedialog import asksaveasfile
from tkinter.filedialog import asksaveasfilename
from tkinter import messagebox
from gtts import gTTS

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('rate', 160)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def read():

    reading_input = text_box.get("1.0", "end-1c")
    text = reading_input.split(' ')

    for word in text:
        word1 = word.strip('/n')
        if len(word1) < 5:
            p = 0.5
        else:
            p = 2.5
        if word1 == 'in' or word1 == 'In':
            speak('inn')
        elif word1.endswith('.'):
            speak(word1 + 'full stop')
        elif word1 == 'the' or word1 == 'The':
            speak('thee')
        elif word1 == 'not' or word1 == 'Not':
            speak('naught')
        elif word1.endswith("?"):
            speak(word1 + 'question mark')
        else:
            speak(word1)
        time.sleep(p)


def pause():
    engine.stop()


def read_only():
    t = (text_box.get('1.0', 'end-1c'))
    engine.say(t)
    engine.runAndWait()


def save_as_mp3():
    global text_box
    filetype = [('mp3 file', '*.mp3')]
    text = text_box.get('1.0', 'end-1c')
    tts = gTTS(text=text)
    s = asksaveasfilename(filetypes=filetype, defaultextension=filetype)
    tts.save(s)
    tkinter.messagebox.showinfo('Success!', 'File Saved successfully')


def new():
    global text_box

    text_box.destroy()
    text_box = tkinter.Text(text_frame, background='sky blue', fg='RoyalBlue4', font=('MV Boli', 12, 'bold'))
    text_box.grid(row=1, column=0, sticky='ew')


def nothing():
    print('hello')


def open_file():
    global text_box

    file = askopenfile(mode='r', filetypes=[('text file', '*.txt'), ('python files', '*.py'), ('PDF files', '*.pdf'),
                                            ('word files', '*.docx'), ('all files', '*.*')])
    if file is not None:
        content = file.read()
        text_box.delete(1.0, 'end')
        text_box.insert(1.0, content)


def select_all():
    text_box.tag_add('sel', '1.0', 'end')


def save_as():
    save_files = [('text file', '*.txt'),
                  ('python files', '*.py'),
                  ('PDF files', '*.pdf'),
                  ('word files', '*.docx'),
                  ('all files', '*.*')]
    file = asksaveasfile(filetypes=save_files, defaultextension=save_files)
    file.write(text_box.get('1.0', 'end-1c'))
    file.close()
    tkinter.messagebox.showinfo('Success', 'File Saved successfully')


def help_about():
    txt = 'How to use:'
    help_frame = tkinter.Tk()
    help_frame.geometry('500x500')
    label2 = tkinter.Label(help_frame, text=txt)
    label2.grid(row=0, column=0)
    help_frame.mainloop()


def female():
    engine.setProperty('voice', voices[1].id)


def male():
    engine.setProperty('voice', voices[0].id)


mainframe = tkinter.Tk()
mainframe.title('Immersive Reader')
mainframe.config(bg='bisque')
mainframe.geometry('1024x720')
mainframe['padx'] = 20

text_frame = tkinter.Frame(mainframe, background='bisque')
text_frame.grid(row=0, column=0, sticky='n')
label1 = tkinter.Label(text_frame, text='Enter your text here:', background='bisque')
label1.grid(row=0, column=0, sticky='w')
label1.configure(font=('MV Boli', 30, 'bold'), fg='RoyalBlue4')
text_box = tkinter.Text(text_frame, background='sky blue', fg='RoyalBlue4', font=('MV Boli', 12, 'bold'))
text_box.grid(row=1, column=0, sticky='ew')
text_scroll = tkinter.Scrollbar(text_frame, orient='vertical', command=text_box.yview)
text_scroll.grid(row=1, column=1, sticky='nsw', rowspan=2)
text_box['yscrollcommand'] = text_scroll.set

menubar = tkinter.Menu(mainframe)
filemenu = tkinter.Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=new)
filemenu.add_command(label="Open", command=open_file)
filemenu.add_command(label="Save", command=save_as)
filemenu.add_command(label="Save as...", command=save_as)
filemenu.add_command(label="Save as audio file", command=save_as_mp3)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=mainframe.quit)
menubar.add_cascade(label="File", menu=filemenu)

editmenu = tkinter.Menu(menubar, tearoff=0)

editmenu.add_command(label="Undo")
editmenu.add_separator()
editmenu.add_command(label="Cut")
editmenu.add_command(label="Copy")
editmenu.add_command(label="Paste")
editmenu.add_command(label="Select All", command=select_all)
editmenu.add_command(label="Delete")

editmenu.entryconfigure("Cut",
                        command=lambda: text_box.event_generate('<<Cut>>'))
editmenu.entryconfigure("Copy",
                        command=lambda: text_box.event_generate('<<Copy>>'))
editmenu.entryconfigure("Paste",
                        command=lambda: text_box.event_generate('<<Paste>>'))
editmenu.entryconfigure("Undo",
                        command=lambda: text_box.event_generate('<<Undo>>'))

menubar.add_cascade(label="Edit", menu=editmenu)
help_menu = tkinter.Menu(menubar, tearoff=0)
help_menu.add_command(label="About...", command=help_about)
menubar.add_cascade(label="Help", menu=help_menu)

frame = tkinter.Frame(mainframe, background='bisque')
frame.grid(row=1, column=0, sticky='n')
radio_label = tkinter.LabelFrame(frame, text='voices')
radio_label.grid(row=0, column=0, sticky='ns')

mainframe.columnconfigure(0, weight=1000)
mainframe.columnconfigure(1, weight=1000)

mainframe.rowconfigure(0, weight=100)
mainframe.rowconfigure(1, weight=100)

rb_value = tkinter.IntVar()
rb_value.set(1)

radio1 = tkinter.Radiobutton(radio_label, text='Male', value=1, variable=rb_value, command=male)
radio2 = tkinter.Radiobutton(radio_label, text='Female', value=2, variable=rb_value, command=female)
radio1.grid(row=0, column=0, sticky='w')
radio2.grid(row=1, column=0, sticky='w')
radio1.configure(font=('MV Boli', 10, 'bold'), fg='RoyalBlue4')
radio2.configure(font=('MV Boli', 10, 'bold'), fg='RoyalBlue4')

read_btn = tkinter.Button(frame, text='Call out', command=read, compound='top')
read_btn.grid(row=0, column=1, sticky='n')
read_btn.configure(font=('MV Boli', 10, 'bold'), fg='RoyalBlue4')
read_btn1 = tkinter.Button(frame, text='read', command=read_only, compound='top')
read_btn1.grid(row=0, column=3, sticky='n')
read_btn1.configure(font=('MV Boli', 11, 'bold'), fg='RoyalBlue4')
pause_btn = tkinter.Button(frame, text='Pause', compound='top', command=pause)
pause_btn.grid(row=0, column=2, sticky='n')
pause_btn.configure(font=('MV Boli', 10, 'bold'), fg='RoyalBlue4')

mainframe.config(menu=menubar)
mainframe.mainloop()