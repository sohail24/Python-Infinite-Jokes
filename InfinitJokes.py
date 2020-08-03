import tkinter as tk
from tkinter import ttk
import pyjokes

root = tk.Tk()
root.geometry("1366x768+-2+0")
root.config(bg = '#15499E')
root.title("Infinite Jokes | Mini GUI Project By Sohail Ahmad")

T = tk.Label(root ,text = "Get Jokes Here..." ,bg = "#236eb0", fg = "white",font=("Sans", 15, "bold"))
T.place(x =25, y = 100 ,relwidth = 0.95, height = 300)

def generate_jokes():
    global joke
    joke = pyjokes.get_joke()
    T.config(text = joke ,fg = 'white')

button_clk = tk.Button(root,text = "Click To Get Next Joke", command = generate_jokes, bd =0 ,font=("Helvetica", 16))
button_clk.place(x = 25, y = 375, height = 50, relwidth = 0.95 )
#button_clk.pack()


root.mainloop()