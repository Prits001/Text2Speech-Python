import pyttsx3, threading
import customtkinter as ctk

engine = pyttsx3.init()
curvol = 100
currate = 150
curid = ''

engine.setProperty('volume', curvol)
engine.setProperty('rate', currate)

ids = []
voices = engine.getProperty('voices')
for voice in voices:
    ids.append([voice.name, voice.id, voice.gender, voice.age, voice.languages])
del engine, voices


def say_stuff():
    text = str(input_box.get())
    engine = pyttsx3.init()
    engine.setProperty('volume', curvol)
    engine.setProperty('rate', currate)
    engine.setProperty('voice', curid)
    engine.say(text)
    engine.runAndWait()
    del engine

def conv_stuff():
    text = str(input_box.get())
    engine = pyttsx3.init()
    engine.setProperty('volume', curvol)
    engine.setProperty('rate', currate)
    engine.setProperty('voice', curid)
    engine.save_to_file(text, 'Voice.mp3')
    engine.runAndWait()
    del engine

def on_buttonSay_click():
    for i in threading.enumerate(): 
        if i.name.startswith('Saying'): return
    th = threading.Thread(target=say_stuff,name="Saying")
    th.daemon = True
    th.start()


def on_buttonConv_click():
    for i in threading.enumerate(): 
        if i.name.startswith('Converting'): return
    th = threading.Thread(target=conv_stuff, name="Converting")
    th.daemon = True
    th.start()

def on_switch_toggle(choice):
    global curvol, currate, curid
    for array in ids:
        if array[0] == choice:
            id = array[1]
            curid = id
            break

def changeRate(rt):
    global curvol, currate, curid
    for i in threading.enumerate(): 
        if i.name.startswith('Saying') or i.name.startswith("Converting"): i.join()
    rate = 50 + rt * 500
    currate = rate
    rateLab.configure(text=f"Rate {int(rate)}")

def changeRateBT(rt):
    global curvol, currate, curid
    rate = 50 + rt * 500
    currate = rate
    rateLab.configure(text=f"Rate {int(rate)}")

def changeVolume(vol):
    global curvol, currate, curid
    for i in threading.enumerate(): 
        if i.name.startswith('Saying') or i.name.startswith("Converting"): i.join()
    curvol = vol
    volLab.configure(text=f"Volume {int(vol*100)}%")

def changeVolumeBT(vol):
    global curvol, currate, curid
    curvol = vol
    volLab.configure(text=f"Volume {int(vol*100)}%")


root = ctk.CTk()
root.geometry("600x450")

input_box = ctk.CTkEntry(root, width=520)
input_box.grid(row=0, column=0,columnspan=4, pady=40, padx=40)

voiceLab = ctk.CTkLabel(root, text="Voice:")
voiceLab.grid(row=1, column=0, padx=5, columnspan=2)

optionmenu_var = ctk.StringVar(value=ids[0][0])
switch_1 = ctk.CTkOptionMenu(root, values=[names[0] for names in ids], variable=optionmenu_var, command=on_switch_toggle)
switch_1.grid(row=1, column=1, pady=20, padx=5, columnspan=2)

button_1 = ctk.CTkButton(root, text="Play the Sound", command=on_buttonSay_click)
button_2 = ctk.CTkButton(root, text="Convert into a File", command=on_buttonConv_click)
button_1.grid(row=2, column=0, pady=20, padx=20, columnspan=2)
button_2.grid(row=3, column=0, pady=20, padx=20, columnspan=2)

volume_Sel = ctk.CTkSlider(root, command=changeVolumeBT)
volume_Sel.grid(row=2, column=2, columnspan=1, padx=10, pady=20)
volume_Sel.set(1)

volLab = ctk.CTkLabel(root, text="Volume 100%")
volLab.grid(row=2, column=3, padx=5)

volume_Sel = ctk.CTkSlider(root, command=changeRateBT)
volume_Sel.grid(row=3, column=2, columnspan=1, padx=10, pady=20)
volume_Sel.set(0.2)

rateLab = ctk.CTkLabel(root, text="Rate 150")
rateLab.grid(row=3, column=3, padx=5)

root.mainloop()
